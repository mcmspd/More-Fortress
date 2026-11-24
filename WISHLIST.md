# More_Fort Wishlist

Planned content for the Warzone 2100 multiplay mod.

| # | Item | Status | Files affected | BEHAVIOUR |
|---|------|--------|----------------|-----------|
| 1 | **M1299 Howitzer Fortress** | ✅ Done | `diffs/MoreFort/stats/weapons.json` (`HowitzerSuper`), `diffs/MoreFort/stats/structure.json` (`X-Super-Howitzer`), `diffs/MoreFort/stats/research.json` (`R-Defense-Super-Howitzer`), `README.md` | Indirect artillery, 3 RPM, 1400 direct + 1400 splash over a 4-tile blast, 65/50% accuracy, 2.5 s ground scorch, recoil 500, heavy 120000-weight turret, 1800 build power, requires HEAP Shells + Plascrete Mk2 |
| 2 | **Super RIM-116 AA Fortress** | ✅ Done | `diffs/MoreFort/stats/weapons.json` (`RIM116Super`), `diffs/MoreFort/stats/structure.json` (`X-Super-RIM116`), `diffs/MoreFort/stats/research.json` (`R-Defense-Super-RIM116`), `components/weapons/rim-116.pie`, `README.md` | Air-only 60-round CIWS interceptor: 60 × 450 damage in a 6 s salvo, 27,000 burst damage, 60 s reload, 32-tile range, requires Avenger SAM + Plascrete Mk2 + missile accuracy/ROF + Sensor Mk3 |
| 3 | **ATGM** | ✅ Done | `diffs/MoreFort/stats/weapons.json` (`Rocket-ATGM`), `diffs/MoreFort/stats/research.json` (`R-Wpn-Rocket-ATGM`), `README.md` | 4 blue missiles per 20 s reload at 105 damage each, 5–30 tile range |
| 4 | **3X3 Super Rail Gun Fortress** | ⬜ Todo | `diffs/MoreFort/stats/` | 3x3 penetrate fortress, 1500 dmg single shot, 20 tiles, DIRECT GAUSS, requires R-Wpn-RailGun03 + Wall09, better than MassDriver |
| 5 | **3X3 Super ATGM-ER Fortress** | ⬜ Todo | `diffs/MoreFort/stats/` | 3x3 ATGM-ER, 4400 dmg x9 salvo, 45 tiles, HOMING-INDIRECT MISSILE, 60 s reload, 5-tile dead zone, 4x Missile Fortress |
| 6 | **Repair Fortress** | ⬜ Todo | `diffs/MoreFort/stats/` | 2x2 REPAIR FACILITY with repairPoints, FortressSensor, no weapon, combinesWithWall |
| 7 | **Mortar Fortress** | ✅ Done | `diffs/MoreFort/stats/` | 2x2 entrance mortar, 165 dmg + 100 splash, 20 tiles, 640 splash (5 tiles), 50 long / 40 short accuracy, 5-tile dead zone, same reload as Mortar, requires HEAP Mortar Shells, optional Acc04 radar upgrade for another 10% |
| 8 | **EMP Howitzer Fortress** | ⬜ Todo | `diffs/MoreFort/stats/` | 2x2 EMP mortar, 40 dmg, 50 tiles, 512 splash (4 tiles) |
| 9 | **Incendiary Howitzer Fortress** | ⬜ Todo | `diffs/MoreFort/stats/` | 2x2 incendiary, 500 direct + 500 burn, 640 radius (5 tiles), 30 s reload, lower direct than M1299 |
| 10 | **Wide-Spectrum Sensor Fortress** | ✅ Done | `diffs/MoreFort/stats/` | 2x2 unarmed sensor, 1.5x wide-spec sight (3390 range), 3x wide-spec mast, limit 3 per player via `userLimits`, high cost, requires WideSpec sensor + tower + Supercrete Mk2, same HP as Cannon Fortress (3200) |
| 11 | **Large Rocket Pod Fortress** | ✅ Done | `diffs/MoreFort/stats/`, `components/weapons/big-mrp.pie`, `README.md`, `Pictures/LRP_FORT.png` | 2x2 fortress with MRP-Super, cost/stats modeled on Flamer/Assault Gun Fortresses, requires HE Rockets Mk3 |
| 12 | **Nexus Link Fortress** | ✅ Done | `diffs/MoreFort/stats/`, `README.md` | 2x2 Nexus tower, 2.5x turret, 3x beam, 20 dmg (10x), 2240 range (1.25x), 4000 BP / 5000 PW, limit 2 via `userLimits`, requires SpyTurret + WallUpgrade05, 15000 RP / 5000 PW |
| 13 | **Plasma Cannon Fortress** | ✅ Done | `diffs/MoreFort/stats/`, `README.md` | 2x2 plasma, 2500 dmg (5x) + 2500 splash, 15 tiles, 5-tile dead zone, 1.25x reload, 2.5x turret, 3x shell, 5 s burn, requires Plasmite Flamer + Plasma Cannon + WallUpgrade05 |
| 14 | **Plasmite Rail Accelerator Fortress** | ⬜ Todo | `diffs/MoreFort/stats/`, `README.md` | 2x2 rail, 300 direct + 300 burn, penetrate, plasmite projectile, 20 tiles |
| 15 | **Particle Gun Fortress** | ⬜ Todo | `diffs/MoreFort/stats/`, `README.md` | 2x2 particle gun fortress |
| 16 | **3x3 Cannon Fortress (concept test)** | ✅ Done | `diffs/MoreFort/stats/` | 3x3 test: 1.5x body, 2x gun, 760 dmg (2x), 640 splash (5 tiles), 3 s burn, 2816 range (2x), ROF 1.25x (pause 48), 6400 HP + 30 armour (2x), muzzle node 195 with meshes at -20 y, 3x shell at 0.75x speed, requires Plascrete Mk2 + HVAPFSDS Mk2 + Autoloader Mk3 |
| 17 | **Large Wall** | ✅ Done | `diffs/MoreFort/stats/` | 2x2 WALL block on fortress body, 2800 HP (4x hardcrete), no weapon, no sensor, requires Supercrete Mk2 |
| 18 | **Large Sunburst Array Fortress** | ✅ Done | `diffs/MoreFort/stats/`, `README.md` | 2x2 air-only fortress, 110 dmg (stock), 36 rounds per salvo (6x), 17-tile range (+5), 3x turret, stock rockets at 2x speed, requires Sunburst AA + WallUpgrade05 |
