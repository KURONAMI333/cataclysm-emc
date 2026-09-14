# ProjectE: EMC for L_Ender's Cataclysm

Give L_Ender's Cataclysm materials hand-tuned EMC values so its boss loot and dungeon metals work with ProjectE's transmutation system.

Cataclysm is all about bosses, dungeons and ruins, and almost none of its rewards are craftable. ProjectE learns values by following recipes, so items that only drop from fights stay worthless forever. This add-on hand-tunes the values where recipes are missing and lets ProjectE derive everything else from the host's own vanilla-type recipes.

- Metals follow the host's progression: black steel → ancient metal → ignitium → witherite → cursium → enderite, each tier priced above the previous one
- Boss materials pay for the fight: every summon key vs. loot yield was checked numerically across all eight bosses
- Nuggets and blocks derive exactly from ingots — ingot values are multiples of nine, so round trips are lossless
- Tools, weapons, armour and curios intentionally get no EMC, same as vanilla

## Usage

There is no config, command, or item. The conversion file registers with ProjectE at startup (`Considering file cataclysm:pe_custom_conversions/cataclysm_default.json` in the log), and the values simply exist.

Hand-set highlights:

```
black_steel_ingot      288    ancient_metal_ingot   1152
ignitium_ingot        2304    witherite_ingot       2560
cursium_ingot         3072    enderite_block        9216
monstrous_horn        4096    abyssal_egg           2048
music discs (x9)      2048    void_core             1024
```

The Amethyst Altar uses a custom recipe type that ProjectE cannot see, so its one conversion (blessed amethyst crab meat) is defined explicitly as the 1:1 exchange it actually is — the altar consumes only the input, there is no catalyst.

## Dependencies

- [L_Ender's Cataclysm](https://modrinth.com/mod/l_enders-cataclysm) — required
- ProjectE — required. It is distributed on CurseForge only, so it cannot be declared as a Modrinth dependency; grab it [here](https://www.curseforge.com/minecraft/mc-mods/projecte)

## Compatibility & scope

Verified against Cataclysm 3.33 (NeoForge 1.21.1) and 3.31 (Forge 1.20.1), the current releases of the host. The add-on ships no host assets — only id strings and numbers — so it stays independent of how the host packages its content.

## Known limitations

- Two slab ids (stone tile slab, polished end stone slab) compute to less than 1 EMC and end at 0. That is the same place vanilla slabs occupy, not a bug
- Ancient Remnant and The Harbinger runs come out ahead of the summon cost (2.46x / 2.18x). That is deliberate: the fight itself is multi-stage work, and the reward band was kept intact rather than squeezed
- Items with no acquisition path (khopesh, final fractal, etc.) deliberately have no EMC — valuing them would create creative-only currency

## License

All Rights Reserved. Free to put in any modpack, on any platform, monetised or not - no permission needed, no credit required. Source is published so you can read exactly what it does.

Built for [L_Ender's Cataclysm](https://modrinth.com/mod/l_enders-cataclysm) by L_Ender (assets © MCL_Ender, source LGPL v3.0 — none are included here).

## Downloads and support

Downloads: [CurseForge](https://www.curseforge.com/minecraft/mc-mods/projecte-emc-for-cataclysm).

For bugs and questions, comment on the [CurseForge page](https://www.curseforge.com/minecraft/mc-mods/projecte-emc-for-cataclysm) or DM [@kuronami333 on X](https://x.com/kuronami333).

[Source](https://github.com/KURONAMI333/cataclysm-emc) · [License](LICENSE)
