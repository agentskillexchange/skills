---
title: "Whisper Subtitle Generator"
description: "Generates accurate subtitles and captions using OpenAI Whisper API with word-level timestamps. Outputs SRT, VTT, and ASS formats with configurable line length and speaker diarization via pyannote."
slug: "whisper-subtitle-generator"
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/whisper-subtitle-generator/"
---

# Whisper Subtitle Generator

Generates accurate subtitles and captions using OpenAI Whisper API with word-level timestamps. Outputs SRT, VTT, and ASS formats with configurable line length and speaker diarization via pyannote.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install whisper-subtitle-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Whisper Subtitle Generator skill combines OpenAI Whisper speech recognition with professional subtitle formatting to produce broadcast-ready caption files. It supports both the Whisper API and local whisper.cpp inference for flexible deployment options.
The skill processes audio through the Whisper API transcriptions endpoint with word-level timestamp granularity, enabling precise subtitle synchronization. It formats output into industry-standard formats: SRT (SubRip) for universal compatibility, WebVTT for HTML5 video players with CSS styling support, and ASS (Advanced SubStation Alpha) for complex typographical layouts. Line-breaking algorithms respect maximum characters-per-line and reading-speed constraints (typically 20 characters per second) to ensure viewer comfort.
Speaker diarization integrates with pyannote.audio to identify and label different speakers, creating color-coded or prefixed subtitle tracks for multi-speaker content like interviews and panel discussions. The skill handles pre-processing through pydub for audio segmentation and format normalization before transcription. Post-processing includes punctuation restoration, profanity filtering via custom word lists, and translation through the Whisper translation endpoint. Batch processing supports entire video libraries with progress tracking and error recovery for interrupted jobs.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-subtitle-generator/)
