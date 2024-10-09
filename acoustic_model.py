import speech_recognition as sr

def transcribe_audio(audio_path):
    """
    Transcribes the given audio file using SpeechRecognition library.
    Returns the transcription text and confidence score.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        # Using Google's Web Speech API for demonstration
        transcription = recognizer.recognize_google(audio, show_all=True)
        if 'alternative' in transcription:
            best_transcription = transcription['alternative'][0]['transcript']
            confidence = transcription['alternative'][0].get('confidence', 1.0)
        else:
            best_transcription = ""
            confidence = 0.0
        return best_transcription, confidence
    except sr.UnknownValueError:
        return "", 0.0
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "", 0.0
