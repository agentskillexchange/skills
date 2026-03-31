---
name: "FFmpeg Audio Normalization Pipeline"
description: "Normalizes audio loudness to broadcast standards using FFmpeg loudnorm filter with EBU R128 two-pass analysis. Measures integrated LUFS, true peak, and loudness range via ffmpeg -af loudnorm=print_format=json."
category: "Media &amp; Transcription"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ffmpeg-audio-normalization-pipeline/"
---
# FFmpeg Audio Normalization Pipeline

Normalizes audio loudness to broadcast standards using FFmpeg loudnorm filter with EBU R128 two-pass analysis. Measures integrated LUFS, true peak, and loudness range via ffmpeg -af loudnorm=print_format=json.

## Overview

This skill implements professional audio loudness normalization using FFmpeg's loudnorm filter conforming to the EBU R128 broadcast standard. It performs a two-pass analysis: the first pass runs ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null /dev/null to measure the source audio's integrated loudness (LUFS), true peak (dBTP), and loudness range (LU). The second pass applies correction using the measured values as input parameters to the loudnorm filter for precise linear normalization. The skill supports multiple target standards: -16 LUFS for streaming platforms (Spotify, Apple Music), -24 LUFS for broadcast TV (ATSC A/85), and -14 LUFS for podcasts. It handles batch processing of multiple files using shell globbing and parallel execution via GNU parallel. Audio format conversion is handled through FFmpeg's codec options: -c:a libmp3lame for MP3, -c:a aac for AAC/M4A, and -c:a libopus for Opus/WebM. The skill preserves metadata tags using -map_metadata 0 and supports sample rate conversion via -ar 44100/48000. Quality validation runs ffprobe -show_format -show_streams to verify output specifications.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-normalization-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-normalization-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-normalization-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-audio-normalization-pipeline -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-audio-normalization-pipeline
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-audio-normalization-pipeline/)
