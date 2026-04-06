---
name: Whisper Subtitle Generator
description: Generates accurate subtitles and captions using OpenAI Whisper API with
  word-level timestamps. Outputs SRT, VTT, and ASS formats with configurable line
  length and speaker diarization via pyannote.
category: "Media &amp; Transcription"
framework: Gemini
verification: security_reviewed
source: "https://agentskillexchange.com/skills/whisper-subtitle-generator/"
---
# Whisper Subtitle Generator

Generates accurate subtitles and captions using OpenAI Whisper API with word-level timestamps. Outputs SRT, VTT, and ASS formats with configurable line length and speaker diarization via pyannote.

The Whisper Subtitle Generator skill combines OpenAI Whisper speech recognition with professional subtitle formatting to produce broadcast-ready caption files. It supports both the Whisper API and local whisper.cpp inference for flexible deployment options.

The skill processes audio through the Whisper API transcriptions endpoint with word-level timestamp granularity, enabling precise subtitle synchronization. It formats output into industry-standard formats: SRT (SubRip) for universal compatibility, WebVTT for HTML5 video players with CSS styling support, and ASS (Advanced SubStation Alpha) for complex typographical layouts. Line-breaking algorithms respect maximum characters-per-line and reading-speed constraints (typically 20 characters per second) to ensure viewer comfort.

Speaker diarization integrates with pyannote.audio to identify and label different speakers, creating color-coded or prefixed subtitle tracks for multi-speaker content like interviews and panel discussions. The skill handles pre-processing through pydub for audio segmentation and format normalization before transcription. Post-processing includes punctuation restoration, profanity filtering via custom word lists, and translation through the Whisper translation endpoint. Batch processing supports entire video libraries with progress tracking and error recovery for interrupted jobs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill whisper-subtitle-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill whisper-subtitle-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill whisper-subtitle-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill whisper-subtitle-generator -a codex
```

### OpenClaw

```bash
clawhub install whisper-subtitle-generator
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-subtitle-generator/)
