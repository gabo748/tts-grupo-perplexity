import click
from .tts import text_to_speech
from .translation import audio_translation

@click.group()
def cli():
    """
    A CLI tool for text-to-speech and audio translation using OpenAI.
    """
    pass

@cli.command()
@click.option('--input', 'input_path', required=True, type=click.Path(exists=True, dir_okay=False), help='Path to the input text file.')
@click.option('--lang', required=True, type=click.Choice(['en', 'es'], case_sensitive=False), help='Source language of the text.')
@click.option('--output', 'output_path', default='output.mp3', type=click.Path(), help='Path to save the output audio file.')
def tts(input_path, lang, output_path):
    """Performs text-to-speech conversion."""
    text_to_speech(input_path, lang, output_path)

@cli.command()
@click.option('--input', 'input_path', required=True, type=click.Path(exists=True, dir_okay=False), help='Path to the input audio file.')
@click.option('--target-lang', required=True, type=click.Choice(['en', 'es'], case_sensitive=False), help='The language to translate the audio to.')
@click.option('--output', 'output_path', default=None, type=click.Path(), help='Path to save the translated audio file.')
def translate(input_path, target_lang, output_path):
    """Translates an audio file to a target language."""
    audio_translation(input_path, target_lang, output_path)

if __name__ == '__main__':
    cli()
