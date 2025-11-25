from pathlib import Path
from .services import openai_service

def text_to_speech(input_path: str, lang: str, output_path: str):
    """
    Converts text from a file to speech and saves it as an audio file.
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        if not text.strip():
            print("Error: Input file is empty.")
            return

        print(f"Generating audio for text from '{input_path}'...")
        openai_service.generate_tts(text, lang, output_path)
        print(f"Successfully created audio file at '{output_path}'")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

