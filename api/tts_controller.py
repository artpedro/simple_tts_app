from TTS.api import TTS
import torch
import numpy as np
import random

def generate_audio(text, speaker, language,output_path ,seed=12):
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False 

    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

    print(f"Generating audio for: {text}")
    print(f"Speaker: {speaker}, Language: {language}")
    print(f"Saving to: {output_path}")
    tts.tts_to_file(
        text=text,
        file_path=output_path,
        speaker=speaker,
        language=language,
        split_sentences=True
    )
    return 1