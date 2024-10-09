import os
import librosa
import numpy as np
from pydub import AudioSegment

def load_audio(file_path, sr=16000):
    """
    Loads an audio file and returns the audio time series and sample rate.
    """
    audio, sample_rate = librosa.load(file_path, sr=sr)
    return audio, sample_rate

def save_audio(audio, sample_rate, file_path):
    """
    Saves the audio time series to a file.
    """
    librosa.output.write_wav(file_path, audio, sample_rate)

def convert_mp3_to_wav(mp3_path, wav_path):
    """
    Converts an MP3 file to WAV format.
    """
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")
