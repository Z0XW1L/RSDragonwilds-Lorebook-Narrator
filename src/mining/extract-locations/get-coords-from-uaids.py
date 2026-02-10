import json
import os
from typing import Iterable, Dict, Tuple


def find_relative_locations(
    folder_path: str,
    uaids: Iterable[str],
) -> Dict[str, Tuple[float, float, float]]:
    """
    Scan all JSON files in folder_path and find RelativeLocation
    for objects whose 'Outer' matches one of the given UAIDs.
    """
    uaid_set = set(uaids)
    results = {}

    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(".json"):
            continue

        file_path = os.path.join(folder_path, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue

        if not isinstance(data, list):
            continue

        for obj in data:
            if not isinstance(obj, dict):
                continue

            outer = obj.get("Outer")
            if outer not in uaid_set:
                continue

            props = obj.get("Properties", {})
            loc = props.get("RelativeLocation")

            if not isinstance(loc, dict):
                continue

            try:
                x = loc["X"]
                y = loc["Y"]
                z = loc["Z"]
            except KeyError:
                continue

            results[outer] = (x, y, z)

    return results


if __name__ == "__main__":
    folder = r"C:/prj/app/FModel/Output/Exports/RSDragonwilds/Content/Maps/World/L_World/_Generated_"

    entries = [
        {"key": "Withering_4", "label": "Battered Diary", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491148362"},
        {"key": "Zogres_3", "label": "Captain Rainer's Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1992942376"},
        {"key": "Withering_3", "label": "Dragon-embossed Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491185374"},
        {"key": "Dragonwolves_2", "label": "Experiment Log", "value": "BP_LoreItem_C_UAID_00BE4395530EA39202_2086739669"},
        {"key": "Zogres_1", "label": "Farmer Fred's Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491145361"},
        {"key": "Dragonwolves_1", "label": "Laboratory Note", "value": "BP_LoreItem_C_UAID_00BE4395530EA39202_2057669668"},
        {"key": "Dragonkin_5", "label": "Lacrussa's Diary", "value": "BP_LoreItem_C_UAID_088FC314E3CE939302_1324788089_32ab1e2f20fdaa73"},
        {"key": "Dragonkin_1", "label": "Lacrussa's Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491154364"},
        {"key": "Vault_Puzzle_1", "label": "Lacrussa's Memoir", "value": "BP_LoreItem_C_UAID_088FC314E3CE939302_1324791090_32ab1e2f20fdaa73"},
        {"key": "Dragonkin_2", "label": "Lacrussa's Notes", "value": "BP_LoreItem_C_UAID_088FC314E3CE939302_1324773088_32ab1e2f20fdaa73"},
        {"key": "Dragonkin_3", "label": "Lacrussa's Ravings", "value": "BP_LoreItem_C_UAID_088FC314E3CE939302_1941325335_4c90d5dc641d7a3d"},
        {"key": "Dragonkin_4", "label": "Lacrussa's Writings", "value": "BP_LoreItem_C_UAID_088FC314E3CE949302_1360610756_ce16175a5c482673"},
        {"key": "Withering_2", "label": "Lazilly-penned Diary", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491163367"},
        {"key": "The_Rising_Dead_1", "label": "Mould-covered Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491182373"},
        {"key": "The_Rising_Dead_5", "label": "Priestly Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491151363"},
        {"key": "Necromancer_And_The_Wolf_5", "label": "Ravanna's Fifth Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491138359"},
        {"key": "Necromancer_And_The_Wolf_1", "label": "Ravanna's First Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491082351"},
        {"key": "Necromancer_And_The_Wolf_4", "label": "Ravanna's Fourth Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491132357"},
        {"key": "Necromancer_And_The_Wolf_2", "label": "Ravanna's Second Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491175371"},
        {"key": "Necromancer_And_The_Wolf_7", "label": "Ravanna's Seventh Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491178372"},
        {"key": "Necromancer_And_The_Wolf_6", "label": "Ravanna's Sixth Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491142360"},
        {"key": "Necromancer_And_The_Wolf_3", "label": "Ravanna's Third Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491172370"},
        {"key": "The_Rising_Dead_4", "label": "Red-stained Diary", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491160366"},
        {"key": "Vault_Puzzle_2", "label": "Rot-covered Journal", "value": "BP_LoreItem_C_UAID_088FC314E3CE3E9A02_2046651038_4c90d5dc641d7a3d"},
        {"key": "The_Rising_Dead_3", "label": "Soot-stained Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491135358"},
        {"key": "Dragonwolves_3", "label": "The Tale of the Ghost Wolves", "value": "BP_LoreItem_C_UAID_00BE4395530EA39202_2089947670"},
        {"key": "Zogres_2", "label": "Ulgo's Diary", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1952382375"},
        {"key": "Withering_1", "label": "Weathered Diary", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491119353"},
        {"key": "Withering_5", "label": "Weathered Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491129356"},
        {"key": "Withering_6", "label": "Withered Diary", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491169369"},
        {"key": "The_Rising_Dead_2", "label": "Withered Journal", "value": "BP_LoreItem_C_UAID_00BE4395530E2A9202_1491116352"},
    ]
    reverse_map = {item["value"]: item["key"] for item in entries}
    label_map = {item["value"]: item["label"] for item in entries}

    uaids = [key["value"] for key in entries]

    locations = find_relative_locations(folder, uaids)

    for uaid, (x, y, z) in locations.items():
        print(f"{{\"coords\": ({x}, {y}, {z}), \"label\": \"{label_map.get(uaid, '')}\", \"key\": \"{reverse_map.get(uaid, '')}\"}},")
