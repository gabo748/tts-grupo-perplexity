# Tasks: Text-to-Speech and Translation CLI

**Input**: Design documents from `/specs/001-tts-translation-cli/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/cli-contract.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [X] T001 Create the project directory structure: `src/py_speech_translator/services/`
- [X] T002 Create an empty `requirements.txt` file
- [X] T003 [P] Create a `.env.example` file with the content `OPENAI_API_KEY=""`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

- [X] T004 Populate `requirements.txt` with `openai`, `python-dotenv`, and `click`
- [X] T005 Implement the main CLI group in `src/py_speech_translator/main.py` using `click`
- [X] T006 [P] Create the OpenAI service wrapper in `src/py_speech_translator/services/openai_service.py` to load the API key from the environment

---

## Phase 3: User Story 1 - Generate Speech from Text (Priority: P1) 🎯 MVP

**Goal**: Implement the `tts` command to convert text to an audio file.

**Independent Test**: Run `python src/py_speech_translator/main.py tts --input <file.txt> --lang en` and verify the audio output.

### Implementation for User Story 1

- [X] T007 [US1] Implement the core logic for text-to-speech in `src/py_speech_translator/tts.py`
- [X] T008 [US1] Add the `tts` function to `src/py_speech_translator/services/openai_service.py` to call the OpenAI TTS API
- [X] T009 [US1] Integrate the `tts` command into `src/py_speech_translator/main.py`, connecting the Click command options to the `tts.py` logic

---

## Phase 4: User Story 2 - Translate Audio File (Priority: P2)

**Goal**: Implement the `translate` command to convert an audio file to a different language.

**Independent Test**: Run `python src/py_speech_translator/main.py translate --input <audio.mp3> --target-lang es` and verify the translated audio output.

### Implementation for User Story 2

- [X] T010 [US2] Implement the core logic for audio translation in `src/py_speech_translator/translation.py`
- [X] T011 [US2] Add the `translate` function to `src/py_speech_translator/services/openai_service.py` to call the OpenAI Whisper API for translation
- [X] T012 [US2] Integrate the `translate` command into `src/py_speech_translator/main.py`, connecting the Click command options to the `translation.py` logic

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [X] T013 [P] Implement error handling in `main.py` for file-not-found errors
- [X] T014 [P] Implement error handling in `openai_service.py` for API-related errors (e.g., invalid key, network issues)
- [X] T015 [P] Review and update the `quickstart.md` with final command examples and any setup adjustments

---

## Dependencies & Execution Order

- **Setup (Phase 1)** must be completed before **Foundational (Phase 2)**.
- **Foundational (Phase 2)** must be completed before any user stories can be implemented.
- **User Story 1 (Phase 3)** and **User Story 2 (Phase 4)** can be implemented in parallel after Phase 2 is complete.
- **Polish (Phase 5)** should be done after all user stories are implemented.
