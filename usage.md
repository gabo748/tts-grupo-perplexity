# Usage Guide

This guide provides a step-by-step walkthrough of how to use the Text-to-Speech and Translation CLI tool.

## 1. Prerequisites

Before you begin, ensure you have the following:

-   Python 3.10 or higher installed.
-   A valid OpenAI API key.

Create a file named `.env` in the root of the project directory and add your API key to it like this:

```
OPENAI_API_KEY="sk-..."
```

## 2. Installation

Install the necessary Python packages by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## 3. Step-by-Step Example

Here is the sequence of commands that were run to generate and translate your audio.

### Step 1: Create the Input Text File

First, we created a text file named `intro_ia.txt` with the following content:

```text
Este es un texto creado para la materia de Introducción a la inteligencia artificial usando Open AI Whisper
```

### Step 2: Generate Speech from Text

Next, we used the `tts` command to convert the text file into a Spanish audio file named `intro_ia.mp3`.

```bash
python -m src.py_speech_translator.main tts --input intro_ia.txt --lang es --output intro_ia.mp3
```

### Step 3: Translate the Audio to English

Finally, we used the `translate` command to take the generated `intro_ia.mp3` audio file and translate it into English, creating `intro_ia_en.mp3`.

```bash
python -m src.py_speech_translator.main translate --input intro_ia.mp3 --target-lang en --output intro_ia_en.mp3
```
