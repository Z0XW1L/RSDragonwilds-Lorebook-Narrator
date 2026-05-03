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

# Extract speaker name from speaker_wav
speaker_wav = "./src/narration/coqui-ai/voices/144862__tekgnosis__medievalspeech.wav"
speaker = speaker_wav.split('/')[-1].replace('.wav', '')

# Create output directory
output_dir = f"./src/narration/coqui-ai/output/{speaker}/repeat"
os.makedirs(output_dir, exist_ok=True)

# Get JSON input from narrators.json file
with open("./src/narration/narrator_repeat.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Generate audio for each entry
for key, text in data.items():
    if not key:
        continue
    file_path = f"{output_dir}/{key}.wav"
    
    # Skip if output already exists
    if os.path.exists(file_path):
        print(f"Skipped {file_path} (already exists)")
        continue
    
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        # speaker=speaker, # Asya Anara, Gilberto Mathias, Damian Black +
        language="en",
        speed=1.0,
        file_path=file_path,
    )
    print(f"Generated {file_path}")
