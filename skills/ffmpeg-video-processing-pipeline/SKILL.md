---
name: FFmpeg Video Processing Pipeline
description: Builds complex FFmpeg filtergraph chains for batch video transcoding,
  thumbnail sprite generation, and HLS adaptive bitrate packaging. Supports NVIDIA
  NVENC hardware acceleration and HDR tone mapping.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-video-processing-pipeline/
category:
- Image &amp; Creative Automation
framework:
- MCP
---
# FFmpeg Video Processing Pipeline

The FFmpeg Video Processing Pipeline constructs sophisticated filtergraph chains for professional video workflows. It handles batch transcoding across codecs (H.264, H.265/HEVC, AV1, VP9) with configurable CRF/bitrate targets, two-pass encoding, and per-title encoding optimization that selects bitrate ladders based on content complexity analysis.
Hardware acceleration is supported via NVIDIA NVENC, Intel QuickSync (QSV), and Apple VideoToolbox, with automatic fallback to software encoding when GPU resources are unavailable. HDR workflows include PQ-to-HLG conversion, HDR10+ dynamic metadata passthrough, and Dolby Vision profile 8.1 remuxing.
The skill generates thumbnail sprite sheets (WebVTT + contact sheet images) for video player scrubbing, creates HLS and DASH adaptive streaming packages with proper segment alignment, and handles audio normalization via EBU R128 loudness standards. Subtitle extraction (SRT, ASS, VobSub OCR) and burn-in with configurable styling round out the post-production capabilities. Scene detection via ffprobe enables intelligent chapter marker generation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-video-processing-pipeline/)
