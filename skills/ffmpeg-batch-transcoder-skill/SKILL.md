---
name: "FFmpeg Batch Transcoder"
description: "Batch transcode media files using FFmpeg CLI with preset profiles for web, mobile, and broadcast delivery. Supports hardware-accelerated encoding via NVENC/VAAPI and automated quality analysis with VMAF scoring."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ffmpeg-batch-transcoder-skill/"
category:
  - "Media &amp; Transcription"
framework:
  - "Cursor"
---

# FFmpeg Batch Transcoder

Automate media transcoding workflows using FFmpeg command-line tools with configurable preset profiles optimized for different delivery targets.
This skill wraps FFmpeg and FFprobe to analyze input media, select appropriate encoding parameters, and batch-process multiple files in parallel. Preset profiles include web-optimized H.264/AAC at various bitrates, mobile-friendly HEVC with adaptive bitrate laddering, and broadcast-spec ProRes/DNxHR for post-production handoff.
Hardware acceleration is supported via NVIDIA NVENC, Intel VAAPI, and Apple VideoToolbox backends, with automatic fallback to software encoding when GPU resources are unavailable. The skill detects available hardware encoders at runtime and selects the optimal pipeline.
Quality validation runs VMAF perceptual scoring against source material to verify encoding quality meets configured thresholds. Failed encodes are automatically retried with adjusted CRF/bitrate parameters. Output includes detailed logs with per-file encoding statistics, compression ratios, and VMAF scores for quality assurance review.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcoder-skill/)
