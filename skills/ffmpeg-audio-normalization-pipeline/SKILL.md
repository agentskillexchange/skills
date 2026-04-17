---
name: FFmpeg Audio Normalization Pipeline
description: Normalizes audio loudness to broadcast standards using FFmpeg loudnorm
  filter with EBU R128 two-pass analysis. Measures integrated LUFS, true peak, and
  loudness range via ffmpeg -af loudnorm=print_format=json.
category: Media & Transcription
framework: OpenClaw
verification: security_reviewed
source: https://github.com/FFmpeg/FFmpeg
---
# FFmpeg Audio Normalization Pipeline
Normalizes audio loudness to broadcast standards using FFmpeg loudnorm filter with EBU R128 two-pass analysis. Measures integrated LUFS, true peak, and loudness range via ffmpeg -af loudnorm=print_format=json.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ffmpeg-audio-normalization-pipeline
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ffmpeg-audio-normalization-pipeline` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-audio-normalization-pipeline/)
