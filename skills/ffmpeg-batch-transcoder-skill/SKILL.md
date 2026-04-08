---
title: FFmpeg Batch Transcoder
description: Automate media transcoding workflows using FFmpeg command-line tools
  with configurable preset profiles optimized for different delivery targets. This
  skill wraps FFmpeg and FFprobe to analyze input media, select appropriate encoding
  parameters, and batch-process multiple files in parallel. Preset profiles include
  web-optimized H.264/AAC at various bitrates, mobile-friendly HEVC with adaptive
  bitrate laddering, and broadcast-spec ProRes/DNxHR for post-production handoff.
  Hardware acceleration is supported via NVIDIA NVENC, Intel VAAPI, and Apple VideoToolbox
  backends, with automatic fallback to software encoding when GPU resources are unavailable.
  The skill detects available hardware encoders at runtime and selects the optimal
  pipeline. Quality validation runs VMAF perceptual scoring against source material
  to verify encoding quality meets configured thresholds. Failed encodes are automatically
  retried with adjusted CRF/bitrate parameters. Output includes detailed logs with
  per-file encoding statistics, compression ratios, and VMAF scores for quality assurance
  review.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-batch-transcoder-skill/
category:
- Media &amp; Transcription
framework:
- Cursor
---

# FFmpeg Batch Transcoder

Automate media transcoding workflows using FFmpeg command-line tools with configurable preset profiles optimized for different delivery targets. This skill wraps FFmpeg and FFprobe to analyze input media, select appropriate encoding parameters, and batch-process multiple files in parallel. Preset profiles include web-optimized H.264/AAC at various bitrates, mobile-friendly HEVC with adaptive bitrate laddering, and broadcast-spec ProRes/DNxHR for post-production handoff. Hardware acceleration is supported via NVIDIA NVENC, Intel VAAPI, and Apple VideoToolbox backends, with automatic fallback to software encoding when GPU resources are unavailable. The skill detects available hardware encoders at runtime and selects the optimal pipeline. Quality validation runs VMAF perceptual scoring against source material to verify encoding quality meets configured thresholds. Failed encodes are automatically retried with adjusted CRF/bitrate parameters. Output includes detailed logs with per-file encoding statistics, compression ratios, and VMAF scores for quality assurance review.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcoder-skill/)
