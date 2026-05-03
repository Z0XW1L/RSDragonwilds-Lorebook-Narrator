import torch
import json
import sys
import os

from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig

torch.serialization.add_safe_globals([
    XttsConfig,
    XttsAudioConfig,
    XttsArgs,
    BaseDatasetConfig,
])

from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
print(tts.speakers)
print("\n")

# Define speakers
speakers = [
    {"type": "wav", "value": "./src/narration/coqui-ai/voices/144862__tekgnosis__medievalspeech.wav", "name": "144862__tekgnosis__medievalspeech"},
    {"type": "builtin", "value": "Asya Anara", "name": "Asya Anara"},
]

# Process each speaker
for speaker in speakers:
    speaker_name = speaker["name"]
    
    # Narration
    output_dir = f"./src/narration/coqui-ai/output/{speaker_name}/narration"
    os.makedirs(output_dir, exist_ok=True)
    
    with open("./src/mining/extract-locations/lore-data-output.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for item in data:
        key = item.get("key", "")
        text = item.get("text", "")
        if not key or not text:
            continue
        file_path = f"{output_dir}/{key}.wav"
        
        if os.path.exists(file_path):
            print(f"Skipped {file_path} (already exists)")
            continue
        
        if speaker["type"] == "wav":
            tts.tts_to_file(
                text=text,
                speaker_wav=speaker["value"],
                language="en",
                speed=1.0,
                file_path=file_path,
            )
        else:
            tts.tts_to_file(
                text=text,
                speaker=speaker["value"],
                language="en",
                speed=1.0,
                file_path=file_path,
            )
        print(f"Generated {file_path}")
    
    # Repeat
    output_dir_repeat = f"./src/narration/coqui-ai/output/{speaker_name}/repeat"
    os.makedirs(output_dir_repeat, exist_ok=True)
    
    with open("./src/narration/narrator_repeat.json", "r", encoding="utf-8") as f:
        data_repeat = json.load(f)
    
    for key, text in data_repeat.items():
        if not key:
            continue
        file_path = f"{output_dir_repeat}/{key}.wav"
        
        if os.path.exists(file_path):
            print(f"Skipped {file_path} (already exists)")
            continue
        
        if speaker["type"] == "wav":
            tts.tts_to_file(
                text=text,
                speaker_wav=speaker["value"],
                language="en",
                speed=1.0,
                file_path=file_path,
            )
        else:
            tts.tts_to_file(
                text=text,
                speaker=speaker["value"],
                language="en",
                speed=1.0,
                file_path=file_path,
            )
        print(f"Generated {file_path}")
