from pathlib import Path
from .services import openai_service

def audio_translation(input_path: str, target_lang: str, output_path: str):
    """
    Translates an audio file to a target language.
    """
    try:
        print(f"Translating audio from '{input_path}' to '{target_lang}'...")
        
        if not output_path:
            p = Path(input_path)
            output_path = f"{p.stem}_{target_lang}.mp3"

        openai_service.translate_audio(input_path, target_lang, output_path)
        print(f"Successfully created translated audio file at '{output_path}'")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
