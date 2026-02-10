import json
import os
from typing import Iterable, Dict, List


def find_lore_items(
    folder_path: str,
    search_keys: Iterable[str],
) -> Dict[str, List[str]]:
    """
    Scan all JSON files in folder_path.
    For each search key, return the list of matching 'Name' values.
    """
    results = {key: [] for key in search_keys}

    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(".json"):
            continue

        file_path = os.path.join(folder_path, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue  # skip unreadable or invalid JSON

        if not isinstance(data, list):
            continue

        for obj in data:
            if not isinstance(obj, dict):
                continue

            name = obj.get("Name")
            if not name:
                continue

            asset_path = (
                obj
                .get("Properties", {})
                .get("JournalEntry", {})
                .get("AssetPathName")
            )

            if not isinstance(asset_path, str):
                continue

            for key in search_keys:
                if key in asset_path:
                    results[key].append(name)

    return results


if __name__ == "__main__":
    folder = r"C:/prj/app/FModel/Output/Exports/RSDragonwilds/Content/Maps/World/L_World/_Generated_"
    entries = [
        {"key": "Withering_4", "value": "Battered Diary"},
        {"key": "Zogres_3", "value": "Captain Rainer's Journal"},
        {"key": "Withering_3", "value": "Dragon-embossed Journal"},
        {"key": "Dragonwolves_2", "value": "Experiment Log"},
        {"key": "Zogres_1", "value": "Farmer Fred's Journal"},
        {"key": "Dragonwolves_1", "value": "Laboratory Note"},
        {"key": "Dragonkin_5", "value": "Lacrussa's Diary"},
        {"key": "Dragonkin_1", "value": "Lacrussa's Journal"},
        {"key": "Vault_Puzzle_1", "value": "Lacrussa's Memoir"},
        {"key": "Dragonkin_2", "value": "Lacrussa's Notes"},
        {"key": "Dragonkin_3", "value": "Lacrussa's Ravings"},
        {"key": "Dragonkin_4", "value": "Lacrussa's Writings"},
        {"key": "Withering_2", "value": "Lazilly-penned Diary"},
        {"key": "The_Rising_Dead_1", "value": "Mould-covered Journal"},
        {"key": "The_Rising_Dead_5", "value": "Priestly Journal"},
        {"key": "Necromancer_And_The_Wolf_5", "value": "Ravanna's Fifth Journal"},
        {"key": "Necromancer_And_The_Wolf_1", "value": "Ravanna's First Journal"},
        {"key": "Necromancer_And_The_Wolf_4", "value": "Ravanna's Fourth Journal"},
        {"key": "Necromancer_And_The_Wolf_2", "value": "Ravanna's Second Journal"},
        {"key": "Necromancer_And_The_Wolf_7", "value": "Ravanna's Seventh Journal"},
        {"key": "Necromancer_And_The_Wolf_6", "value": "Ravanna's Sixth Journal"},
        {"key": "Necromancer_And_The_Wolf_3", "value": "Ravanna's Third Journal"},
        {"key": "The_Rising_Dead_4", "value": "Red-stained Diary"},
        {"key": "Vault_Puzzle_2", "value": "Rot-covered Journal"},
        {"key": "The_Rising_Dead_3", "value": "Soot-stained Journal"},
        {"key": "Dragonwolves_3", "value": "The Tale of the Ghost Wolves"},
        {"key": "Zogres_2", "value": "Ulgo's Diary"},
        {"key": "Withering_1", "value": "Weathered Diary"},
        {"key": "Withering_5", "value": "Weathered Journal"},
        {"key": "Withering_6", "value": "Withered Diary"},
        {"key": "The_Rising_Dead_2", "value": "Withered Journal"},
    ]
    keys = [entry["key"] for entry in entries]
    map = {item["key"]: item["value"] for item in entries}

    matches = find_lore_items(folder, keys)

    for key, names in matches.items():
        for n in names:
            print(f"{{\"key\": \"{key}\", \"label\": \"{map[key]}\", \"value\": \"{n}\"}},")