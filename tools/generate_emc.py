"""Generate data/cataclysm/pe_custom_conversions/cataclysm_default.json (NeoForge 1.21.1).

Values come from `_research/emc_campaign_2026-08-26/CATACLYSM_EMC_SPEC.md` SS3
(values.before, 56 id) and SS4.3 (groups.altar_of_amethyst, 1 conversion). Every number
below is copied from that spec -- this script only encodes the ProjectE 1.21.1
(PE1.1.0) JSON shape and verifies the written file by reading it back.

Notable spec rulings baked in here:
- Music discs are enumerated BY ID (9 discs), never via a tag: PE1.1.0 has no value on
  `#minecraft:music_discs`, and the host's own tag misses `music_disc_maledictus`
  (SPEC SS7-5 / SS8-5). Hand-setting all 9 makes the tag irrelevant.
- The Altar of Amethyst conversion is a plain 1:1 swap (single input slot, no catalyst,
  javap of AltarOfAmethyst_Block_Entity), so the group prices output = input = 64.
- Gear (tools/weapons/armour), stateful curios (4), ancient_metal_block/witherite_block
  (derived from ingot x9) and AUTO functional items are intentionally absent.

Usage: python tools/generate_emc.py [--verify-only]
"""

import json
import os
import sys

OUT = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "main",
    "resources",
    "data",
    "cataclysm",
    "pe_custom_conversions",
    "cataclysm_default.json",
)

# Hand-set EMC values, SPEC SS3. Comment on each id = spec's "根拠" column, condensed.
# (suffix, emc, comment); full id is f"cataclysm:{suffix}".
BEFORE = [
    # SS3.1 M metals (6)
    ("black_steel_ingot", 288, "early-game metal (draugr drops, ruin chests), just above iron(256); 32x9 nugget(32), block 2592"),
    ("ancient_metal_ingot", 1152, "koboleton dungeons + Ancient Remnant; 4.5x iron; 128x9 nugget(128), block 10368"),
    ("ignitium_ingot", 2304, "Ignis drops 3/fight; just above gold(2048); block 20736"),
    ("witherite_ingot", 2560, "Harbinger drops block(=9 ingots)/fight; between gold and emerald; block 23040"),
    ("cursium_ingot", 3072, "Maledictus drops 3-4/fight; advancement-wise after frosted prison; block 27648"),
    ("enderite_block", 9216, "end-structure mining primitive (no ingot exists); just above diamond(8192), below netherite_scrap(12288)"),
    # SS3.2 D/E mob drops (13)
    ("lacrima", 64, "ocean mob drop (scylla 8-16); seed for derived azure_seastone(9)"),
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
    # SS3.3 F functional drops / treasure (9)
    ("strange_key", 512, "aptrgangr key drop; consumable but non-stateful non-wearable primitive"),
    ("void_jaw", 768, "crying_obsidian band; endermaptera 1-2; void_scatter_arrow (AUTO) input"),
    ("void_core", 1024, "ender_pearl band (PE's own End-mob precedent); void_forge fusion input"),
    ("sandstorm_in_a_bottle", 1024, "nautilus_shell band; Ancient Remnant guaranteed drop; wrath_of_the_desert fusion input"),
    ("goddess_statue", 1024, "sunken-city decor statue (mined)"),
    ("remnant_skull", 1024, "boss skull; above vanilla head(256)"),
    ("unbreakable_skull", 1024, "desert_treasure chest skull"),
    ("essence_of_the_storm", 1536, "blaze_rod band; scylla 3-4; astrape/ceraunus (GEAR) input"),
    ("abyssal_egg", 2048, "shulker_shell band; Leviathan guaranteed drop; consumed on use -> entity, no EMC loop (SS8-4)"),
    # SS3.4 H heads (3)
    ("aptrgangr_head", 256, "vanilla skeleton head anchor; self-drop block"),
    ("draugr_head", 256, "vanilla zombie head anchor; self-drop block"),
    ("kobolediator_skull", 256, "vanilla creeper head anchor; self-drop block"),
    # SS3.5 C ruins decor & traps (16)
    ("pointed_icicle", 16, "ink_sac band decor shard; self-drop"),
    ("void_stone", 16, "mutated end_stone(1); common input of trap bricks/void_purpur_tiles (consumed as sink)"),
    ("void_infused_end_stone_bricks", 64, "obsidian band upgrade of end_stone_bricks(1); self-drop only"),
    ("azure_seastone_mural_cindaria", 64, "ruin mural relic (painted, one of 10); derived seastone is 9; self-drop so place/break neutral (SS6-6)"),
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
    # SS3.6 music discs (9) -- enumerated BY ID, never a tag (SPEC SS7-5 ruling)
    ("music_disc_ancient_remnant", 2048, "ProjectE disc band 2048; PE1.1.0 has no #minecraft:music_discs value; host tag not relied on (maledictus missing there)"),
    ("music_disc_ender_guardian", 2048, "ProjectE disc band 2048; hand-restored, id-enumerated"),
    ("music_disc_ignis", 2048, "ProjectE disc band 2048; hand-restored, id-enumerated"),
    ("music_disc_maledictus", 2048, "ProjectE disc band 2048; MISSING from host music_discs tag on 1.21.1 -- must stay explicit (SS7-5)"),
    ("music_disc_netherite_monstrosity", 2048, "ProjectE disc band 2048; hand-restored, id-enumerated"),
    ("music_disc_scylla", 2048, "ProjectE disc band 2048; hand-restored, id-enumerated"),
    ("music_disc_the_harbinger", 2048, "ProjectE disc band 2048; hand-restored, id-enumerated"),
    ("music_disc_the_leviathan", 2048, "ProjectE disc band 2048; hand-restored, id-enumerated"),
    ("music_disc_the_cataclysmfarer", 2048, "ProjectE disc band 2048; survey '?' item resolved to the disc band (SS0)"),
]

EXPECTED_DISCS = [
    "ancient_remnant", "ender_guardian", "ignis", "maledictus",
    "netherite_monstrosity", "scylla", "the_harbinger", "the_leviathan",
    "the_cataclysmfarer",
]

# SS4.3 verbatim structure: single-slot altar, no catalyst -> 1:1 equal swap.
GROUPS = {
    "altar_of_amethyst": {
        "comment": (
            "cataclysm:amethyst_bless is a custom recipe type (AltarOfAmethyst), so "
            "ProjectE cannot derive it. The altar consumes only the input item (single "
            "slot, AltarOfAmethyst_BlockEntity#cookAndOutputItems); there is no catalyst."
        ),
        "conversions": [
            {
                "output": {
                    "type": "projecte:item",
                    "id": "cataclysm:blessed_amethyst_crab_meat",
                },
                "count": 1,
                "ingredients": [
                    {"type": "projecte:item", "id": "cataclysm:amethyst_crab_meat"}
                ],
            }
        ],
    }
}

COMMENT = (
    "L_Ender's Cataclysm EMC integration for ProjectE (KURONAMI). Values per "
    "_research/emc_campaign_2026-08-26/CATACLYSM_EMC_SPEC.md (SS3/SS4, rulings SS8). "
    "Gear (tools/weapons/armour incl. sturdy_boots), stateful curios (berserker_soul_"
    "amulet, ring_of_grudged, necklace_of_the_desert, vitality_ankh) and khopesh "
    "(no acquisition path) intentionally have no EMC. ancient_metal_block/witherite_"
    "block derive from their ingots (x9). Music discs are enumerated by id because "
    "PE1.1.0 gives no value to #minecraft:music_discs."
)


def build_doc() -> dict:
    return {
        "replace": False,
        "comment": COMMENT,
        "values": {
            "before": [
                {"type": "projecte:item", "emc_value": v, "id": f"cataclysm:{k}"}
                for k, v, _ in BEFORE
            ]
        },
        "groups": GROUPS,
    }


def verify(path: str) -> None:
    """Read back the written JSON and diff it against the in-script SPEC tables."""
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)

    errors: list[str] = []

    got = {
        e["id"]: e["emc_value"]
        for e in doc["values"]["before"]
        if isinstance(e, dict)
        and set(e) == {"type", "emc_value", "id"}
        and e["type"] == "projecte:item"
    }
    if len(got) != len(doc["values"]["before"]):
        errors.append("values.before entries deviate from {type,emc_value,id} shape")

    expected = {f"cataclysm:{k}": v for k, v, _ in BEFORE}
    for rid in sorted(set(expected) | set(got)):
        if expected.get(rid) != got.get(rid):
            errors.append(f"value mismatch {rid}: expected {expected.get(rid)}, got {got.get(rid)}")

    if len(expected) != 56:
        errors.append(f"SPEC SS3 table size is {len(expected)}, expected 56")

    discs = [k for k, _, _ in BEFORE if k.startswith("music_disc_")]
    if sorted(discs) != sorted(f"music_disc_{n}" for n in EXPECTED_DISCS):
        errors.append("disc enumeration does not match the 9 SPEC SS3.6 ids")
    if any("tag" in json.dumps(e) for e in doc["values"]["before"]):
        errors.append("a tag reference leaked into values.before (SS7-5 forbids tag-dependent discs)")

    conv = doc["groups"]["altar_of_amethyst"]["conversions"]
    if len(conv) != 1:
        errors.append("groups.altar_of_amethyst must hold exactly 1 conversion")
    else:
        c = conv[0]
        if c["output"] != {"type": "projecte:item", "id": "cataclysm:blessed_amethyst_crab_meat"}:
            errors.append("group output mismatch")
        if c["ingredients"] != [{"type": "projecte:item", "id": "cataclysm:amethyst_crab_meat"}]:
            errors.append("group ingredients mismatch (must be the single meat input)")
        if c.get("count") != 1:
            errors.append("group count must be 1")

    print(f"verify: values.before={len(got)} (expect 56), groups conversions={len(conv)}")
    for k, v, _ in BEFORE:
        mark = "ok" if got.get(f"cataclysm:{k}") == v else "MISMATCH"
        print(f"  {mark:8s} cataclysm:{k} = {v}")
    if errors:
        for e in errors:
            print(f"VERIFY FAILED: {e}", file=sys.stderr)
        sys.exit(1)
    print("verify: all 56 ids match CATACLYSM_EMC_SPEC.md SS3; groups match SS4.3")


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
