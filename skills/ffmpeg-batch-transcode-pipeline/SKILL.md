---
title: "FFmpeg Batch Transcode Pipeline"
description: "Orchestrates parallel FFmpeg transcoding jobs with hardware-accelerated encoding via NVENC, VAAPI, or VideoToolbox. Supports HLS adaptive bitrate packaging using ffmpeg -f hls with multiple -map streams and fmp4 segment formatting for DASH output."
slug: "ffmpeg-batch-transcode-pipeline"
category:
  - "Media &amp; Transcription"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ffmpeg-batch-transcode-pipeline/"
---

# FFmpeg Batch Transcode Pipeline

Orchestrates parallel FFmpeg transcoding jobs with hardware-accelerated encoding via NVENC, VAAPI, or VideoToolbox. Supports HLS adaptive bitrate packaging using ffmpeg -f hls with multiple -map streams and fmp4 segment formatting for DASH output.

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
clawhub install ffmpeg-batch-transcode-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
The FFmpeg Batch Transcode Pipeline orchestrates parallel video transcoding jobs with intelligent queue management and hardware acceleration detection. It maximizes throughput by distributing encoding workloads across available GPU and CPU resources while maintaining output quality standards.
Key Capabilities
This skill auto-detects hardware acceleration capabilities including NVIDIA NVENC via ffmpeg -hwaccels, Intel VAAPI through /dev/dri/renderD128, and Apple VideoToolbox on macOS. It configures optimal encoder presets with bitrate ladders for adaptive streaming, supporting both H.264 and HEVC/H.265 encoding with lookahead and B-frame optimization.
Streaming Output
Generates HLS adaptive bitrate packages using ffmpeg -f hls with multiple -map stream selections, fMP4 segment formatting for DASH compatibility, and master playlist generation with bandwidth and resolution variant declarations. Supports subtitle track multiplexing, audio normalization via the loudnorm filter, and thumbnail sprite sheet generation using the fps and tile filters for video player scrubbing previews.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcode-pipeline/)
