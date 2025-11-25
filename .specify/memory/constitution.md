<!--
Sync Impact Report:
- Version: 1.0.1
- Changes: Removed the Development Workflow section requiring TDD.
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md (No changes needed)
  - ✅ .specify/templates/spec-template.md (No changes needed)
  - ✅ .specify/templates/tasks-template.md (No changes needed)
-->

# py-speech-translator Constitution

## Core Principles

### I. Clarity and Focus
The project will be a command-line tool, avoiding the complexity of a graphical user interface to ensure simplicity and maintainability.

### II. Core Technologies
The tool will be built using Python and leverage the OpenAI Whisper model for its core functionalities of text-to-speech and translation.

### III. Language Support
The initial version will exclusively support English and Spanish for both text-to-speech and translation, with the potential to expand in the future.

### IV. Cost-Effectiveness
The project will prioritize using the most cost-effective tiers of external services. An investigation into using the user's existing paid API key within these constraints is a priority.

### V. Modular Functionality
The tool will have distinct actions for (1) generating audio from text and (2) translating previously generated audio, allowing for clear and separate use cases.

## Governance

All pull requests and reviews must verify compliance with this constitution. Any deviation must be justified and documented.

**Version**: 1.0.1 | **Ratified**: 2025-11-24 | **Last Amended**: 2025-11-24