---
title: FFmpeg Audio Normalization Pipeline
description: Normalizes audio loudness to broadcast standards using FFmpeg loudnorm
  filter with EBU R128 two-pass analysis. Measures integrated LUFS, true peak, and
  loudness range via ffmpeg -af loudnorm=print_format=json.
verification: security_reviewed
source: https://github.com/FFmpeg/FFmpeg
category:
- Media & Transcription
framework:
- OpenClaw
tool_ecosystem:
  github_repo: ffmpeg/ffmpeg
  github_stars: 58972
---

# FFmpeg Audio Normalization Pipeline

Normalizes audio loudness to broadcast standards using FFmpeg loudnorm filter with EBU R128 two-pass analysis. Measures integrated LUFS, true peak, and loudness range via ffmpeg -af loudnorm=print_format=json.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/ffmpeg-audio-normalization-pipeline/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ffmpeg-audio-normalization-pipeline
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/ffmpeg-audio-normalization-pipeline`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-audio-normalization-pipeline/)
