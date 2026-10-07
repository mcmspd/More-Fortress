# More_Fort — Agent Guide

Warzone 2100 multiplay mod: adds Fortress-class defenses + 1 mortar pit + 1 designable rocket weapon. Data-only, no JS (`multiplay/`, `SurvivalMod/` absent).

## Layout

```
More_Fort/
  diffs/MoreFort/stats/weapons.json     8 keys (6 full + 2 patches)
  diffs/MoreFort/stats/structure.json  5 keys (full objects)
  diffs/MoreFort/stats/research.json   6 keys (full objects)
  components/weapons/*.pie  13 turret/barrel models
  structs/*.pie              3 building bodies (2 unused, kept intentionally)
  effects/*.pie              9 scaled FX
  texpages/page-12-player-buildings.png
  README.md / agents.md
```

No `stats/` folder. Engine merges `diffs/*/stats/*.json` onto `data/mp/stats/*.json` at load (`WzConfig`, recursive `jsonMerge`; `null` deletes). Subfolder name under `diffs/` is arbitrary.

## Content

### Structures (`structure.json`)

All `FORTRESS` except mortar pit, all `combinesWithWall:true`, `sensorID:FortressSensor` (pit: `DefaultSensor1Mk1`):

* `X-Super-AG` 1600HP armour 8, 2x2, 1000pts/500pow, weapon `AGFort`
* `X-Super-Laser` 3200HP armour 15, 2x2, 2000pts/1000pow, weapon `LaserSuper`
* `X-Super-AA` 2800HP armour 15, 2x2, weapon `AAGunSuper`
* `X-Super-Flame` 1600HP armour 8, 2x2, weapon `FlameSuper`
* `Emplacement-MortarPit03` 1200HP, 2x2 `DEFENSE`, model `BLMRTPIT-2x.PIE`, weapon `Mortar1Mk2`

Removed as unresearchable: `X-Super-HC-HC-CF`, `X-Super-Rocket-Dual` + orphan weapon `Cannon375mmMk2`. `.pie` files for them (`stwpfcan-x3.pie`, `dual_fortress_base.pie`) kept intentionally — harmless.

### Weapons (`weapons.json`)

* `AGFort` dmg 35, pause 0.5, range 1024-1408, `ShootAir`, model `ag_barrel_3x.pie`
* `LaserSuper` dmg 350, 15 rounds / reload 50, range 1500-2304, 100% hit, `las_barrel_3x.pie`
* `AAGunSuper` dmg 250, `AirOnly`, range 1408-2560, `gnhair-3x.pie`
* `FlameSuper` dmg 55 + periodic 20, range 512-1280, `gnmflmr-3x.pie`
* `Mortar1Mk2` dmg 175, `INDIRECT`, range 1152-3072, `gnmmort-2x.pie`
* `Rocket-ATGM` dmg 60, `designable:1`, `INDIRECT`, range 512-3840, `atgm_weapon.pie` — only tank weapon, unlocked via research not structure
* Patches (minimal, forward-compatible): `Mortar2Mk1`, `Mortar3ROTARYMk1`: `{"model":"gnmmort-2x.pie"}` only

### Research (`research.json`)

* `R-Defense-Super-AG`: `R-Wpn-MG4 + Wall03`, 4800/200 → `X-Super-AG`
* `R-Defense-Super-Laser`: `R-Wpn-Laser02 + Wall05`, 12000/400 → `X-Super-Laser`
* `R-Defense-Super-AA`: `R-Wpn-AAGun02 + Wall05`, 8400/262 → `X-Super-AA`
* `R-Defense-Super-Flame`: `R-Wpn-Flame2 + Wall03`, 4800/200 → `X-Super-Flame`
* `R-Defense-Large-MortarPit`: `R-Defense-MortarPit`, 800/36 → `Emplacement-MortarPit03`
* `R-Wpn-Rocket-ATGM`: `R-Wpn-Rocket01-LtAT`, 4000/200 → `Rocket-ATGM`

### Models

* `components/weapons/`: `ag_barrel_3x`, `las_barrel_3x` + `las_body_3x`, `gnhair/trhair-3x`, `gnmflmr/trmflmr-3x`, `gnmmort/trmmort-2x`, `atgm_weapon/mount`. Unused but kept: `gnmmorti-2x.pie`, `mg_body_3x.pie`.
* `structs/`: `blmrtpit-2x.pie` (mortar pit), 2 fortress bases (now unused, kept).
* `effects/`: `-2x/-3x/4x` scaled FX (`fxtracerh-2x`, `fxplammo_4x` for LaserSuper, etc.).
* `texpages/`: only building page override; weapons/FX use base pages.

## Install / Edit

* Drop folder (or pack as `.wz`) into `mods/<version>/multiplay`.
* Edit: add full object under new key in `diffs/MoreFort/stats/*.json`; add `.pie` + texture as needed. Partial objects patch base fields. Use `null` value to delete a base key.
* Validate: `python3 -c "import json; json.load(open('diffs/MoreFort/stats/weapons.json'))"` + cross-check `structure.weapons[]` ∈ base+diff, `research.requiredResearch` ∈ base+diff, `resultStructures/Components` exist.

## Known issues (do not "fix" without approval)

1. `LaserSuper.mountModel: las_Body_3x.pie` vs file `las_body_3x.pie` — case mismatch, breaks Linux.
2. `R-Defense-Large-MortarPit.statID: Emplacement-MortarPit01` ≠ result `...03` (base convention: equal).
3. `msgName` reused (`RES_EMP_CAN` x4, `RES_EMP_Mpit`, `RES_W_RK_LTAT1` collide with base).
4. `R-Wpn-Rocket-ATGM.redComponents: [""]` — empty string, should be real ID or omitted.
5. `README.md` documents only AG/Laser; mod ships AA/Flame/Mortar/ATGM too.
