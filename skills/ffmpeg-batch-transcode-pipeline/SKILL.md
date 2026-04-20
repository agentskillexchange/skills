---
title: "FFmpeg Batch Transcode Pipeline"
description: "Orchestrates parallel FFmpeg transcoding jobs with hardware-accelerated encoding via NVENC, VAAPI, or VideoToolbox. Supports HLS adaptive bitrate packaging using ffmpeg -f hls with multiple -map streams and fmp4 segment formatting for DASH output."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Media &amp; Transcription"
framework:
  - "Custom Agents"
---

# FFmpeg Batch Transcode Pipeline

Orchestrates parallel FFmpeg transcoding jobs with hardware-accelerated encoding via NVENC, VAAPI, or VideoToolbox. Supports HLS adaptive bitrate packaging using ffmpeg -f hls with multiple -map streams and fmp4 segment formatting for DASH output.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/ffmpeg-batch-transcode-pipeline/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ffmpeg-batch-transcode-pipeline
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/ffmpeg-batch-transcode-pipeline`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcode-pipeline/)
