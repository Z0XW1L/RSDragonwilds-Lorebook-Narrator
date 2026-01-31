import torch
import json
import sys
import os
import nltk # Use nltk to split sentences properly

from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig
from nltk.tokenize import sent_tokenize
from pydub import AudioSegment # To merge audio files

torch.serialization.add_safe_globals([
    XttsConfig,
    XttsAudioConfig,
    XttsArgs,
    BaseDatasetConfig,
])

from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

nltk.download('punkt')

text = "16. Die große Lehrrede von der vollkommenen ErlöschungBeiseite stehend, Ananda, sagte Mara, der Böse, zu mir Folgendes:‚Möge der verehrungswürdige Erhabene jetzt in das vollkommene Er-löschen eintreten, möge der Wohlgegangene jetzt in das vollkommeneErlöschen eintreten, jetzt ist die Zeit, dass der verehrungswürdigeErhabene vollkommen erlischt. Denn dieses sagte ja der verehrungs-würdige Erhabene: «Nicht werde ich, Böser, vollkommen erlöschen,bis nicht meine Mönche Hörer sein werden, gebildet, gezügelt, furcht-los, kundig, Träger der Lehre, die Lehre kennend und befolgend, mitangemessener Vorgehensweise nach der Lehre handelnd."
sentences = sent_tokenize(text)

combined_audio = AudioSegment.empty()
print(tts.speakers)

for i, sentence in enumerate(sentences):
    temp_path = f"chunk_{i}.wav"
    # Generate each sentence separately
    tts.tts_to_file(text=sentence, speaker="Damjan Chapman", language="de", file_path=temp_path)
    
    # Add to the master file
    segment = AudioSegment.from_wav(temp_path)
    combined_audio += segment
    
combined_audio.export("full_narration.wav", format="wav")