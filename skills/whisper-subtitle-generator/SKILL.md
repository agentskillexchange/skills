---
title: "Whisper Subtitle Generator"
description: "Generates accurate subtitles and captions using OpenAI Whisper API with word-level timestamps. Outputs SRT, VTT, and ASS formats with configurable line length and speaker diarization via pyannote."
verification: security_reviewed
source: "https://github.com/openai/whisper"
category:
  - "Media &amp; Transcription"
framework:
  - "Gemini"
---

# Whisper Subtitle Generator

The Whisper Subtitle Generator skill combines OpenAI Whisper speech recognition with professional subtitle formatting to produce broadcast-ready caption files. It supports both the Whisper API and local whisper.cpp inference for flexible deployment options.

The skill processes audio through the Whisper API transcriptions endpoint with word-level timestamp granularity, enabling precise subtitle synchronization. It formats output into industry-standard formats: SRT (SubRip) for universal compatibility, WebVTT for HTML5 video players with CSS styling support, and ASS (Advanced SubStation Alpha) for complex typographical layouts. Line-breaking algorithms respect maximum characters-per-line and reading-speed constraints (typically 20 characters per second) to ensure viewer comfort.

Speaker diarization integrates with pyannote.audio to identify and label different speakers, creating color-coded or prefixed subtitle tracks for multi-speaker content like interviews and panel discussions. The skill handles pre-processing through pydub for audio segmentation and format normalization before transcription. Post-processing includes punctuation restoration, profanity filtering via custom word lists, and translation through the Whisper translation endpoint. Batch processing supports entire video libraries with progress tracking and error recovery for interrupted jobs.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-subtitle-generator/)
