---
title: "Whisper Diarization Post-Processor"
description: "Enhances OpenAI Whisper transcription output with speaker diarization using pyannote.audio pipeline and speechbrain embeddings. Aligns word-level timestamps from whisper-timestamped with speaker segments for multi-speaker meeting transcript generation."
slug: "whisper-diarization-post-processor"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/whisper-diarization-post-processor/"
---

# Whisper Diarization Post-Processor

Enhances OpenAI Whisper transcription output with speaker diarization using pyannote.audio pipeline and speechbrain embeddings. Aligns word-level timestamps from whisper-timestamped with speaker segments for multi-speaker meeting transcript generation.

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
clawhub install whisper-diarization-post-processor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
The Whisper Diarization Post-Processor enhances raw OpenAI Whisper transcription output by adding speaker identification and precise timestamp alignment. It combines state-of-the-art speech recognition with neural speaker diarization for production-quality meeting transcripts.
Key Capabilities
This skill processes Whisper output through the pyannote.audio speaker diarization pipeline, using pre-trained speaker embedding models from speechbrain for voice characterization. It aligns word-level timestamps from whisper-timestamped with speaker segments using an optimal assignment algorithm that handles overlapping speech regions.
Output Formats
Generates formatted transcripts with speaker labels, timestamps, and confidence scores in multiple output formats including SRT, VTT, and structured JSON. Supports custom speaker name mapping through voice enrollment, handles multi-language transcription with automatic language detection, and produces analytics summaries including per-speaker talk time ratios, interruption counts, and topic transition markers for meeting intelligence dashboards.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-diarization-post-processor/)
