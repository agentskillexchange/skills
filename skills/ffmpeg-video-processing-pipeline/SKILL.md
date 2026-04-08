---
title: FFmpeg Video Processing Pipeline
description: The FFmpeg Video Processing Pipeline constructs sophisticated filtergraph
  chains for professional video workflows. It handles batch transcoding across codecs
  (H.264, H.265/HEVC, AV1, VP9) with configurable CRF/bitrate targets, two-pass encoding,
  and per-title encoding optimization that selects bitrate ladders based on content
  complexity analysis. Hardware acceleration is supported via NVIDIA NVENC, Intel
  QuickSync (QSV), and Apple VideoToolbox, with automatic fallback to software encoding
  when GPU resources are unavailable. HDR workflows include PQ-to-HLG conversion,
  HDR10+ dynamic metadata passthrough, and Dolby Vision profile 8.1 remuxing. The
  skill generates thumbnail sprite sheets (WebVTT + contact sheet images) for video
  player scrubbing, creates HLS and DASH adaptive streaming packages with proper segment
  alignment, and handles audio normalization via EBU R128 loudness standards. Subtitle
  extraction (SRT, ASS, VobSub OCR) and burn-in with configurable styling round out
  the post-production capabilities. Scene detection via ffprobe enables intelligent
  chapter marker generation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-video-processing-pipeline/
category:
- Image &amp; Creative Automation
framework:
- MCP
---

# FFmpeg Video Processing Pipeline

The FFmpeg Video Processing Pipeline constructs sophisticated filtergraph chains for professional video workflows. It handles batch transcoding across codecs (H.264, H.265/HEVC, AV1, VP9) with configurable CRF/bitrate targets, two-pass encoding, and per-title encoding optimization that selects bitrate ladders based on content complexity analysis. Hardware acceleration is supported via NVIDIA NVENC, Intel QuickSync (QSV), and Apple VideoToolbox, with automatic fallback to software encoding when GPU resources are unavailable. HDR workflows include PQ-to-HLG conversion, HDR10+ dynamic metadata passthrough, and Dolby Vision profile 8.1 remuxing. The skill generates thumbnail sprite sheets (WebVTT + contact sheet images) for video player scrubbing, creates HLS and DASH adaptive streaming packages with proper segment alignment, and handles audio normalization via EBU R128 loudness standards. Subtitle extraction (SRT, ASS, VobSub OCR) and burn-in with configurable styling round out the post-production capabilities. Scene detection via ffprobe enables intelligent chapter marker generation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-video-processing-pipeline/)
