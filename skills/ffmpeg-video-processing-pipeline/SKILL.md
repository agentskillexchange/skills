---
title: "FFmpeg Video Processing Pipeline"
description: "Builds complex FFmpeg filtergraph chains for batch video transcoding, thumbnail sprite generation, and HLS adaptive bitrate packaging. Supports NVIDIA NVENC hardware acceleration and HDR tone mapping."
slug: "ffmpeg-video-processing-pipeline"
category:
  - "Image &amp; Creative Automation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ffmpeg-video-processing-pipeline/"
listed: true
---

# FFmpeg Video Processing Pipeline

Builds complex FFmpeg filtergraph chains for batch video transcoding, thumbnail sprite generation, and HLS adaptive bitrate packaging. Supports NVIDIA NVENC hardware acceleration and HDR tone mapping.

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
clawhub install ffmpeg-video-processing-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The FFmpeg Video Processing Pipeline constructs sophisticated filtergraph chains for professional video workflows. It handles batch transcoding across codecs (H.264, H.265/HEVC, AV1, VP9) with configurable CRF/bitrate targets, two-pass encoding, and per-title encoding optimization that selects bitrate ladders based on content complexity analysis.
Hardware acceleration is supported via NVIDIA NVENC, Intel QuickSync (QSV), and Apple VideoToolbox, with automatic fallback to software encoding when GPU resources are unavailable. HDR workflows include PQ-to-HLG conversion, HDR10+ dynamic metadata passthrough, and Dolby Vision profile 8.1 remuxing.
The skill generates thumbnail sprite sheets (WebVTT + contact sheet images) for video player scrubbing, creates HLS and DASH adaptive streaming packages with proper segment alignment, and handles audio normalization via EBU R128 loudness standards. Subtitle extraction (SRT, ASS, VobSub OCR) and burn-in with configurable styling round out the post-production capabilities. Scene detection via ffprobe enables intelligent chapter marker generation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-video-processing-pipeline/)
