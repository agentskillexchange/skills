---
title: "FFmpeg Batch Transcoder"
description: "Batch transcode media files using FFmpeg CLI with preset profiles for web, mobile, and broadcast delivery. Supports hardware-accelerated encoding via NVENC/VAAPI and automated quality analysis with VMAF scoring."
slug: "ffmpeg-batch-transcoder-skill"
category:
  - "Media &amp; Transcription"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ffmpeg-batch-transcoder-skill/"
listed: true
---

# FFmpeg Batch Transcoder

Batch transcode media files using FFmpeg CLI with preset profiles for web, mobile, and broadcast delivery. Supports hardware-accelerated encoding via NVENC/VAAPI and automated quality analysis with VMAF scoring.

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
clawhub install ffmpeg-batch-transcoder-skill
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Automate media transcoding workflows using FFmpeg command-line tools with configurable preset profiles optimized for different delivery targets.
This skill wraps FFmpeg and FFprobe to analyze input media, select appropriate encoding parameters, and batch-process multiple files in parallel. Preset profiles include web-optimized H.264/AAC at various bitrates, mobile-friendly HEVC with adaptive bitrate laddering, and broadcast-spec ProRes/DNxHR for post-production handoff.
Hardware acceleration is supported via NVIDIA NVENC, Intel VAAPI, and Apple VideoToolbox backends, with automatic fallback to software encoding when GPU resources are unavailable. The skill detects available hardware encoders at runtime and selects the optimal pipeline.
Quality validation runs VMAF perceptual scoring against source material to verify encoding quality meets configured thresholds. Failed encodes are automatically retried with adjusted CRF/bitrate parameters. Output includes detailed logs with per-file encoding statistics, compression ratios, and VMAF scores for quality assurance review.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcoder-skill/)
