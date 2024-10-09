# Ghost Results Mitigation in Speech-to-Text Systems

## Overview

This project implements techniques to reduce ghost results in speech-to-text (STT) transcriptions by integrating Noise Reduction, Acoustic Model Enhancement, Language Model Integration, and Confidence Scoring.

## Features

- **Noise Reduction**: Filters out background noise to enhance speech clarity.
- **Acoustic Model Enhancement**: Utilizes robust speech recognition models trained on diverse datasets.
- **Language Model Integration**: Employs advanced language models to improve contextual understanding and transcription accuracy.
- **Confidence Scoring**: Assigns confidence levels to transcriptions, enabling the filtering of low-confidence segments.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Faiqlatheef/ghost-results-mitigation.git
   cd ghost-results-mitigation

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install Dependencies**
   
   ```bash
   pip install -r requirements.txt

4. **Prepare Audio Files**

   Ensure your audio files are in WAV format. If not, convert them using the provided utility.

5. **Run the Main Script**
    ```bash
    python main.py --input path_to_your_audio_file.wav
