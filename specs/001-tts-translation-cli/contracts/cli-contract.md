# CLI Contract

**Date**: 2025-11-24
**Feature**: [Text-to-Speech and Translation CLI](../spec.md)

## Overview

This document defines the command-line interface for the `py-speech-translator` tool.

## Commands

### `tts`

Performs text-to-speech conversion.

**Usage**:
```bash
py-speech-translator tts [OPTIONS]
```

**Options**:

| Option | Required | Type | Description |
| :--- | :--- | :--- | :--- |
| `--input <path>` | Yes | File Path | Path to the input text file (`.txt`). |
| `--lang <lang>` | Yes | String | Source language of the text. Supported: `en`, `es`. |
| `--output <path>` | No | File Path | Path to save the output audio file. Defaults to `output.mp3` in the current directory. |

---

### `translate`

Translates speech from an audio file to a target language.

**Usage**:
```bash
py-speech-translator translate [OPTIONS]
```

**Options**:

| Option | Required | Type | Description |
| :--- | :--- | :--- | :--- |
| `--input <path>` | Yes | File Path | Path to the input audio file. |
| `--target-lang <lang>` | Yes | String | The language to translate the audio to. Supported: `en`, `es`. |
| `--output <path>` | No | File Path | Path to save the translated audio file. Defaults to `<input_name>_<lang>.mp3`. |
