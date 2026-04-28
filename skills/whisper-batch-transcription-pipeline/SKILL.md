---
title: "OpenAI Whisper Batch Transcription Pipeline"
description: "Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English."
verification: security_reviewed
source: "https://github.com/openai/whisper"
category:
  - "Media & Transcription"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openai/whisper"
  github_stars: 97803
  license: "MIT"
---

# OpenAI Whisper Batch Transcription Pipeline

Processes audio files from an S3 bucket using Whisper large-v3, splitting recordings into 30-second chunks with ffmpeg before transcription. Outputs timestamped SRT and VTT subtitle files plus plain-text transcripts, then uploads artifacts back to S3. Supports language auto-detection and translation to English.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/whisper-batch-transcription-pipeline
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/whisper-batch-transcription-pipeline`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisper-batch-transcription-pipeline/)
