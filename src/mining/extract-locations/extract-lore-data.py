import json
import os
from typing import Dict, List, Tuple


def extract_lore_data(lore_folder: str) -> List[Dict]:
    """
    Extract key, title, text, and name from lore JSON files.
    """
    results = []
    for filename in os.listdir(lore_folder):
        if not filename.lower().endswith('.json'):
            continue

        filepath = os.path.join(lore_folder, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue

        if not isinstance(data, list) or not data:
            continue

        obj = data[0]
        name = obj.get('Name', '')
        props = obj.get('Properties', {})
        display_name = props.get('DisplayName', {})
        key = display_name.get('Key', '')
        title = display_name.get('LocalizedString', '')
        page_descriptions = props.get('PageDescriptions', [])
        text = ''
        if page_descriptions:
            desc = page_descriptions[0].get('Description', {})
            text = desc.get('LocalizedString', '')

        results.append({
            'name': name,
            'key': key
                    .replace('.', '_')
                    .replace('_DisplayName', '')
                    .replace('_title', '')
                    .replace('_Title', '')
                    .replace('_Name', ''),
            'title': title,
            'text': text
        })

    return results


def find_uaids(world_folder: str, names: List[str]) -> Dict[str, List[str]]:
    """
    Find UAIDs for given names by scanning world JSON files.
    """
    results = {name: [] for name in names}
    for filename in os.listdir(world_folder):
        if not filename.lower().endswith('.json'):
            continue

        filepath = os.path.join(world_folder, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue

        if not isinstance(data, list):
            continue

        for obj in data:
            if not isinstance(obj, dict):
                continue

            name = obj.get('Name')
            if not name:
                continue

            asset_path = obj.get('Properties', {}).get('JournalEntry', {}).get('AssetPathName')
            if not asset_path:
                continue

            for search_name in names:
                if search_name in asset_path:
                    results[search_name].append(name)

    return results


def find_coords(world_folder: str, uaids: List[str]) -> Dict[str, Tuple[float, float, float]]:
    """
    Find coordinates for given UAIDs by scanning world JSON files.
    """
    uaid_set = set(uaids)
    results = {}
    for filename in os.listdir(world_folder):
        if not filename.lower().endswith('.json'):
            continue

        filepath = os.path.join(world_folder, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue

        if not isinstance(data, list):
            continue

        for obj in data:
            if not isinstance(obj, dict):
                continue

            if obj.get('Type') != 'SceneComponent':
                continue

            outer = obj.get('Outer')
            if not isinstance(outer, dict):
                continue

            object_name = outer.get('ObjectName', '')
            if not object_name:
                continue

            matched_uaid = None
            for uaid in uaid_set:
                if uaid in object_name:
                    matched_uaid = uaid
                    break

            if not matched_uaid:
                continue

            props = obj.get('Properties', {})
            loc = props.get('RelativeLocation')
            if not isinstance(loc, dict):
                continue

            x = loc.get('X')
            y = loc.get('Y')
            z = loc.get('Z')
            if x is not None and y is not None and z is not None:
                results[matched_uaid] = (x, y, z)

    return results


if __name__ == "__main__":
    lore_folder = r"C:/prj/app/FModel/Output/Exports/RSDragonwilds/Content/UI/JournalData/Entries/Knowledge/LoreScraps"
    world_folder = r"C:/prj/app/FModel/Output/Exports/RSDragonwilds/Content/Maps/World/L_World/_Generated_"

    # Extract lore data
    lore_data = extract_lore_data(lore_folder)

    # Get names for UAID search
    names = [item['name'] for item in lore_data]

    # Find UAIDs
    uaids_map = find_uaids(world_folder, names)

    # Collect all UAIDs
    all_uaids = []
    for uaids in uaids_map.values():
        all_uaids.extend(uaids)

    # Find coords
    coords_map = find_coords(world_folder, all_uaids)

    # Build final results
    results = []
    for lore_item in lore_data:
        name = lore_item['name']
        uaids = uaids_map.get(name, [])
        for uaid in uaids:
            coords = coords_map.get(uaid)
            results.append({
                'key': lore_item['key'],
                'title': lore_item['title'],
                'uaid': uaid,
                'coords': coords,
                'text': lore_item['text']
            })

    # Write to output file
    with open('lore-data-output.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Generate Unreal sound map
    map_entries = []
    for item in results:
        coords = item['coords']
        if coords is not None:
            x, y, z = coords
            sound_path = f"/Script/Engine.SoundWave'/Game/Mods/LoreNarratorMod/Sound/Narrator/{item['key']}.{item['key']}'"
            map_entries.append(f"(X={x:.6f},Y={y:.6f},Z={z:.6f}), \"{sound_path}\"")
    
    if map_entries:
        entries_str = ",".join(f"({entry})" for entry in map_entries)
        full_map = f"({entries_str})"
        with open('unreal-sound-map.txt', 'w', encoding='utf-8') as f:
            f.write(full_map)