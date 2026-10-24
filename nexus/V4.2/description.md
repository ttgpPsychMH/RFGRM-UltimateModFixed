# Godlike Campaign Overhaul - Hammer and Backpacks

A campaign overhaul for **Red Faction Guerrilla Re-Mars-tered**, built for offline play. Give Alec much greater durability, hit harder with the hammer, carry more ammunition, and get more use out of all ten backpack profiles.

The aim is a more generous, destructive campaign with less waiting between abilities. Progression conditions and stock NPC loadouts are retained, while selected combat, activity and economy settings are adjusted.

**Release status: configuration-validated, with in-game testing still needed.** The archives have passed structural and data checks. Flight height, measured movement speed, campaign NPC healing and AI reactions have not been verified in game.

## Campaign features

- **Godlike Alec:** health configured at 5,500, a 10 m/s character speed limit, strong damage resistance and faster regeneration. Scripted failures and mission objectives still apply.
- **Powerful hammer attacks:** main player attack branches use ×10 NPC damage, ×20 vehicle damage and ×5 structural damage relative to their original values. Reach and hit radius are increased by 25%; impact and ragdoll impulse by 50%. Upgraded and golden variants scale from their own original values.
- **Stronger firearms:** selected non-explosive handheld weapon damage is ×3. Positive player recoil and normal/fine-aim spread settings are reduced by 20%.
- **More ammunition:** selected carry limits, upgraded carry limits, restock amounts and activity ammunition are ×5. Magazine sizes retain their original settings.
- **Retuned explosives:** selected explosive weapon profiles use ×2 NPC/vehicle blast damage, ×1.5 structural damage and ×1.5 selected effect radii. Thermobaric damage is ×1.5 with its original radii retained.
- **Tougher NPCs:** main-campaign allied/civilian health is ×3; EDF/Marauder health is ×2. Stock equipment, squad references and spawn vehicle pools are retained. DLC has separate faction handling and exceptions for two scripted actors.
- **Vehicle adjustments:** selected speed/engine values are ×1.5 and selected health values are ×5. These changes do not apply uniformly to every vehicle.
- **More forgiving activities and economy:** selected objective timers are ×3, courier escape speed is divided by 3, explicit salvage rewards are ×3, and positive purchase/upgrade costs are halved with integer rounding.
- **Faster encounters and salvage collection:** selected reinforcement delays are halved; newly spawned salvage has a 250 ms collection delay. The salvage-after-death setting is configured to retain 100%, but its actual death/save behavior still needs testing.

These are scoped changes to the relevant table entries, rather than global multipliers applied to every game statistic. Detailed parameter reports are available below.

## All ten backpacks retuned

The following describes the new configuration. Actual behavior depends on the game engine, mode, progression and existing upgrades.

- **Jetpack:** fuel consumption reduced from 0.3 to 0.075 per second; regeneration increased from 0.15 to 0.5. Lower fuel consumption does not establish a higher flight ceiling.
- **Fleetfoot:** active movement multiplier set to 2.0, with lower fuel consumption and faster recovery. The backpack's fine-aim restriction is removed. Actual movement speed remains subject to engine and animation limits.
- **Heal:** active healing configured at 900 HP/second with a radius of 10; the active enemy-healing flag is disabled. Fuel consumption is greatly reduced. Healing campaign NPCs or hostages is unconfirmed.
- **Rhino:** charge speed configured at 14 m/s, lower fuel drain, faster recovery, a lower activation threshold and player-controlled cancellation enabled in the data.
- **Thrust:** vertical velocity boost increased from 10 to 15, with faster fuel recovery and activation allowed below a full tank.
- **Tremor:** shorter fuel-driven bursts, faster recovery and 50% more structural damage per pulse. Existing pulse spacing and radii are retained.
- **Concussion:** wider character-push range and stronger character knockback. Structural damage from its associated blast is reduced by 80% to make its destructive effect easier to manage.
- **Firepower:** direct-damage multiplier set to 2.0 and reload-duration factor to 0.7. Its area-damage multiplier is set to 1.0, retaining the underlying explosive profile without an additional Firepower area bonus.
- **Vision:** lower fuel drain, faster recovery and shorter visual transition times. Campaign target detection still needs testing.
- **Stealth:** lower fuel drain, faster recovery, a 250 ms cloaking transition and a 500 ms recloaking delay. Campaign AI detection behavior is unconfirmed.

Firepower is named **Commando** in the data; Concussion is named **Shockwave**. Fuel overrides for Commando, Vision and Stealth are synchronized with the main profiles.

Backpack unlock conditions are retained. This package does not automatically grant or unlock every backpack.

## Requirements and installation

Requires the PC version of **Red Faction Guerrilla Re-Mars-tered**. No additional mod or RSL installation is required for this VPP package. Game-build and storefront compatibility have not been comprehensively tested.

1. Close the game and back up your saves.
2. Locate the game folder containing your existing **misc.vpp_pc** and **table.vpp_pc**. Back up both files.
3. Extract the V4.2 main download.
4. Copy **both VPP files** into that folder and replace the existing files.
5. Test on a separate save before using the mod for important missions.

This is a complete package. The original Ultimate Mod download and earlier versions of this build are not required. Installation is manual; no mod-manager-specific installer is included.

To uninstall, close the game and restore both backed-up VPP files. If necessary, use your storefront's verify/repair function to restore game files; this may also overwrite other archive replacements.

## Compatibility

- Treat other mods replacing **misc.vpp_pc** or **table.vpp_pc** as conflicting. Combining them requires merging their underlying changes and repacking the archives.
- Shared weapon definitions can affect NPC-versus-NPC combat as well as the player's attacks.
- Backpack definitions are shared with multiplayer/Wrecking Crew. This release is intended for offline play; multiplayer behavior has not been validated.
- Runtime tools and other mods may override these settings. The separate experimental jump addon from the GitHub project is not included or required.

## Testing status and known limitations

**Data validation is complete; gameplay validation is still pending.** Checks cover archive structure, entry offsets, filename hashes, extraction round trips, modified XML, parameter values and fuel-override consistency. All modified XTBL files parse successfully.

- Backpack durations and Rhino travel distances derived from fuel are theoretical estimates, not measured results. Fuel capacity, regeneration while active and upgrade modifiers need in-game verification.
- Longer Jetpack fuel duration does not guarantee increased maximum height or lift.
- Heal support for campaign NPCs/hostages, Stealth interactions with AI and Vision's campaign targets are unconfirmed.
- Stronger hammer attacks, explosions and knockback can kill hostages, damage escort vehicles or collapse mission buildings. Alec's durability does not protect mission objectives.
- Save behavior, individual DLC encounters and compatibility with other mods have not been fully tested.

If reporting a problem, please include the mod version, game build/storefront, game mode, relevant backpack/upgrades, other installed mods, and steps to reproduce the issue. Screenshots or a short video are useful when available.

## Credits and documentation

Earlier work on this project was inspired by [Ultimate Mod on Nexus Mods](https://www.nexusmods.com/redfactionguerrillaremarstered/mods/16). The V4.x campaign balance was rebuilt using original game-table values, with further hammer, quality-of-life and backpack revisions.

- [Project, downloads and version history](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed)
- [V4.2 backpack configuration and validation](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/blob/main/reports/campaign-v4_2.md)
- [Underlying campaign and hammer configuration](https://github.com/ttgpPsychMH/RFGRM-UltimateModFixed/blob/main/reports/campaign-v4_1.md)

Detailed change inventories, checksums, build scripts and the independent validator are included in the optional reports download.
