# ProjectE: EMC for L_Ender's Cataclysm

> L_Ender's Cataclysm's materials can't enter ProjectE's transmutation system on their own — this add-on prices them, so boss loot and dungeon metals finally have an EMC value.

Cataclysm is all about bosses, dungeons and ruins, and almost none of its rewards are craftable. ProjectE learns values by following recipes, so items that only drop from fights stay worthless forever. This add-on hand-tunes the values where recipes are missing and lets ProjectE derive everything else from the host's own vanilla-type recipes.

- Metals follow the host's progression: black steel → ancient metal → ignitium → witherite → cursium → enderite, each tier priced above the previous one
- Boss materials pay for the fight: every summon key vs. loot yield was checked numerically across all eight bosses
- Nuggets and blocks derive exactly from ingots — ingot values are multiples of nine, so round trips are lossless
- Tools, weapons, armour and curios intentionally get no EMC, same as vanilla
- Server-side data only — clients do not need to install it

## What it does / Usage

Drop the jar on the **server** (singleplayer counts too) next to ProjectE and Cataclysm. There is no config, no command, no item: the conversion file registers with ProjectE at startup and the values simply exist.

Hand-set highlights:

```
black_steel_ingot      288    ancient_metal_ingot   1152
ignitium_ingot        2304    witherite_ingot       2560
cursium_ingot         3072    enderite_block        9216
monstrous_horn        4096    abyssal_egg           2048
music discs (x9)      2048    void_core             1024
```

The Amethyst Altar uses a custom recipe type that ProjectE cannot see, so its one conversion (blessed amethyst crab meat) is defined explicitly as the 1:1 exchange it actually is — the altar consumes only the input, there is no catalyst.

## Supported loaders / versions

| Minecraft | Loader | Cataclysm | ProjectE |
|---|---|---|---|
| 1.21.1 | NeoForge | 3.33 | PE 1.1.0 |
| 1.20.1 | Forge | 3.31 | PE 1.0.1 |

Both cells were verified on dedicated servers: EMC computation completes, zero parse errors, and the 1.20.1 value table matches the spec exactly (69/69). On 1.21.1 the host additionally requires lionfishapi and curios; install them as you normally would for Cataclysm.

## Dependencies

- [L_Ender's Cataclysm](https://www.curseforge.com/minecraft/mc-mods/cataclysm) — required
- [ProjectE](https://www.curseforge.com/minecraft/mc-mods/projecte) — required

## Compatibility & scope

Verified against Cataclysm 3.33 (NeoForge 1.21.1) and 3.31 (Forge 1.20.1), the current releases of the host. The add-on ships no host assets — only id strings and numbers — so it stays independent of how the host packages its content.

## Known limitations

- Two slab ids (stone tile slab, polished end stone slab) compute to less than 1 EMC and end at 0. That is the same place vanilla slabs occupy, not a bug
- Ancient Remnant and The Harbinger runs come out ahead of the summon cost (2.46x / 2.18x). That is deliberate: the fight itself is multi-stage work, and the reward band was kept intact rather than squeezed
- Items with no acquisition path (khopesh, final fractal, etc.) deliberately have no EMC — valuing them would create creative-only currency

## Install

1. Install NeoForge (MC 1.21.1) or Forge (MC 1.20.1)
2. Install L_Ender's Cataclysm and ProjectE
3. Drop `cataclysm_emc-0.1.0+neoforge-1.21.1.jar` or `cataclysm_emc-0.1.0+forge-1.20.1.jar` into `mods/` on the server

- Server-side · clients do not need it

## License

All Rights Reserved. Free to put in any modpack, on any platform, monetised or not - no permission needed, no credit required. Source is published so you can read exactly what it does.

Author: KURONAMI · Built for [L_Ender's Cataclysm](https://www.curseforge.com/minecraft/mc-mods/cataclysm) by L_Ender (assets © MCL_Ender, source LGPL v3.0 — none are included here)

Source: https://github.com/KURONAMI333/cataclysm-emc · Issues: https://github.com/KURONAMI333/cataclysm-emc/issues
