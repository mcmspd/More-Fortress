**Warzone 2100 Mod: More Fortress**

Adds 13 new Fortress defenses, 1 large wall, 1 ATGM emplacement, and 1 new tank weapon to skirmish and multiplayer.

## Installation

1. Copy this folder (or its `.wz` pack) into your Warzone 2100 mods folder:
   `mods/<version>/multiplay`
2. Enable the mod when hosting a multiplay or skirmish game.

## New structures

All fortresses join onto walls and come with their own gun. Most are 2x2;
the 3x3 Cannon Fortress is the exception. The Large Wall is a gunless 2x2 block.

MRT = Minimum Research Time from `research_time.py` (clean No Bases start,
1 fully-moduled lab, power cost ignored). Blocks below ordered by ascending MRT.

Large Rocket Pod Fortress:

![Large Rocket Pod Fortress](Pictures/LRP_FORT.png)

- List of Required Researches:
  - Mini-Rocket Pod (`R-Wpn-Rocket05-MiniPod`)
  - Improved Hardcrete Mk3 (`R-Defense-WallUpgrade03`)
  - HE Rockets Mk3 (`R-Wpn-Rocket-Damage03`)
- MRT: 11:23
- Build Power: 750
- Build Points: 650
- Weapon:
- Name: Large-Rocket-Pod
- Range: 5-10 tiles
- ROF: 171/min
- Damage: 40 (114/s)
- Damage Type: Kinetic
- Damage Mod: Anti-Tank
- Splash: no
- Radius Damage: No
- Burn: no
- Burn Damage: No

ATGM Emplacement:

![ATGM Emplacement](Pictures/ATGM_Emplacement.png)

- List of Required Researches:
  - Anti-Tank Guided Missile Launcher (`R-Wpn-Rocket-ATGM`)
- MRT: 13:22
- Build Power: 250
- Build Points: 400
- Weapon:
- Name: ATGM
- Range: 4-30 tiles
- ROF: 11/min
- Damage: 105 (19.2/s)
- Damage Type: Kinetic
- Damage Mod: Anti-Tank
- Splash: no
- Radius Damage: No
- Burn: no
- Burn Damage: No

Flamer Fortress:

![Flamer Fortress](Pictures/FLAM_FORT.png)

- List of Required Researches:
  - Heavy Flamer - Inferno (`R-Wpn-Flame2`)
  - Improved Hardcrete Mk3 (`R-Defense-WallUpgrade03`)
- MRT: 15:14
- Build Power: 750
- Build Points: 650
- Weapon:
- Name: FlamerFortress
- Range: 4-10 tiles
- ROF: 40/min
- Damage: 55 (36.7/s)
- Damage Type: Heat
- Damage Mod: Flamer
- Splash: 2 tiles
- Radius Damage: 40 damage / 2 Tiles
- Burn: 2 tiles for 5 seconds
- Burn Damage: 20 damage

Assault Gun Fortress:

![Assault Gun Fortress](Pictures/AG_FORT.png)

- List of Required Researches:
  - Assault Gun (`R-Wpn-MG4`)
  - Improved Hardcrete Mk3 (`R-Defense-WallUpgrade03`)
- MRT: 16:04
- Build Power: 750
- Build Points: 650
- Weapon:
- Name: Assault Gun Fortress
- Range: 8-11 tiles
- ROF: 600/min
- Damage: 35 (350/s)
- Damage Type: Kinetic
- Damage Mod: Anti-Personnel
- Splash: no
- Radius Damage: No
- Burn: no
- Burn Damage: No

Large Wall:

![Large Wall](Pictures/L_Wall.png)

- List of Required Researches:
  - Supercrete Mk2 (`R-Defense-WallUpgrade05`)
- MRT: 19:33
- Build Power: 100
- Build Points: 500
- Weapon: none (gunless wall block)

Mortar Fortress:

![Mortar Fortress](Pictures/Mort_FORT.png)

- List of Required Researches:
  - Supercrete Mk2 (`R-Defense-WallUpgrade05`)
  - HEAP Mortar Shells (`R-Wpn-Mortar-Damage04`)
  - Target Acquisition Mortar Shells (`R-Wpn-Mortar-Acc03`)
- MRT: 20:09
- Build Power: 1000
- Build Points: 650
- Weapon:
- Name: Mortar Fortress
- Range: 11-22 tiles
- ROF: 20/min
- Damage: 200 (66.7/s)
- Damage Type: Kinetic
- Damage Mod: Artillery Round
- Splash: 4 tiles
- Radius Damage: 100 damage / 4 Tiles
- Burn: no
- Burn Damage: No
- Note: Radar-Assisted Mortar Targeting (`R-Wpn-Mortar-Acc04`) adds another 10% accuracy after Target Acquisition shells

Large Sunburst Array Fortress:

- List of Required Researches:
  - Sunburst AA Rocket Array (`R-Wpn-Sunburst`)
  - Supercrete Mk2 (`R-Defense-WallUpgrade05`)
- MRT: 21:14
- Build Power: 1000
- Build Points: 1750
- Weapon:
- Name: Large Sunburst Array
- Range: 11-20 tiles
- ROF: 171/min
- Damage: 138 (393.3/s)
- Damage Type: Kinetic
- Damage Mod: Anti-Tank
- Splash: 1.5 tiles
- Radius Damage: 50 damage / 1.5 Tiles
- Burn: no
- Burn Damage: No
- Note: triple-size turret, stock rockets at double speed



AA Flak Fortress:

![AA Flak Fortress](Pictures/AA_FLAK_FORT.png)

- List of Required Researches:
  - AA Tornado Flak Cannon (`R-Wpn-AAGun02`)
  - Supercrete Mk2 (`R-Defense-WallUpgrade05`)
- MRT: 25:36
- Build Power: 750
- Build Points: 1500
- Weapon:
- Name: AA Flak Fortress
- Range: 11-20 tiles
- ROF: 43/min
- Damage: 250 (179.2/s)
- Damage Type: Kinetic
- Damage Mod: Anti-Tank
- Splash: 5 tiles
- Radius Damage: 180 damage / 5 Tiles
- Burn: no
- Burn Damage: No

Plasma Cannon Fortress:

![Plasma Cannon Fortress](Pictures/PC_FORT.png)

- List of Required Researches:
  - Cannon Fortress (`R-Defense-Super-Cannon`)
  - Plasmite Flamer (`R-Wpn-Plasmite-Flamer`)
  - Superhot Plasmite Gel Mk2 (`R-Wpn-Flamer-Damage08`)
  - Plasma Cannon (`R-Wpn-PlasmaCannon`)
  - Supercrete Mk2 (`R-Defense-WallUpgrade05`)
- MRT: 33:08
- Build Power: 1750
- Build Points: 2500
- Weapon:
- Name: Plasma Cannon Fortress
- Range: 10-15 tiles
- ROF: 4.8/min
- Damage: 500 (40/s)
- Damage Type: Heat
- Damage Mod: All-Rounder
- Splash: 5 tiles
- Radius Damage: 500 damage / 5 Tiles
- Burn: 5 tiles for 5 seconds
- Burn Damage: 25 damage

Laser Fortress:

![Laser Fortress](Pictures/LAS_FORT.png)

- List of Required Researches:
  - Pulse Laser (`R-Wpn-Laser02`)
  - Supercrete Mk2 (`R-Defense-WallUpgrade05`)
- MRT: 35:03
- Build Power: 1250
- Build Points: 2000
- Weapon:
- Name: Laser Fortress
- Range: 11.7-24 tiles
- ROF: 112/min
- Damage: 380 (709.3/s)
- Damage Type: Heat
- Damage Mod: Anti-Personnel
- Splash: no
- Radius Damage: No
- Burn: no
- Burn Damage: No

3x3 Cannon Fortress (concept test):

![3x3 Cannon Fortress](Pictures/3x3Can_FORT.png)

- List of Required Researches:
  - Plascrete Mk2 (`R-Defense-WallUpgrade08`)
  - HVAPFSDS Cannon Rounds Mk2 (`R-Wpn-Cannon-Damage08`)
  - Cannon Autoloader Mk3 (`R-Wpn-Cannon-ROF03`)
- MRT: 35:39
- Build Power: 5000
- Build Points: 4000
- Weapon:
- Name: 3x3 Cannon Fortress
- Range: 2-22 tiles
- ROF: 12.5/min
- Damage: 750 (156.2/s)
- Damage Type: Kinetic
- Damage Mod: All-Rounder
- Splash: 5 tiles
- Radius Damage: 520 damage / 5 Tiles
- Burn: 5 tiles for 3 seconds
- Burn Damage: 1 damage

Wide-Spectrum Sensor Fortress:

![Wide-Spectrum Sensor Fortress](Pictures/WideSpec_FORT.png)

- List of Required Researches:
  - Wide Spectrum Sensor (`R-Sys-Sensor-WS`)
  - Wide Spectrum Sensor Tower (`R-Sys-Sensor-WSTower`)
  - Plascrete Mk2 (`R-Defense-WallUpgrade08`)
- MRT: 36:09
- Build Power: 2000
- Build Points: 4000
- Weapon: none (unarmed sensor, limited to 3 per player)

M1299 Howitzer Fortress:

![M1299 Howitzer Fortress](Pictures/H_FORT.png)

- List of Required Researches:
  - HEAP Howitzer Shells (`R-Wpn-Howitzer-Damage04`)
  - Plascrete Mk2 (`R-Defense-WallUpgrade08`)
- MRT: 36:40
- Build Power: 1800
- Build Points: 2000
- Weapon:
- Name: M1299 Howitzer
- Range: 30-80 tiles
- ROF: 2.4/min
- Damage: 1400 (56/s)
- Damage Type: Kinetic
- Damage Mod: Artillery Round
- Splash: 4 tiles
- Radius Damage: 1400 damage / 4 Tiles
- Burn: 4 tiles for 2.5 seconds
- Burn Damage: 1 damage

Nexus Link Fortress:

![Nexus Link Fortress](Pictures/NLINK_FORT.png)

- List of Required Researches:
  - Nexus Link Turret (`R-Sys-SpyTurret`)
  - Plascrete Mk2 (`R-Defense-WallUpgrade08`)
- MRT: 36:55
- Build Power: 5000
- Build Points: 4000
- Weapon:
- Name: Nexus Link Fortress
- Range: 17.5 tiles
- ROF: 600/min
- Damage: 20 (200/s)
- Damage Type: Heat
- Damage Mod: Anti-Personnel
- Splash: no
- Radius Damage: No
- Burn: no
- Burn Damage: No
- Limit: 2 per player (`userLimits`)

Super RIM-116 AA Fortress:

![Super RIM-116 AA Fortress](Pictures/RIM116_FORT.png)

- List of Required Researches:
  - Avenger SAM (`R-Wpn-Missile-LtSAM`)
  - Supercrete Mk2 (`R-Defense-WallUpgrade05`)
  - Target Prediction Missiles (`R-Wpn-Missile-Accuracy01`)
  - Advanced Missile Allocation System (`R-Wpn-Missile-ROF01`)
  - Sensor Upgrade Mk3 (`R-Sys-Sensor-Upgrade03`)
- MRT: 39:14
- Build Power: 1750
- Build Points: 2000
- Weapon:
- Name: RIM-116 AA Missile
- Range: 5-32 tiles
- ROF: 37.5/min
- Damage: 550 (343.8/s)
- Damage Type: Kinetic
- Damage Mod: Anti-Tank
- Splash: 0.5 tiles
- Radius Damage: 100 damage / 0.5 Tiles
- Burn: no## Research upgrades
- Burn Damage: No

Ultra-High Performance Concrete, Carbon-Fibre Reinforced Concrete and
Self-Healing Nano-Concrete:
- Three final wall upgrades, researched in order after "Plasteel Mk3"
  (`R-Defense-WallUpgrade12`), each adding 100% hit points to every wall,
  bunker and fortress on top of the twelve base wall tiers
- Together they add 300%, turning a Laser or RIM-116 Fortress from 3200
  hit points into 24320, and the M1299 Howitzer Fortress from 4000 into
  30400
- Brutally expensive: 65535 research points and 4500 research power each,
  the most expensive research in the game, for 196605 research points and
  13500 research power to get all three
- They add hit points only, so armour still comes from the Plasteel tiers

## New weapon

Anti-Tank Guided Missile Launcher:
- A designable turret for your own tank designs
- List of Required Researches:
  - Lancer AT Rocket (`R-Wpn-Rocket01-LtAT`)
- Build Power: 250
- Build Points: 1500
- Weapon:
- Name: ATGM
- Range: 4-30 tiles
- ROF: 11/min
- Damage: 105 (19.2/s)
- Damage Type: Kinetic
- Damage Mod: Anti-Tank
- Splash: no
- Radius Damage: No
- Burn: no
- Burn Damage: No
- MRT: 12:34
