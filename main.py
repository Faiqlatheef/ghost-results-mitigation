import argparse
from noise_reduction import reduce_noise
from acoustic_model import transcribe_audio
from language_model_integration import correct_transcription
from confidence_scoring import handle_confidence
from utils import convert_mp3_to_wav

def process_audio(input_path, output_path):
    # Convert MP3 to WAV if necessary
    if input_path.endswith('.mp3'):
        wav_path = 'temp.wav'
        convert_mp3_to_wav(input_path, wav_path)
    else:
        wav_path = input_path

    # Step 1: Noise Reduction
    cleaned_audio_path = 'cleaned_audio.wav'
    reduce_noise(wav_path, cleaned_audio_path)

    # Step 2: Acoustic Model Transcription
    transcription, confidence = transcribe_audio(cleaned_audio_path)

    # Step 3: Language Model Integration
    corrected_transcription = correct_transcription(transcription)

    # Step 4: Confidence Scoring
    final_output = handle_confidence(corrected_transcription, confidence)

    # Save the final transcription
    with open(output_path, 'w') as f:
        f.write(final_output)
    
    print(f"Transcription saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mitigate Ghost Results in Speech-to-Text")
    parser.add_argument('--input', type=str, required=True, help='Path to input audio file (wav or mp3)')
    parser.add_argument('--output', type=str, required=True, help='Path to save transcription output')
    args = parser.parse_args()

    process_audio(args.input, args.output)
