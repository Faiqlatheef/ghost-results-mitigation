import noisereduce as nr
import numpy as np
from utils import load_audio, save_audio

def reduce_noise(input_audio_path, output_audio_path):
    """
    Reduces background noise from the input audio file and saves the cleaned audio.
    """
    audio, sr = load_audio(input_audio_path)
    reduced_noise = nr.reduce_noise(y=audio, sr=sr)
    save_audio(reduced_noise, sr, output_audio_path)
    return output_audio_path
