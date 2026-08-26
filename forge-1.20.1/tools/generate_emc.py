"""Generate data/cataclysm/pe_custom_conversions/cataclysm_default.json
for ProjectE on Minecraft 1.20.1 (PE1.0.1, Forge).

Values come from `_research/emc_campaign_2026-08-26/CATACLYSM_EMC_SPEC.md` SS5,
which is the 1.21.1 SS3 table (56 id) minus the 9 music discs -- PE1.0.1's own
defaults.json carries `#minecraft:music_discs` = 2048 so all 9 discs are valued
through the tag (SS5.1) -- plus the 22 `curved_azure_seastone_*` blocks that 1.20.1
cannot derive (no stonecutting recipe; all PRIM in the survey). NOTE: SPEC SS5.1's
explicit enumeration lists 22 ids (4+4+4+9+1); the prose count "21" is an arithmetic
slip -- the enumeration is authoritative and is what this generator writes.

ProjectE 1.20.1's CustomConversionFile reads `values.before` as a MAP ({id: emc}),
`output` as a bare string and `ingredients` as an array of strings / map form
(PROJECTE_EMC_NOTES.md SS1.20.1 展開 table; PE1.0.1 jar's own defaults/metals JSON).
The altar_of_amethyst group exists here too: the blessed_amethyst_crab_meat recipe
is present on 1.20.1 (SPEC SS4.2/SS4.3).

Usage: python tools/generate_emc.py [--verify-only]
"""

import json
import os
import sys

OUT = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "data",
    "cataclysm",
    "pe_custom_conversions",
    "cataclysm_default.json",
)

# Hand-set EMC values, SPEC SS3 values kept verbatim (SS5: identical across cells)
# minus the 9 discs, plus the 22 curved_azure_seastone_* at SS5.1.
# (suffix, emc, comment); full id is f"cataclysm:{suffix}".
BEFORE = [
    # SS3.1 M metals (6) -- identical to 1.21.1
    ("black_steel_ingot", 288, "early-game metal (draugr drops, ruin chests), just above iron(256); 32x9 nugget(32), block 2592"),
    ("ancient_metal_ingot", 1152, "koboleton dungeons + Ancient Remnant; 4.5x iron; 128x9 nugget(128), block 10368"),
    ("ignitium_ingot", 2304, "Ignis drops 3/fight; just above gold(2048); block 20736"),
    ("witherite_ingot", 2560, "Harbinger drops block(=9 ingots)/fight; between gold and emerald; block 23040"),
    ("cursium_ingot", 3072, "Maledictus drops 3-4/fight; advancement-wise after frosted prison; block 27648"),
    ("enderite_block", 9216, "end-structure mining primitive (no ingot exists); just above diamond(8192), below netherite_scrap(12288)"),
    # SS3.2 D/E mob drops (13) -- identical to 1.21.1
    ("lacrima", 64, "ocean mob drop (scylla 8-16); seed for the seastone chain (no stonecutting here, murals hand-set instead)"),
    ("lionfish", 64, "vanilla cod/salmon anchor"),
    ("koboleton_bone", 64, "common small-bone drop; below vanilla bone(144) since 3-5 drop per kill"),
    ("amethyst_crab_meat", 64, "vanilla beef anchor; altar_of_amethyst group input"),
    ("crystallized_coral_fragments", 128, "coral_golem guaranteed drop; 4 -> crystallized_coral(512) integral"),
    ("coral_chunk", 256, "prismarine_shard band; coralssus guaranteed drop"),
    ("void_crystal", 256, "quartz band; mining cluster"),
    ("void_lantern_block", 256, "glowing decor; glowstone-block tier"),
    ("lava_power_cell", 256, "monstrosity drops 16-24, kept low: ~20x256=5120 ~= summon key (SS6-7)"),
    ("amethyst_crab_shell", 512, "prismarine_crystals band; crab drops 3-5; bloom_stone_pauldrons sink input"),
    ("chitin_claw", 512, "clawdian guaranteed drop"),
    ("dying_ember", 512, "above gunpowder(192)/bone(144); ignited_berserker 0-2; burning_ashes derives at 2048 (no multiplication path)"),
    ("monstrous_horn", 4096, "uranium band; monstrosity guaranteed drop; monstrous_helm smithing input"),
    # SS3.3 F functional drops / treasure (9) -- identical to 1.21.1
    ("strange_key", 512, "aptrgangr key drop; consumable but non-stateful non-wearable primitive (SS8-4)"),
    ("void_jaw", 768, "crying_obsidian band; endermaptera 1-2; void_scatter_arrow (AUTO) input"),
    ("void_core", 1024, "ender_pearl band (PE's own End-mob precedent); void_forge fusion input"),
    ("sandstorm_in_a_bottle", 1024, "nautilus_shell band; Ancient Remnant guaranteed drop (SS8-4)"),
    ("goddess_statue", 1024, "sunken-city decor statue (mined)"),
    ("remnant_skull", 1024, "boss skull; above vanilla head(256)"),
    ("unbreakable_skull", 1024, "desert_treasure chest skull"),
    ("essence_of_the_storm", 1536, "blaze_rod band; scylla 3-4; astrape/ceraunus (GEAR) input"),
    ("abyssal_egg", 2048, "shulker_shell band; Leviathan guaranteed drop; consumed on use -> entity, no EMC loop (SS8-4)"),
    # SS3.4 H heads (3) -- identical to 1.21.1
    ("aptrgangr_head", 256, "vanilla skeleton head anchor; self-drop block"),
    ("draugr_head", 256, "vanilla zombie head anchor; self-drop block"),
    ("kobolediator_skull", 256, "vanilla creeper head anchor; self-drop block"),
    # SS3.5 C ruins decor & traps (16) -- identical to 1.21.1
    ("pointed_icicle", 16, "ink_sac band decor shard; self-drop"),
    ("void_stone", 16, "mutated end_stone(1); common input of trap bricks/void_purpur_tiles (consumed as sink)"),
    ("void_infused_end_stone_bricks", 64, "obsidian band upgrade of end_stone_bricks(1); self-drop only"),
    ("azure_seastone_mural_cindaria", 64, "ruin mural relic (painted, one of 10); self-drop so place/break neutral (SS6-6)"),
    ("azure_seastone_mural_clawdian", 64, "ruin mural relic; self-drop"),
    ("azure_seastone_mural_harvest", 64, "ruin mural relic; self-drop"),
    ("azure_seastone_mural_hippocamtus", 64, "ruin mural relic; self-drop"),
    ("azure_seastone_mural_sea", 64, "ruin mural relic; self-drop"),
    ("azure_seastone_mural_smithing", 64, "ruin mural relic; self-drop"),
    ("azure_seastone_mural_thunder", 64, "ruin mural relic; self-drop"),
    ("azure_seastone_mural_underworld", 64, "ruin mural relic; self-drop"),
    ("azure_seastone_mural_urchinkin", 64, "ruin mural relic; self-drop"),
    ("azure_seastone_mural_wisdom", 64, "ruin mural relic; self-drop"),
    ("sandstone_falling_trap", 64, "trap body; triggers spawn entities with DISALLOWED pickup / no item drops (SS6-1); contents sum 0 <= 64"),
    ("sandstone_ignite_trap", 64, "trap body; ignition only, no item source (SS6-1)"),
    ("sandstone_poison_dart_trap", 64, "trap body; dart arrow is DISALLOWED-pickup, no EMC source (SS6-1)"),
    # SS5.1 curved_azure_seastone (22) -- 1.20.1-only hand-set; no stonecutting recipe
    # exists on this cell (all PRIM in survey), priced at the mural band 64 per SS5.1.
    ("curved_azure_seastone_cindaria_1", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_cindaria_2", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_cindaria_3", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_cindaria_4", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_clawdian_1", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_clawdian_2", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_clawdian_3", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_clawdian_4", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_hippocamtus_1", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_hippocamtus_2", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_hippocamtus_3", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_hippocamtus_4", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_scylla_1", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_scylla_2", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_scylla_3", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_scylla_4", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_scylla_5", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_scylla_6", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_scylla_7", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_scylla_8", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_scylla_9", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
    ("curved_azure_seastone_urchinkin", 64, "curved seastone variant; no 1.20.1 derivation, mural band (SS5.1)"),
]

# Music discs intentionally absent: #minecraft:music_discs = 2048 in PE1.0.1 defaults
# covers all 9 (host tag holds all 9 on 1.20.1, verified in survey).

EXPECTED_CURVED = [
    *[f"curved_azure_seastone_cindaria_{i}" for i in range(1, 5)],
    *[f"curved_azure_seastone_clawdian_{i}" for i in range(1, 5)],
    *[f"curved_azure_seastone_hippocamtus_{i}" for i in range(1, 5)],
    *[f"curved_azure_seastone_scylla_{i}" for i in range(1, 10)],
    "curved_azure_seastone_urchinkin",
]

# SS4.3 rewritten to the PE1.0.1 shape: bare-string output, array ingredients.
GROUPS = {
    "altar_of_amethyst": {
        "comment": (
            "cataclysm:amethyst_bless is a custom recipe type (AltarOfAmethyst), so "
            "ProjectE cannot derive it. The altar consumes only the input item (single "
            "slot); there is no catalyst."
        ),
        "conversions": [
            {
                "output": "cataclysm:blessed_amethyst_crab_meat",
                "count": 1,
                "ingredients": ["cataclysm:amethyst_crab_meat"],
            }
        ],
    }
}

COMMENT = (
    "L_Ender's Cataclysm EMC integration for ProjectE (KURONAMI). Values per "
    "_research/emc_campaign_2026-08-26/CATACLYSM_EMC_SPEC.md (SS5). Gear (tools/"
    "weapons/armour incl. sturdy_boots), stateful curios (berserker_soul_amulet, "
    "ring_of_grudged, necklace_of_the_desert, vitality_ankh) and khopesh (no "
    "acquisition path) intentionally have no EMC. ancient_metal_block/witherite_block "
    "derive from their ingots (x9). Music discs need no entry: PE1.0.1 defaults value "
    "#minecraft:music_discs at 2048."
)


def build_doc() -> dict:
    return {
        "comment": COMMENT,
        "values": {
            "before": {f"cataclysm:{k}": v for k, v, _ in BEFORE}
        },
        "groups": GROUPS,
    }


def verify(path: str) -> None:
    """Read back the written JSON and diff it against the in-script SPEC tables."""
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)

    errors: list[str] = []

    before = doc["values"]["before"]
    if not isinstance(before, dict):
        errors.append("values.before must be a MAP {id: emc} on PE1.0.1")
        sys.exit(1)

    expected = {f"cataclysm:{k}": v for k, v, _ in BEFORE}
    for rid in sorted(set(expected) | set(before)):
        if expected.get(rid) != before.get(rid):
            errors.append(f"value mismatch {rid}: expected {expected.get(rid)}, got {before.get(rid)}")

    if len(expected) != 69:
        errors.append(f"SPEC SS5 table size is {len(expected)}, expected 69 (47 shared + 22 curved)")

    got_curved = sorted(k[len("cataclysm:"):] for k in before if "curved_azure_seastone" in k)
    if got_curved != sorted(EXPECTED_CURVED):
        errors.append("curved_azure_seastone enumeration does not match SPEC SS5.1's 22 ids")
    discs = [k for k in before if "music_disc" in k]
    if discs:
        errors.append(f"discs must NOT be hand-set on 1.20.1 (tag-valued): {discs}")

    conv = doc["groups"]["altar_of_amethyst"]["conversions"]
    if len(conv) != 1:
        errors.append("groups.altar_of_amethyst must hold exactly 1 conversion")
    else:
        c = conv[0]
        if c["output"] != "cataclysm:blessed_amethyst_crab_meat":
            errors.append("group output must be a bare string id")
        if c["ingredients"] != ["cataclysm:amethyst_crab_meat"]:
            errors.append("group ingredients mismatch (must be the single meat input)")
        if c.get("count") != 1:
            errors.append("group count must be 1")

    print(f"verify: values.before={len(before)} (expect 69), groups conversions={len(conv)}")
    for k, v, _ in BEFORE:
        mark = "ok" if before.get(f"cataclysm:{k}") == v else "MISMATCH"
        print(f"  {mark:8s} cataclysm:{k} = {v}")
    if errors:
        for e in errors:
            print(f"VERIFY FAILED: {e}", file=sys.stderr)
        sys.exit(1)
    print("verify: all 69 ids match CATACLYSM_EMC_SPEC.md SS5; groups match SS4.3 (1201 form)")


def main() -> None:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    if "--verify-only" not in sys.argv[1:]:
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(build_doc(), f, ensure_ascii=False, indent=2)
            f.write("\n")
        n_groups = sum(len(g["conversions"]) for g in GROUPS.values())
        print(
            f"values.before={len(BEFORE)} groups.conversions={n_groups} -> {os.path.normpath(OUT)}"
        )
    verify(os.path.normpath(OUT))


if __name__ == "__main__":
    main()
