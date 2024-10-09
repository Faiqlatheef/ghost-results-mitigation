def handle_confidence(transcription, confidence, threshold=0.6):
    """
    Checks the confidence score and decides whether to accept the transcription
    or flag it for review.
    """
    if confidence < threshold:
        return "Transcription is uncertain. Please review the audio."
    else:
        return transcription
