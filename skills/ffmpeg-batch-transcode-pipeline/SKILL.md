---
title: "FFmpeg Batch Transcode Pipeline"
description: "Orchestrates parallel FFmpeg transcoding jobs with hardware-accelerated encoding via NVENC, VAAPI, or VideoToolbox. Supports HLS adaptive bitrate packaging using ffmpeg -f hls with multiple -map streams and fmp4 segment formatting for DASH output."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Media & Transcription"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "ffmpeg/ffmpeg"
  github_stars: 58972
---

# FFmpeg Batch Transcode Pipeline

Overview The FFmpeg Batch Transcode Pipeline orchestrates parallel video transcoding jobs with intelligent queue management and hardware acceleration detection. It maximizes throughput by distributing encoding workloads across available GPU and CPU resources while maintaining output quality standards.

Key Capabilities This skill auto-detects hardware acceleration capabilities including NVIDIA NVENC via ffmpeg -hwaccels, Intel VAAPI through /dev/dri/renderD128, and Apple VideoToolbox on macOS. It configures optimal encoder presets with bitrate ladders for adaptive streaming, supporting both H.264 and HEVC/H.265 encoding with lookahead and B-frame optimization.

Streaming Output Generates HLS adaptive bitrate packages using ffmpeg -f hls with multiple -map stream selections, fMP4 segment formatting for DASH compatibility, and master playlist generation with bandwidth and resolution variant declarations. Supports subtitle track multiplexing, audio normalization via the loudnorm filter, and thumbnail sprite sheet generation using the fps and tile filters for video player scrubbing previews.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ffmpeg-batch-transcode-pipeline
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ffmpeg-batch-transcode-pipeline` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcode-pipeline/)
