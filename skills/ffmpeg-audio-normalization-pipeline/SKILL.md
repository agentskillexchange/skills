---
title: "FFmpeg Audio Normalization Pipeline"
description: "Normalizes audio loudness to broadcast standards using FFmpeg loudnorm filter with EBU R128 two-pass analysis. Measures integrated LUFS, true peak, and loudness range via ffmpeg -af loudnorm=print_format=json."
slug: "ffmpeg-audio-normalization-pipeline"
category:
  - "Media &amp; Transcription"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ffmpeg-audio-normalization-pipeline/"
listed: true
---

# FFmpeg Audio Normalization Pipeline

Normalizes audio loudness to broadcast standards using FFmpeg loudnorm filter with EBU R128 two-pass analysis. Measures integrated LUFS, true peak, and loudness range via ffmpeg -af loudnorm=print_format=json.

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
clawhub install ffmpeg-audio-normalization-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill implements professional audio loudness normalization using FFmpeg’s loudnorm filter conforming to the EBU R128 broadcast standard. It performs a two-pass analysis: the first pass runs ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null /dev/null to measure the source audio’s integrated loudness (LUFS), true peak (dBTP), and loudness range (LU). The second pass applies correction using the measured values as input parameters to the loudnorm filter for precise linear normalization. The skill supports multiple target standards: -16 LUFS for streaming platforms (Spotify, Apple Music), -24 LUFS for broadcast TV (ATSC A/85), and -14 LUFS for podcasts. It handles batch processing of multiple files using shell globbing and parallel execution via GNU parallel. Audio format conversion is handled through FFmpeg’s codec options: -c:a libmp3lame for MP3, -c:a aac for AAC/M4A, and -c:a libopus for Opus/WebM. The skill preserves metadata tags using -map_metadata 0 and supports sample rate conversion via -ar 44100/48000. Quality validation runs ffprobe -show_format -show_streams to verify output specifications.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-audio-normalization-pipeline/)
