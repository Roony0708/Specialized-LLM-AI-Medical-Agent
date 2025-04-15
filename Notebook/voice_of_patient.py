import os
import logging
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import which
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Explicitly tell Pydub where ffmpeg is
AudioSegment.converter = which("ffmpeg") or r"C:\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"  

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Record audio from the microphone and save it as an MP3 file.

    Args:
        file_path (str): Path to save the recorded audio file.
        timeout (int): Max time to wait for speech (in seconds).
        phrase_time_limit (int): Max duration of speech (in seconds).
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")

            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            # Convert audio to MP3 using Pydub
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Run it
audio_filepath="patient_voice_test.mp3"
record_audio(file_path=audio_filepath)


#Step2: Setup Speech to text–STT–model for transcription
import os
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
stt_model="whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)

    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )

    return transcription.text