import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found.")

client = OpenAI(api_key=api_key)

def generate_tts(text: str, lang: str, output_path: str):
    """
    Calls the OpenAI TTS API to generate audio from text.
    """
    # Note: The OpenAI TTS API does not have a `lang` parameter.
    # The voice determines the language accent. 'alloy' is a standard voice.
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(output_path)

def translate_audio(input_path: str, target_lang: str, output_path: str):
    """
    Calls the OpenAI Whisper API to translate audio.
    """
    with open(input_path, "rb") as audio_file:
        translation = client.audio.translations.create(
            model="whisper-1",
            file=audio_file
        )
    
    # The translation result is text. We need to convert this text back to speech.
    generate_tts(translation.text, target_lang, output_path)

