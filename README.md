# RSDragonwilds Lore Narrator - Project Overview

## What is This Mod?

The **RSDragonwilds Lore Narrator** is an immersive audio narration mod for RuneScape that brings the game's rich lore to life through text-to-speech technology. Instead of reading static text from lore books, players can now listen to voice-acted narrations while playing the game.

### The Problem It Solves

RuneScape's lore books contain deep, engaging storylines and world-building—but reading them all requires significant time investment away from gameplay. This mod allows players to:
- **Stay immersed** in the game world while learning its lore
- **Multitask** by listening to narrations while skilling or questing
- **Enjoy content** without the time barrier of reading lengthy text

## How It Works

The mod uses an **AI-powered Text-to-Speech pipeline** built on:

1. **Voice Cloning Technology** - Coqui-AI XTTS-v2 voice synthesis engine
2. **Custom Voice Models** - Voice samples cloned from high-quality open-source audio
3. **UE4SS Modding Framework** - Integrates with RuneScape's Unreal Engine 4 through scripting
4. **Pre-Generated Audio Assets** - Narrations pre-recorded and packaged with the mod

### Architecture

```
Game (RuneScape UE4 Engine)
    ↓
UE4SS Runtime (Mod Loader)
    ↓
Lua Scripts (Game Hooks)
    ├── lorefinder.lua - Detects lore book interactions
    └── loreplayer.lua - Triggers audio playback
    ↓
Audio System
    └── Pre-narrated .WAV files (packaged in mod)
```

## Key Features

### Implemented Features
- **Audio Narration (Base Areas)** - Comprehensive coverage of base game lore books
- **Partial Fellhollow Coverage** - Some dungeon lore books narrated (expanded regularly)
- **Multiple Voice Options**:
  - **MedievalSpeech** - Male voice with historical tone
  - **Asya Anara** - Female voice alternative

### Planned Features
- **Audio Queue Management** - Prevent overlapping playback when visiting multiple locations rapidly
- **Enhanced User Control** - Better management of simultaneous audio events

### Possible Future Enhancements
- **Multi-Language Support** - Narrations in different languages
- **Additional Voices** - More voice variety for player choice
- **Proximity Triggering** - Play lore audio when near books without opening them
- **Configurable Settings** - Adjustable playback distance and parameters
- **Playback Controls** - Replay, pause, and continue functionality
- **Progress Indicator** - Visual UI showing narration progress (0-100%)

## Project Structure

```
RSDragonwilds-Lorebook-Narrator/
├── src/
│   ├── narration/           # TTS and voice processing pipeline
│   │   ├── coqui-ai/        # Voice cloning implementation
│   │   │   ├── clone-voice.py     # Voice model generation
│   │   │   ├── voices/             # Voice source data
│   │   │   └── output/             # Generated narrations
│   │   ├── narrator_repeat.json    # Narration configuration
│   │   └── install.md              # Setup instructions
│   │
│   ├── mods/               # Mod implementation (Lua)
│   │   ├── lorefinder.lua      # Lore book detection
│   │   └── loreplayer.lua      # Audio playback logic
│   │
│   ├── mining/             # Data extraction tools
│   │   └── extract-locations/  # Lore data processing
│   │
│   └── util/               # Utility scripts
│       └── *.py            # Coordinate mapping, validation
│
├── output/
│   ├── make-release.py     # Release packaging script
│   └── LoreNarratorMod/    # Packaged mod distribution
│
└── doc/
    └── images/             # Documentation images
```

## Technical Details

### Voice Cloning Pipeline

The mod uses a sophisticated voice synthesis workflow:

1. **Source Audio Selection** - Curated voice samples (Medieval historical audio, professional voice actors)
2. **Model Training** - Coqui-AI XTTS-v2 trains from voice samples
3. **Text-to-Speech Synthesis** - Lore text converted to audio using cloned voice
4. **Audio Processing** - Quality normalization and optimization
5. **Asset Packaging** - Audio files bundled into mod distribution

### Supported Voice Sources

The mod currently includes voice models from:
- **MedievalSpeech** (tekgnosis, CC0 licensed)
- **Asya Anara** (Coqui HuggingFace model)
- Additional custom voices can be added via the pipeline

### Lore Data Processing

- **Automated Extraction** - Scripts pull lore text from game assets
- **Location Mapping** - Links narrations to specific in-game locations
- **Configuration Management** - `narrator_repeat.json` defines narration triggers

## Development Workflow

### Adding New Narrations

1. **Extract Lore Data** - Run `extract-lore-data.bat` to pull fresh lore from game
2. **Generate Audio** - Use `clone-voice.py` to synthesize narrations
3. **Package Release** - Run `make-release.py` to create distributable mod
4. **Test in Game** - Verify narration playback via UE4SS

### Building & Deployment

- **Build Script** - `src/unreal/RSDragonwilds 5.4/build.bat`
- **Clone Script** - `clone-voice.bat` for rapid voice model generation
- **Release Creation** - Package mod for distribution via make-release.py

## Dependencies

### Runtime Requirements
- **UE4SS** - Unreal Engine 4 modding framework
- **Lua Runtime** - For mod scripting hooks
- **RuneScape Game** - Obviously!

### Development Requirements
- **Coqui-AI XTTS-v2** - Voice synthesis engine
- **Python 3.x** - For data processing and TTS pipeline
- **Unreal Engine 4** - For game mod integration

## Use Cases

### For Players
- **Lore Enthusiasts** - Experience the story without reading commitment
- **Accessibility** - Audio-only consumption for different learning styles
- **Immersion** - Hear the world while actively playing
- **Multitasking** - Learn lore while skilling or adventuring

### For Developers
- **Mod Template** - Reference implementation for UE4SS + TTS mods
- **Voice Synthesis** - Example of Coqui-AI voice cloning in practice
- **Data Mining** - Extraction and mapping of game lore assets
- **Automation** - Scripted release and packaging workflow

## Credits & Attribution

### Technology
- **Coqui-AI XTTS-v2** - Voice synthesis engine (Apache 2.0 license)
- **UE4SS** - Unreal modding framework
- **Lua** - Mod scripting language

### Voice Samples & Models
- **MedievalSpeech** - tekgnosis (https://freesound.org/s/144862/, CC0 License)
- **Asya Anara** - Coqui HuggingFace repository
- Additional voice contributors acknowledged in release notes

### Project Team
Built by me, Z0WX1L, just for the fun of it.

## Getting Started

- **Users**: See [Installation Guide](README.md#installation)
- **Developers**: Review [Development Setup](src/narration/install.md)
- **Contributors**: Check individual README files in src/ subdirectories

## License

See [LICENSE](LICENSE) file for details.

---

**Last Updated**: 2026-08-16  
**Project Status**: Active Development
