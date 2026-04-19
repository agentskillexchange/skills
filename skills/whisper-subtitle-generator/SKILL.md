---
title: "Whisper Subtitle Generator"
description: "The Whisper Subtitle Generator skill combines OpenAI Whisper speech recognition with professional subtitle formatting to produce broadcast-ready caption files. It supports both the Whisper API and local whisper.cpp inference for flexible deployment options. The skill processes audio through the Whisper API transcriptions endpoint with word-level timestamp granularity, enabling precise subtitle synchronization. It formats output into industry-standard formats: SRT (SubRip) for universal compatibility, WebVTT for HTML5 video players with CSS styling support, and ASS (Advanced SubStation Alpha) for complex typographical layouts. Line-breaking algorithms respect maximum characters-per-line and reading-speed constraints (typically 20 characters per second) to ensure viewer comfort. Speaker diarization integrates with pyannote.audio to identify and label different speakers, creating color-coded or prefixed subtitle tracks for multi-speaker content like interviews and panel discussions. The skill handles pre-processing through pydub for audio segmentation and format normalization before transcription. Post-processing includes punctuation restoration, profanity filtering via custom word lists, and translation through the Whisper translation endpoint. Batch processing supports entire video libraries with progress tracking and error recovery for interrupted jobs."
source: "https://github.com/openai/whisper"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97775
---

# Whisper Subtitle Generator

The Whisper Subtitle Generator skill combines OpenAI Whisper speech recognition with professional subtitle formatting to produce broadcast-ready caption files. It supports both the Whisper API and local whisper.cpp inference for flexible deployment options. The skill processes audio through the Whisper API transcriptions endpoint with word-level timestamp granularity, enabling precise subtitle synchronization. It formats output into industry-standard formats: SRT (SubRip) for universal compatibility, WebVTT for HTML5 video players with CSS styling support, and ASS (Advanced SubStation Alpha) for complex typographical layouts. Line-breaking algorithms respect maximum characters-per-line and reading-speed constraints (typically 20 characters per second) to ensure viewer comfort. Speaker diarization integrates with pyannote.audio to identify and label different speakers, creating color-coded or prefixed subtitle tracks for multi-speaker content like interviews and panel discussions. The skill handles pre-processing through pydub for audio segmentation and format normalization before transcription. Post-processing includes punctuation restoration, profanity filtering via custom word lists, and translation through the Whisper translation endpoint. Batch processing supports entire video libraries with progress tracking and error recovery for interrupted jobs.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-subtitle-generator/)
