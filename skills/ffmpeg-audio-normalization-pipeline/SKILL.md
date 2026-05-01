---
title: "FFmpeg Audio Normalization Pipeline"
description: "Normalizes audio loudness to broadcast standards using FFmpeg loudnorm filter with EBU R128 two-pass analysis. Measures integrated LUFS, true peak, and loudness range via ffmpeg -af loudnorm=print_format=json."
verification: "security_reviewed"
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Media & Transcription"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "ffmpeg/ffmpeg"
  github_stars: 58972
---

# FFmpeg Audio Normalization Pipeline

This skill implements professional audio loudness normalization using FFmpeg’s loudnorm filter conforming to the EBU R128 broadcast standard. It performs a two-pass analysis: the first pass runs ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null /dev/null to measure the source audio’s integrated loudness (LUFS), true peak (dBTP), and loudness range (LU). The second pass applies correction using the measured values as input parameters to the loudnorm filter for precise linear normalization. The skill supports multiple target standards: -16 LUFS for streaming platforms (Spotify, Apple Music), -24 LUFS for broadcast TV (ATSC A/85), and -14 LUFS for podcasts. It handles batch processing of multiple files using shell globbing and parallel execution via GNU parallel. Audio format conversion is handled through FFmpeg’s codec options: -c:a libmp3lame for MP3, -c:a aac for AAC/M4A, and -c:a libopus for Opus/WebM. The skill preserves metadata tags using -map_metadata 0 and supports sample rate conversion via -ar 44100/48000. Quality validation runs ffprobe -show_format -show_streams to verify output specifications.

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
