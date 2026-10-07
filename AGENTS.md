# More_Fort — Agent Guide

> REQUIRED: any AI agent working in this folder MUST read this file
> plus `stats-reference.md` before editing, adding, or deleting stats/models.

Warzone 2100 multiplay mod: adds 4 Fortress-class defenses + 1 designable rocket weapon. Data-only, no JS. All `.pie` files are kept intentionally, even if unreferenced.

## How the 3 stats files connect

`research → structure → weapon → .pie`. Break one link and the entry is dead:

* `research.resultStructures[]` unlocks `structure.id`; `resultComponents[]` unlocks `weapons.id`.
* `structure.weapons[]` must exist in base game + `weapons.json`.
* `weapons.model/mountModel/*Gfx` → `components/`, `effects/`; `structure.structureModel` → `structs/` or base.

Current mapping (verified, no orphans):

* `R-Defense-Super-AG` → `X-Super-AG` → `AGFort`
* `R-Defense-Super-Laser` → `X-Super-Laser` → `LaserSuper`
* `R-Defense-Super-AA` → `X-Super-AA` → `AAGunSuper`
* `R-Defense-Super-Flame` → `X-Super-Flame` → `FlameSuper`
* `R-Wpn-Rocket-ATGM` → `Rocket-ATGM` (designable tank weapon, no structure)

## Layout

```
More_Fort/
  diffs/MoreFort/stats/weapons.json     5 keys, full objects
  diffs/MoreFort/stats/structure.json  4 keys, full objects
  diffs/MoreFort/stats/research.json   5 keys, full objects
  components/weapons/*.pie  13 files (some now unused, kept)
  structs/*.pie              3 files (2 now unused, kept)
  effects/*.pie              9 files (some now unused, kept)
  texpages/page-12-player-buildings.png
```

No `stats/` folder. Engine merges `diffs/*/stats/*.json` onto `data/mp/stats/*.json` (`WzConfig jsonMerge`; `null` deletes). Subfolder name under `diffs/` is arbitrary.

## Content

### Structures — all `FORTRESS`, `combinesWithWall:true`, `FortressSensor`

* `X-Super-AG` 1600HP armour 8, 2x2, 1000/500
* `X-Super-Laser` 3200HP armour 15, 2x2, 2000/1000
* `X-Super-AA` 2800HP armour 15, 2x2
* `X-Super-Flame` 1600HP armour 8, 2x2

### Weapons

* `AGFort` 35dmg, 0.5 pause, 1024-1408, `ShootAir`
* `LaserSuper` 350dmg, 15rds/reload 50, 1500-2304, 100% hit
* `AAGunSuper` 250dmg, `AirOnly`, 1408-2560
* `FlameSuper` 55dmg + periodic 20, 512-1280
* `Rocket-ATGM` 60dmg, `designable:1`, 512-3840

### Research

* `R-Defense-Super-AG`: `MG4 + Wall03`, 4800/200
* `R-Defense-Super-Laser`: `Laser02 + Wall05`, 12000/400
* `R-Defense-Super-AA`: `AAGun02 + Wall05`, 8400/262
* `R-Defense-Super-Flame`: `Flame2 + Wall03`, 4800/200
* `R-Wpn-Rocket-ATGM`: `Rocket01-LtAT`, 4000/200

### Removed (per user)

* Unresearchable: `X-Super-HC-HC-CF`, `X-Super-Rocket-Dual`, `Cannon375mmMk2`.
* All mortars: `Emplacement-MortarPit03`, `Mortar1Mk2`, `Mortar2Mk1`/`Mortar3ROTARYMk1` patches, `R-Defense-Large-MortarPit`.

## Install / Edit

* Drop folder (or `.wz`) into `mods/<version>/multiplay`.
* Add: full object under new key + `.pie` as needed. Patch base with partial object. Delete base key with `null`.
* Validate: JSON parses; `structure.weapons[]` ∈ base+diff; `research.requiredResearch/result*` exist; `.pie` case matches (`las_Body` vs `las_body` is wrong).

## Known issues (do not fix without approval)

1. `LaserSuper.mountModel: las_Body_3x.pie` vs file `las_body_3x.pie` — Linux break.
2. `msgName` reused (`RES_EMP_CAN` x4, `RES_W_RK_LTAT1` collides with base).
3. `R-Wpn-Rocket-ATGM.redComponents: [""]` — should be real ID or omitted.
4. `README.md` documents only AG/Laser.
