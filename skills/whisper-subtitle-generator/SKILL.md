---
title: "Whisper Subtitle Generator"
description: "Generates accurate subtitles and captions using OpenAI Whisper API with word-level timestamps. Outputs SRT, VTT, and ASS formats with configurable line length and speaker diarization via pyannote."
verification: "security_reviewed"
source: "https://github.com/openai/whisper"
category:
  - "Media & Transcription"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97775
---

# Whisper Subtitle Generator

The Whisper Subtitle Generator skill combines OpenAI Whisper speech recognition with professional subtitle formatting to produce broadcast-ready caption files. It supports both the Whisper API and local whisper.cpp inference for flexible deployment options.

The skill processes audio through the Whisper API transcriptions endpoint with word-level timestamp granularity, enabling precise subtitle synchronization. It formats output into industry-standard formats: SRT (SubRip) for universal compatibility, WebVTT for HTML5 video players with CSS styling support, and ASS (Advanced SubStation Alpha) for complex typographical layouts. Line-breaking algorithms respect maximum characters-per-line and reading-speed constraints (typically 20 characters per second) to ensure viewer comfort.

Speaker diarization integrates with pyannote.audio to identify and label different speakers, creating color-coded or prefixed subtitle tracks for multi-speaker content like interviews and panel discussions. The skill handles pre-processing through pydub for audio segmentation and format normalization before transcription. Post-processing includes punctuation restoration, profanity filtering via custom word lists, and translation through the Whisper translation endpoint. Batch processing supports entire video libraries with progress tracking and error recovery for interrupted jobs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/whisper-subtitle-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/whisper-subtitle-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/whisper-subtitle-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-subtitle-generator/)
