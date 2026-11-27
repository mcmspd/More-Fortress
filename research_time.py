#!/usr/bin/env python3
"""Minimum research time for a Warzone 2100 research topic, structure, or weapon.

Rate model calibrated against https://aco4.github.io/wz/mrt/ (generator:
https://github.com/aco4/wz/blob/main/mrt/make.py). Single research queue,
per-second rate from one fully-moduled lab, research-speed upgrades applied
the moment their branch cost is covered. Power cost (researchPower) is
ignored, same as the reference (assumes power stockpiled).

Usage:
  python3 research_time.py R-Defense-Super-Mortar
  python3 research_time.py MortarSuper --preset 2 --labs 5
  python3 research_time.py R-Wpn-RailGun02 --preset 0

Presets: 0 No Bases, 1 T1 with Bases, 2 T1 with Advanced Bases (default),
         3 T2, 4 T3. Preset techs come pre-researched (zero cost).
--labs N multiplies the per-second rate (reference uses 1 lab).
"""

import argparse
import json
import math
import re
import sys
import time
import urllib.request
from pathlib import Path

WZ_RAW = "https://raw.githubusercontent.com/Warzone2100/warzone2100"
REF = "master"
CACHE_DIR = "/tmp/opencode/wz-check-cache"

BASE_STARTING = [
    "R-Sys-Spade1Mk1",
    "R-Vehicle-Body01",
    "R-Vehicle-Prop-Wheels",
]

UPGRADE_TECH_IDS = [
    None,
    "R-Struc-Research-Module",
    "R-Struc-Research-Upgrade01",
    "R-Struc-Research-Upgrade02",
    "R-Struc-Research-Upgrade03",
    "R-Struc-Research-Upgrade04",
    "R-Struc-Research-Upgrade05",
    "R-Struc-Research-Upgrade06",
    "R-Struc-Research-Upgrade07",
    "R-Struc-Research-Upgrade08",
    "R-Struc-Research-Upgrade09",
]

PRESETS = [
    {"name": "No Bases", "offset": 0},
    {"name": "T1 with Bases", "offset": 3 * 60},
    {"name": "T1 with Advanced Bases", "offset": int(6.4 * 60)},
    {"name": "T2", "offset": 17 * 60},
    {"name": "T3", "offset": 26 * 60},
]

MOD_RESEARCH = Path("diffs/MoreFort/stats/research.json")
MOD_STRUCTURE = Path("diffs/MoreFort/stats/structure.json")
MOD_WEAPONS = Path("diffs/MoreFort/stats/weapons.json")


def cache_path(key):
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", key)
    return Path(CACHE_DIR) / (safe + ".json")


def fetch_json(url, key, ttl_days=7):
    p = cache_path(key)
    try:
        if p.exists() and time.time() - p.stat().st_mtime < ttl_days * 86400:
            return json.loads(p.read_text())
    except (OSError, ValueError):
        pass
    req = urllib.request.Request(url, headers={"User-Agent": "morefort-mrt"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8"))
    try:
        Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data))
    except OSError:
        pass
    return data


def fmt(s):
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{h}:{m:02}:{sec:02}" if h else f"{m}:{sec:02}"


def zero_out(rq, tech, seen=None):
    seen = seen if seen is not None else set()
    if tech in seen or tech not in rq:
        return
    seen.add(tech)
    rq[tech]["researchPoints"] = 0
    reqs = rq[tech].get("requiredResearch")
    if isinstance(reqs, list):
        for child in reqs:
            zero_out(rq, child, seen)


def main():
    ap = argparse.ArgumentParser(description="Minimum research time (mrt-calibrated).")
    ap.add_argument("target", help="research / structure / weapon ID")
    ap.add_argument("--preset", type=int, default=2,
                    help="0 No Bases, 1 T1 Bases, 2 T1 Adv Bases, 3 T2, 4 T3")
    ap.add_argument("--labs", type=int, default=1,
                    help="research labs working (rate multiplier, ref uses 1)")
    ap.add_argument("--chain", action="store_true",
                    help="print the critical prerequisite chain")
    args = ap.parse_args()

    if not 0 <= args.preset <= 4:
        sys.exit("preset must be 0-4")
    if args.labs < 1:
        sys.exit("labs must be >= 1")

    base_rq = fetch_json(f"{WZ_RAW}/{REF}/data/mp/stats/research.json",
                         f"raw-{REF}-research")
    base_st = fetch_json(f"{WZ_RAW}/{REF}/data/base/stats/structure.json",
                         f"raw-{REF}-bstructure")
    base_wp = fetch_json(f"{WZ_RAW}/{REF}/data/mp/stats/weapons.json",
                         f"raw-{REF}-weapons")

    # Merge mod diffs over base (mod file holds new full objects only).
    research = dict(base_rq)
    if MOD_RESEARCH.exists():
        research.update(json.loads(MOD_RESEARCH.read_text()))
    structures = dict(base_st)
    if MOD_STRUCTURE.exists():
        structures.update(json.loads(MOD_STRUCTURE.read_text()))
    weapons = dict(base_wp)
    if MOD_WEAPONS.exists():
        weapons.update(json.loads(MOD_WEAPONS.read_text()))

    # ---- rates (single fully-moduled lab; --labs scales it) ----
    fac = base_st.get("A0ResearchFacility", {})
    base_rp = fac.get("researchPoints", 14)
    module_rp = fac.get("moduleResearchPoints", 7)
    max_rates, prev = [], base_rp
    for tid in UPGRADE_TECH_IDS:
        if tid is None:
            rate, top = base_rp, base_rp
        elif tid == "R-Struc-Research-Module":
            rate, top = base_rp, base_rp + module_rp
        else:
            pct = research[tid]["results"][0]["value"] / 100
            rate = prev + math.ceil(base_rp * pct)
            top = rate + module_rp
        max_rates.append(top * args.labs)
        prev = rate

    # ---- preset starting set (computed on clean BASE data, like ref) ----
    memo = {}

    def branch_on(rq, tech):
        if tech in memo:
            return memo[tech]
        if tech is None or tech not in rq:
            memo[tech] = 0
            return 0
        rp = rq.get(tech, {}).get("researchPoints", 0) or 0
        reqs = rq.get(tech, {}).get("requiredResearch")
        if not isinstance(reqs, list):
            memo[tech] = rp
            return rp
        memo[tech] = rp + max((branch_on(rq, c) for c in reqs), default=0)
        return memo[tech]

    clean = {k: dict(v) for k, v in base_rq.items()}
    stack, seen = list(BASE_STARTING), set()
    while stack:
        cur = stack.pop()
        if cur in seen or cur not in clean:
            continue
        seen.add(cur)
        d = dict(clean[cur])
        d["researchPoints"] = 0
        clean[cur] = d
        reqs = base_rq.get(cur, {}).get("requiredResearch")
        if isinstance(reqs, list):
            stack.extend(reqs)

    memo.clear()
    clean_secs = {}
    # clean branch needs its own memo over `clean`
    clean_memo = {}

    def clean_branch(tech):
        if tech in clean_memo:
            return clean_memo[tech]
        if tech is None or tech not in clean:
            clean_memo[tech] = 0
            return 0
        rp = clean.get(tech, {}).get("researchPoints", 0) or 0
        reqs = clean.get(tech, {}).get("requiredResearch")
        if not isinstance(reqs, list):
            clean_memo[tech] = rp
            return rp
        clean_memo[tech] = rp + max((clean_branch(c) for c in reqs), default=0)
        return clean_memo[tech]

    clean_infl = [clean_branch(t) for t in UPGRADE_TECH_IDS]

    def rate_sim(points, inflections, start_lvl, rates):
        if points <= 0:
            return 0
        lvl, rate, done, secs = start_lvl, rates[start_lvl], 0, 0
        while done < points:
            if lvl < 10 and done > inflections[lvl + 1]:
                lvl += 1
                rate = rates[lvl]
            done += rate
            secs += 1
        return secs

    for tid in base_rq:
        clean_secs[tid] = rate_sim(clean_branch(tid), clean_infl, 0, max_rates)

    offset = PRESETS[args.preset]["offset"]
    starting = set(BASE_STARTING)
    for tid, s in clean_secs.items():
        if 0 < s <= offset:
            starting.add(tid)

    # ---- resolve target to research topic(s) ----
    topics = []
    if args.target in research:
        topics = [args.target]
    elif args.target in structures:
        topics = [k for k, v in research.items()
                  if args.target in (v.get("resultStructures") or [])]
        if not topics:
            sys.exit(f"{args.target}: structure has no unlocking research")
    elif args.target in weapons:
        direct = [k for k, v in research.items()
                  if args.target in (v.get("resultComponents") or [])
                  or v.get("statID") == args.target]
        users = [sk for sk, sv in structures.items()
                 if args.target in (sv.get("weapons") or [])]
        via_struct = [k for k, v in research.items()
                      for u in users if u in (v.get("resultStructures") or [])]
        topics = direct + [t for t in via_struct if t not in direct]
        if not topics:
            sys.exit(f"{args.target}: no research unlocks this weapon")
    else:
        sys.exit(f"{args.target}: unknown research/structure/weapon ID")

    # ---- compute on merged data with zeroed starting set ----
    merged = {k: dict(v) for k, v in research.items()}
    stack, seen = list(starting), set()
    while stack:
        cur = stack.pop()
        if cur in seen or cur not in merged:
            continue
        seen.add(cur)
        d = dict(merged[cur])
        d["researchPoints"] = 0
        merged[cur] = d
        reqs = research.get(cur, {}).get("requiredResearch")
        if isinstance(reqs, list):
            stack.extend(reqs)

    memo.clear()
    infl = [branch_on(merged, t) for t in UPGRADE_TECH_IDS]
    start_lvl = 0
    for i in range(len(UPGRADE_TECH_IDS) - 1, -1, -1):
        if UPGRADE_TECH_IDS[i] in starting:
            start_lvl = i
            break

    for topic in topics:
        pts = branch_on(merged, topic)
        secs = rate_sim(pts, infl, start_lvl, max_rates)
        name = research[topic].get("name", topic)
        print(f"{name} ({topic})")
        print(f"  preset : {PRESETS[args.preset]['name']}, labs: {args.labs}")
        print(f"  points : {pts} (critical path), start lab level: {start_lvl}")
        print(f"  minimum: {secs}s = {fmt(secs)}")
        if args.chain:
            chain, cur = [], topic
            while cur and cur in merged:
                chain.append(cur)
                reqs = merged.get(cur, {}).get("requiredResearch")
                if not isinstance(reqs, list) or not reqs:
                    break
                # the zeroed merged dict loses original costs; use research
                cur = max(reqs, key=lambda c: branch_on(merged, c))
                if branch_on(merged, cur) == 0 and \
                        research.get(cur, {}).get("researchPoints", 0) == 0:
                    break
            print("  chain  :")
            for c in chain:
                rp = research.get(c, {}).get("researchPoints", 0)
                nm = research.get(c, {}).get("name", c)
                mark = " (pre-researched)" if c in starting else ""
                print(f"    {rp:>7}  {nm} [{c}]{mark}")


if __name__ == "__main__":
    main()
