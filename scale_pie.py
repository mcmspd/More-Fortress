#!/usr/bin/env python3
"""Scale Warzone 2100 .pie model coordinates by a uniform factor.

Usage: python3 scale_pie.py --scale 2.0 in.pie out.pie
Scales POINTS and CONNECTORS XYZ. Leaves POLYGONS (mesh indices
plus UV), TYPE, TEXTURE, LEVELS untouched.
"""

import argparse
from pathlib import Path


def fmt(v):
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    s = repr(v)
    if "." in s and "e" not in s:
        s = s.rstrip("0").rstrip(".")
    return s.replace("-0", "0") if s == "-0" else s


def scale_text(text, factor):
    lines = text.splitlines()
    out = []
    i = 0
    in_connectors = False
    while i < len(lines):
        line = lines[i]
        out.append(line)
        parts = line.split()
        if len(parts) == 2 and parts[0] in ("POINTS", "CONNECTORS"):
            in_connectors = parts[0] == "CONNECTORS"
            try:
                n = int(parts[1])
            except ValueError:
                in_connectors = False
                i += 1
                continue
            for _ in range(n):
                i += 1
                nums = lines[i].split()
                if len(nums) == 3:
                    try:
                        vals = [float(x) * factor for x in nums]
                    except ValueError:
                        out.append(lines[i])
                        continue
                    if in_connectors:
                        # engine connector parser rejects mixed int/float
                        # lines, so connectors snap to integers
                        out.append(" ".join(str(int(round(v))) for v in vals))
                    else:
                        out.append(" ".join(fmt(v) for v in vals))
                else:
                    out.append(lines[i])
        i += 1
    end = "\n" if text.endswith("\n") else ""
    return "\n".join(out) + end


def main(argv=None):
    p = argparse.ArgumentParser(description="Uniform-scale .pie coordinates")
    p.add_argument("input", help="source .pie file")
    p.add_argument("output", help="scaled .pie output path")
    p.add_argument("--scale", type=float, required=True,
                   help="uniform XYZ factor, e.g. 2.0")
    args = p.parse_args(argv)
    text = Path(args.input).read_text()
    Path(args.output).write_text(scale_text(text, args.scale))


if __name__ == "__main__":
    main()
