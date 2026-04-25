---
title: "Whisper Diarization Post-Processor"
description: "Enhances OpenAI Whisper transcription output with speaker diarization using pyannote.audio pipeline and speechbrain embeddings. Aligns word-level timestamps from whisper-timestamped with speaker segments for multi-speaker meeting transcript generation."
verification: "security_reviewed"
source: "https://github.com/openai/whisper"
category:
  - "Media & Transcription"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97775
---

# Whisper Diarization Post-Processor

Overview The Whisper Diarization Post-Processor enhances raw OpenAI Whisper transcription output by adding speaker identification and precise timestamp alignment. It combines state-of-the-art speech recognition with neural speaker diarization for production-quality meeting transcripts. Key Capabilities This skill processes Whisper output through the pyannote.audio speaker diarization pipeline, using pre-trained speaker embedding models from speechbrain for voice characterization. It aligns word-level timestamps from whisper-timestamped with speaker segments using an optimal assignment algorithm that handles overlapping speech regions. Output Formats Generates formatted transcripts with speaker labels, timestamps, and confidence scores in multiple output formats including SRT, VTT, and structured JSON. Supports custom speaker name mapping through voice enrollment, handles multi-language transcription with automatic language detection, and produces analytics summaries including per-speaker talk time ratios, interruption counts, and topic transition markers for meeting intelligence dashboards.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/whisper-diarization-post-processor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/whisper-diarization-post-processor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/whisper-diarization-post-processor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-diarization-post-processor/)
