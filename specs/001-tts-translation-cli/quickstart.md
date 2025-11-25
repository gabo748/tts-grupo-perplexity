# Quickstart: Text-to-Speech and Translation CLI

**Feature**: [Text-to-Speech and Translation CLI](./spec.md)

## 1. Setup

### Prerequisites

-   Python 3.10+
-   An OpenAI API key

### Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    # This step is just for context; you are already in the project.
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create a virtual environment**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key**:
    -   Create a file named `.env` in the root of the project.
    -   Add your OpenAI API key to it:
        ```env
        OPENAI_API_KEY="sk-..."
        ```

## 2. Usage

The main tool is `py-speech-translator`. It has two primary commands: `tts` and `translate`.

### Text-to-Speech (`tts`)

Converts a text file to an audio file.

**Example**:
1.  Create a file `hello.txt` with the content: `Hello world, this is a test.`
2.  Run the command:
    ```bash
    python src/py_speech_translator/main.py tts --input hello.txt --lang en --output hello.mp3
    ```
3.  This will create a `hello.mp3` file in your current directory.

### Translation (`translate`)

Translates an audio file into a different language.

**Example**:
1.  Using the `hello.mp3` file from the previous step.
2.  Run the command to translate it to Spanish:
    ```bash
    python src/py_speech_translator/main.py translate --input hello.mp3 --target-lang es --output hello_es.mp3
    ```
3.  This will create a `hello_es.mp3` file containing the Spanish translation.
