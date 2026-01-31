# RSDragonwilds Lore Narrator

## Overview

A RuneScape: Dragonwilds mod that provides voice narration for lore locations throughout the game world. The narrator reads contextual lore and background information when players visit specific in-game locations, creating an immersive storytelling experience.

> **Attention:** As of now, the narration does not include Lorebooks in Fellhollow as I have not explored this area yet and did not want to spoil the fun for me. As soon as my character is able to advance into this territory, the narration will be added!

> **Attention 2:** I did not extensively test if the narration matches with the actual lorebooks. So it could be that there are some slight mistakes. If you find any, please tell me and I will fix it.

## Installation

1. Download the newest `RSDragonwilds` release of this repository
2. Extract `RSDragonwilds.zip` to your RuneScape game installation directory
3. Edit your `RSDragonwilds\Binaries\Win64\ue4ss\Mods\mods.json` settings file and add the following configuration to the end of the array:
   ```json
   {
       "mod_name": "LoreNarratorMod",
       "mod_enabled": true
   }
   ```
4. Edit your `RSDragonwilds\Binaries\Win64\ue4ss\Mods\mods.txt` settings file and add the following configuration to the end of the file:
   ```ini
   LoreNarratorMod : 1
   ```
5. Launch the game and the narrator will begin playing contextual audio at designated lore locations

## Features

- **Location-based narration** - Audio plays automatically when you visit 30 distinct lore locations
- **High-quality voice acting** - Professional English narration from various voice actors
- **Immersive storytelling** - Lore content expands on the game's world-building and character backgrounds

## Planned Features

- **Audio queue management** - Prevent overlapping audio playback when visiting multiple locations in quick succession
- **Proximity Based Playing** - Play the lore when being near to a lore book without opening it
- **More Languages** - Mod in different languages
- **More Voices** - Adding more voice choices for narration
- **Additional lore locations**
- **Additional Settings**

## Credits

- The narration has been done with [coqui-ai-TTS](https://github.com/coqui-ai/TTS)
- The narration is based on a voice clone from [NPC Faras (Greetings)](https://freesound.org/sounds/731604/)
