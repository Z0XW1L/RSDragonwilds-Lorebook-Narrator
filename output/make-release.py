#!/usr/bin/env python3
"""
Script to copy mod files from the game installation to the release folder.
Supports multiple mods with configurable settings.
"""

import os
import shutil
from pathlib import Path
from typing import List, Dict

# Configuration
GAME_BASE_PATH = Path(r"C:\Program Files (x86)\Steam\steamapps\common\RSDragonwilds\RSDragonwilds")
RELEASE_BASE_PATH = Path(__file__).parent  # Points to release/ folder

# Mod configurations
MODS = [
    {
        "name": "LoreNarratorMod",
        "enabled": True,
    },
    # Add more mods here as needed
    # {
    #     "name": "YourModName",
    #     "enabled": True,
    # },
]


def ensure_directory(path: Path) -> None:
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


def copy_pak_files(mod_name: str) -> bool:
    """
    Copy .pak, .ucas, and .utoc files for the specified mod.
    
    Args:
        mod_name: Name of the mod to copy
        
    Returns:
        True if successful, False otherwise
    """
    source_dir = GAME_BASE_PATH / "Content" / "Paks" / "LogicMods"
    dest_dir = RELEASE_BASE_PATH / mod_name / "RSDragonwilds" / "Content" / "Paks" / "LogicMods"
    
    print(f"  Copying PAK files for {mod_name}...")
    print(f"    Source: {source_dir}")
    print(f"    Dest:   {dest_dir}")
    
    if not source_dir.exists():
        print(f"    ⚠ Warning: Source directory does not exist: {source_dir}")
        return False
    
    # Ensure destination directory exists
    ensure_directory(dest_dir)
    
    # Copy all files matching the mod name pattern
    extensions = [".pak", ".ucas", ".utoc"]
    files_copied = 0
    
    for ext in extensions:
        pattern = f"{mod_name}{ext}"
        source_file = source_dir / pattern
        
        if source_file.exists():
            dest_file = dest_dir / pattern
            shutil.copy2(source_file, dest_file)
            print(f"    ✓ Copied: {pattern}")
            files_copied += 1
        else:
            print(f"    ⚠ Not found: {pattern}")
    
    return files_copied > 0


def copy_ue4ss_mod_folder(mod_name: str) -> bool:
    """
    Copy the complete UE4SS mod folder with all its contents.
    
    Args:
        mod_name: Name of the mod to copy
        
    Returns:
        True if successful, False otherwise
    """
    source_dir = GAME_BASE_PATH / "Binaries" / "Win64" / "ue4ss" / "Mods" / mod_name
    dest_dir = RELEASE_BASE_PATH / mod_name / "RSDragonwilds" / "Binaries" / "Win64" / "ue4ss" / "Mods" / mod_name
    
    print(f"  Copying UE4SS mod folder for {mod_name}...")
    print(f"    Source: {source_dir}")
    print(f"    Dest:   {dest_dir}")
    
    if not source_dir.exists():
        print(f"    ⚠ Warning: Source directory does not exist: {source_dir}")
        return False
    
    # Remove existing destination folder if it exists
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
        print(f"    ℹ Removed existing destination folder")
    
    # Copy entire directory tree
    shutil.copytree(source_dir, dest_dir)
    
    # Remove settings.lua from Scripts/ folder if present
    settings_file = dest_dir / "Scripts" / "settings.lua"
    if settings_file.exists():
        settings_file.unlink()
        print(f"    ✓ Removed settings.lua from Scripts/ folder")
    
    # Count files copied
    file_count = sum(1 for _ in dest_dir.rglob("*") if _.is_file())
    print(f"    ✓ Copied {file_count} file(s) from UE4SS mod folder")
    
    return True


def process_mod(mod_config: Dict) -> bool:
    """
    Process a single mod configuration.
    
    Args:
        mod_config: Dictionary containing mod configuration
        
    Returns:
        True if successful, False otherwise
    """
    mod_name = mod_config["name"]
    
    print(f"\nProcessing mod: {mod_name}")
    print("=" * 60)
    
    pak_success = copy_pak_files(mod_name)
    ue4ss_success = copy_ue4ss_mod_folder(mod_name)
    
    success = pak_success or ue4ss_success
    
    if success:
        print(f"  ✓ {mod_name} processed successfully")
    else:
        print(f"  ✗ {mod_name} failed - no files copied")
    
    return success


def main():
    """Main entry point for the script."""
    print("RSDragonwilds Mod Release Builder")
    print("=" * 60)
    print(f"Game path: {GAME_BASE_PATH}")
    print(f"Release path: {RELEASE_BASE_PATH}")
    print()
    
    if not GAME_BASE_PATH.exists():
        print(f"✗ Error: Game installation not found at {GAME_BASE_PATH}")
        print("  Please update GAME_BASE_PATH in the script.")
        return 1
    
    # Process enabled mods
    enabled_mods = [mod for mod in MODS if mod.get("enabled", True)]
    
    if not enabled_mods:
        print("No enabled mods to process.")
        return 0
    
    print(f"Found {len(enabled_mods)} enabled mod(s) to process\n")
    
    results = []
    for mod in enabled_mods:
        success = process_mod(mod)
        results.append((mod["name"], success))
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    for mod_name, success in results:
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"  {status}: {mod_name}")
    
    failed_count = sum(1 for _, success in results if not success)
    
    print()
    if failed_count == 0:
        print("All mods processed successfully!")
        return 0
    else:
        print(f"{failed_count} mod(s) failed to process.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
