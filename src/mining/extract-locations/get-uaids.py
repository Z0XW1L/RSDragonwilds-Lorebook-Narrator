import json
import os
from typing import Iterable, Dict, List


def extract_name_from_path(asset_path: str) -> str:
    """
    Extract the name part from an AssetPathName.
    Example: "/Game/UI/JournalData/Entries/Knowledge/LoreScraps/JOURNAL_Know_Zogres_1.JOURNAL_Know_Zogres_1"
    Returns: "JOURNAL_Know_Zogres_1.JOURNAL_Know_Zogres_1"
    """
    if not asset_path:
        return ""
    return asset_path.split("/")[-1]


def transform_key(key: str) -> str:
    """
    Transform a key by extracting just the relevant part after the prefix.
    Example: "JOURNAL_Know_LoreScrap_C1.JOURNAL_Know_LoreScrap_C1" → "LoreScrap_C1"
    
    Args:
        key: The full key string
        
    Returns:
        The transformed key with prefix removed
    """
    # Extract the part before the first dot
    part = key.split(".")[0]
    
    # Remove the "JOURNAL_Know_" prefix if present
    if part.startswith("JOURNAL_Know_"):
        return part[len("JOURNAL_Know_"):]
    
    return part


def find_all_journal_entries(folder_path: str, filter_contains: str = None) -> Dict[str, List[Dict[str, str]]]:
    """
    Scan all JSON files and extract all AssetPathName entries as keys.
    Returns a dict mapping extracted names to lists of {label, uaid} entries.
    
    Args:
        folder_path: Path to the folder containing JSON files
        filter_contains: Optional filter string. Only includes entries whose keys contain this string.
    """
    results = {}

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

            uaid = obj.get("Name")
            if not uaid:
                continue

            properties = obj.get("Properties", {})
            if not isinstance(properties, dict):
                continue

            # Scan all properties for AssetPathName entries
            for prop_name, prop_value in properties.items():
                if not isinstance(prop_value, dict):
                    continue

                asset_path = prop_value.get("AssetPathName")
                if not isinstance(asset_path, str) or not asset_path:
                    continue

                # Extract the name part from the path
                key = extract_name_from_path(asset_path)
                if not key:
                    continue

                # Apply filter if specified
                if filter_contains and filter_contains not in key:
                    continue

                if key not in results:
                    results[key] = []

                results[key].append({
                    "label": prop_name,
                    "uaid": uaid
                })

    return results


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
    
    # Extract all journal entries automatically, filtered to only JOURNAL_Know_ entries
    print("=== All Journal Entry Keys (JOURNAL_Know_ only) ===\n")
    journal_entries = find_all_journal_entries(folder, filter_contains="JOURNAL_Know_")
    
    # Output in JSON format with transformed keys
    print(f"Found {sum(len(entries) for entries in journal_entries.values())} entries across {len(journal_entries)} unique keys.\n")
    for key, entries in sorted(journal_entries.items()):
        transformed_key = transform_key(key)
        for entry in entries:
            print(f"{{\"key\": \"{transformed_key}\", \"label\": \"{entry['label']}\", \"value\": \"{entry['uaid']}\"}},")
    
    print("\n=== Legacy Search Mode ===\n")
    legacy_entries = [
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
    keys = [entry["key"] for entry in legacy_entries]
    map = {item["key"]: item["value"] for item in legacy_entries}

    matches = find_lore_items(folder, keys)

    for key, names in matches.items():
        for n in names:
            print(f"{{\"key\": \"{key}\", \"label\": \"{map[key]}\", \"value\": \"{n}\"}},")
