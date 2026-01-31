# Coqui XTTS‑v2 – Local Installation Guide

This document describes how to install **Coqui TTS (XTTS‑v2)** with voice cloning support on a fresh machine. The steps are reproducible and tested on Windows; Linux/macOS are analogous.

The guide intentionally pins certain versions to avoid known incompatibilities (notably PyTorch ≥2.6).

---

## Goal

- Local text‑to‑speech using **XTTS‑v2**
- Voice cloning via reference audio (`speaker_wav`)
- CPU or CUDA GPU support
- Reproducible setup across machines

---

## 1. System Requirements

### Python

- **Python 3.10 or 3.11** (recommended)

Verify:

```bash
python --version
```

---

### FFmpeg (Required)

XTTS relies on FFmpeg for audio decoding.

1. Download from: https://ffmpeg.org/
2. Add `ffmpeg/bin` to your system `PATH`
3. Verify:

```bash
ffmpeg -version
```

---

### GPU (Optional)

- NVIDIA GPU with recent drivers
- CUDA is optional; XTTS works on CPU (slower)

---

## 2. Project Setup

Create a project directory and virtual environment using **uv**:

```bash
mkdir tts
cd tts
uv venv
```

Activate the environment:

**Windows**
```powershell
.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

---

## 3. Install PyTorch (Critical Version Pin)

⚠️ **Important**: PyTorch ≥2.6 breaks Coqui XTTS checkpoint loading due to `weights_only=True` being the default.

Always install **torch < 2.6**.

### CPU‑only

```bash
uv pip install "torch<2.6" torchaudio
```

### CUDA example (CUDA 12.1)

```bash
uv pip install "torch<2.6" torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Verify:

```bash
python - <<EOF
import torch
print(torch.__version__)
print("CUDA available:", torch.cuda.is_available())
EOF
```

---

## 4. Install Coqui TTS

```bash
uv pip install TTS
```

This installs:

- Coqui TTS API
- XTTS‑v2 model support
- Transformers + audio dependencies

---

## 5. PyTorch Safe Globals (Recommended)

To avoid checkpoint deserialization errors, register XTTS config classes explicitly.

Add this **once** at the top of your TTS scripts:

```python
import torch

from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig

torch.serialization.add_safe_globals([
    XttsConfig,
    XttsAudioConfig,
    XttsArgs,
    BaseDatasetConfig,
])
```

This is defensive and forward‑compatible.

---

## 6. Minimal Working Voice‑Cloning Example

```python
import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

tts.tts_to_file(
    text="This is a cloned voice speaking.",
    speaker_wav="voices/example.wav",
    language="en",
    file_path="out.wav",
)
```

### Key Concept

XTTS‑v2 **does not store speakers by name**.

- There is no speaker database
- No persistent embeddings by default
- **Reusing a voice = reusing the same `speaker_wav`**

The reference audio *is* the speaker identity.

---

## 7. Reference Audio Requirements

For best results, `speaker_wav` should be:

- WAV or FLAC
- Mono (preferred)
- 16–48 kHz
- 5–30 seconds duration
- Clean speech (no music, reverb, or background noise)

Poor reference audio produces unstable speaker embeddings.

---

## 8. Long Text Support

XTTS‑v2 natively supports long input text:

- Automatic sentence splitting
- Internal streaming
- No extra configuration required

You can safely pass thousands of characters.

---

## 9. Optional Parameters

Example:

```python
tts.tts_to_file(
    text="Hello there.",
    speaker_wav="voices/example.wav",
    language="en",
    speed=0.9,
)
```

### Emotion Parameter

Although the API exposes `emotion`, **XTTS‑v2 does not meaningfully support emotion control**, especially for cloned voices.

- Emotion is implicitly derived from the reference audio
- Explicit `emotion=` values are ignored or weakly applied

---

## 10. Reproducing This Setup on Another PC

Checklist:

1. Install Python 3.10 or 3.11
2. Install FFmpeg and add to PATH
3. Create venv with `uv`
4. Install `torch<2.6` + `torchaudio`
5. `uv pip install TTS`
6. Use `speaker_wav` for voice reuse

---

## 11. Troubleshooting

### `_pickle.UnpicklingError` or `weights_only` errors

- Torch version is too new
- Reinstall with:

```bash
uv pip install "torch<2.6" --force-reinstall
```

---

## Notes

XTTS‑v2 is a **conditional generative model**, not a traditional TTS voice registry.

There are no speakers — only waveforms conditioning latent space.

Once that is understood, the system becomes predictable and stable.

