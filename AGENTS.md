# More_Fort — Agent Guide

> REQUIRED: any AI agent working in this folder MUST read this file
> plus `stats-reference.md` before editing, adding, or deleting stats/models.

Warzone 2100 multiplay mod: adds 13 Fortress-class defenses + Large Wall + ATGM emplacement + 1 designable rocket weapon. Data-only, no JS. Every `.pie` on disk must be referenced; orphans get deleted (`check.py` warns).

## Layout

```
More_Fort/
  diffs/MoreFort/stats/weapons.json     new weapons (full objects)
  diffs/MoreFort/stats/structure.json  new structures (full objects)
  diffs/MoreFort/stats/research.json   new research topics (full objects)
  diffs/MoreFort/stats/sensor.json     new sensors (full objects, e.g. fortress sensor)
  diffs/MoreFort/stats/body.json       new droid bodies (e.g. heavy engineering truck)
  diffs/MoreFort/stats/construct.json  new construct components
  diffs/MoreFort/stats/repair.json     new repair components
  diffs/MoreFort/stats/templates.json  premade unit templates
  components/weapons/*.pie  turret/barrel models
  components/bodies/*.pie   scaled body models
  structs/*.pie              building bodies
  effects/*.pie              scaled FX
  check.py                   compliance checker (run it)
  scale_pie.py               uniform PIE scaler (run it)
  research_time.py           minimum research time per ID (mrt-calibrated)
  stats-reference.md         field/enum reference + checklist
  WISHLIST.md                build tracker (update status per item)
  README.md                  player-facing install + content
  Pictures/                  in-game screenshots (deferred to the end)
```

No `stats/` folder. Engine merges `diffs/*/stats/*.json` onto `data/mp/stats/*.json` (`WzConfig jsonMerge`; `null` deletes a base key). Subfolder name under `diffs/` is arbitrary.

## How the 3 stats files connect

`research → structure → weapon → .pie`. Break one link and the entry is dead:

* `research.resultStructures[]` unlocks `structure.id`; `resultComponents[]` unlocks `weapons.id`.
* `structure.weapons[]` must exist in base game + `weapons.json` (max 3).
* `weapons.model/mountModel/*Gfx` → `components/`, `effects/`; `structure.structureModel` → `structs/` or base.
* Research prerequisites (`requiredResearch`) must exist in base or in this mod; cycles fail load.

## Compliance

Authoritative source is the Warzone2100 GitHub repo (`Warzone2100/warzone2100`, ref `master`):

* Stats shape and merge: `data/mp/stats/*.json`, `lib/framework/wzconfig.cpp` (`jsonMerge`).
* Field semantics and enums: `src/stats.cpp` (`loadWeaponStats`), `src/structure.cpp`, `src/research.cpp` (`loadResearch`).
* Asset filenames on disk are lowercase; `.pie`/`.ogg` references must match exactly (Linux break otherwise). Base files on disk are lowercase even where base JSON uses uppercase — always write lowercase.

Rules that have bitten before:

* Time/damage numeric fields must be integers — the engine applies `toUInt()` then multiplies by 100, so floats truncate (`2.5` → `2`).
* `researchPoints` and `researchPower` are capped at `UWORD_MAX` (65535, `uint16` in the engine). Exceeding the cap makes `loadResearch()` fail and the game exits to the main menu (`Failed to parse wrf/multires.wrf` → `Exiting to main menu`).
* `research.msgName` is optional; if present it must be unique, must not collide with base keys, and is only legal on a `techCode: 0` (TC_MAJOR) topic. This mod ships no briefing file, so prefer omitting it.
* `redComponents[]`/`redStructures[]` must never contain `""`.
* Never add, shadow, or delete `ZNULL*` entries.
* Build caps use the stats field `userLimits: [min, mp, max]` (e.g. Repair Facility `[0, 5, 5]`). Campaign scripts can raise them; MP uses the middle value. No JS needed.
* Art convention: scaled pies keep the stock point counts with multiplied coordinates (`-2x`, `-3x`, `-4x`, `-5x` suffixes). Never use `.` in pie names (`-25x` means 2.5x). Unreferenced pies are orphans: delete them, never hoard.
* 3x3 fortress recipe (proven in game): body at 1.5x stock with connector `0 0 195`; weapon meshes at 2x stock with y minus 20 on every mesh point; weapon connectors at pure scaled values snapped to integers (engine rejects mixed int/float connector lines), never shifted. The minus 20 is visual only: it reseats the enlarged mesh on the mount after the connector was raised for line of fire, and it changes no ballistics. Copy this verbatim for every future 3x3 fortress weapon. Do not re-derive it.

## Tools and verification

* `python3 check.py` — full compliance check, always online (verifies base refs against GitHub, cached under `/tmp/opencode/wz-check-cache`). Must report `0 error(s), 0 warning(s)` before commit. Do not use `--offline`; base refs must verify against upstream, not assumed. `--online` is accepted as a legacy no-op flag.
* `python3 scale_pie.py --scale F in.pie out.pie` — uniform XYZ scaler for POINTS and CONNECTORS; leaves POLYGONS UV, TYPE, TEXTURE untouched. Use it for `-4x` art instead of hand-editing. Verify by halving/doubling back against the stock pie bounding box.
* `python3 research_time.py <research|structure|weapon ID> [--preset 0-4] [--labs N] [--chain]` — minimum research time, rate model calibrated against https://aco4.github.io/wz/mrt/ (single moduled lab, upgrades applied at inflection, power ignored). Spot checks on preset 2: Mortar Pit 0:24, HEAP Mk3 16:01, Rail Gun 37:35.
* Chain check per item: `research.resultStructures[]` → `structure.id`, `structure.weapons[]` → `weapons.id`, `weapons.model/mountModel/*Gfx` → files on disk (lowercase, exact match). Break one link and the entry is dead in game.
* Orphan check: every mod `.pie` must be referenced from stats (`model`/`mountModel`/`*Gfx`/`structureModel`/`sensorModel`); `check.py` warns on orphans.
* Docs sync per item: `WISHLIST.md` holds only UNIMPLEMENTED features (Todo). Remove a row once the item is implemented and fully tested — Done/Balanced items live only in `README.md`, never in `WISHLIST.md`. `README.md` section with research prerequisites and behavior. `Pictures/` screenshots are deferred to the end; mark `Done (pic pending)` meanwhile.
* README block template (one per structure, ordered by ascending MRT; keep rows in this order, omit N/A rows):
  `Name:` / blank / `![Name](Pictures/FILE.png)` / blank / `- List of Required Researches:` (`  - Name (\`ID\`)` per line) / `- MRT: m:ss` (from `research_time.py`, clean No Bases start, 1 lab) / `- Build Power:` / `- Build Points:` / `- Weapon:` (`- Weapon: none (...)` if unarmed) / `- Name:` / `- Range: A-B tiles` / `- ROF:` (`X/min`, continuous counts as 600/min) / `- Damage:` (`N (DPS/s)`, DPS = damage x ROF / 60, 1 decimal) / `- Damage Type:` / `- Salvo:` (`X Rounds`, burst weapons only) / `- Salvo Damage:` (damage × X) / `- Damage Mod:` / `- Splash:` (`no` or `N tiles`) / `- Radius Damage:` (`No` or `N damage / M Tiles`) / `- Burn:` (`no` or `N tiles for S seconds`) / `- Burn Damage:` (`No` or `N damage`) / optional `- Limit:` / `- Note:` lines.

## Install / Edit

* Drop folder (or `.wz`) into `mods/<version>/multiplay`.
* Add: full object under new key + `.pie` as needed. Patch base with partial object. Delete base key with `null`.
* Validate: `python3 check.py` must report 0 errors.
