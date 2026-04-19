---
title: "FFmpeg Batch Transcoder"
description: "Automate media transcoding workflows using FFmpeg command-line tools with configurable preset profiles optimized for different delivery targets. This skill wraps FFmpeg and FFprobe to analyze input media, select appropriate encoding parameters, and batch-process multiple files in parallel. Preset profiles include web-optimized H.264/AAC at various bitrates, mobile-friendly HEVC with adaptive bitrate laddering, and broadcast-spec ProRes/DNxHR for post-production handoff. Hardware acceleration is supported via NVIDIA NVENC, Intel VAAPI, and Apple VideoToolbox backends, with automatic fallback to software encoding when GPU resources are unavailable. The skill detects available hardware encoders at runtime and selects the optimal pipeline. Quality validation runs VMAF perceptual scoring against source material to verify encoding quality meets configured thresholds. Failed encodes are automatically retried with adjusted CRF/bitrate parameters. Output includes detailed logs with per-file encoding statistics, compression ratios, and VMAF scores for quality assurance review."
source: "https://github.com/FFmpeg/FFmpeg"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Cursor"
---

# FFmpeg Batch Transcoder

Automate media transcoding workflows using FFmpeg command-line tools with configurable preset profiles optimized for different delivery targets. This skill wraps FFmpeg and FFprobe to analyze input media, select appropriate encoding parameters, and batch-process multiple files in parallel. Preset profiles include web-optimized H.264/AAC at various bitrates, mobile-friendly HEVC with adaptive bitrate laddering, and broadcast-spec ProRes/DNxHR for post-production handoff. Hardware acceleration is supported via NVIDIA NVENC, Intel VAAPI, and Apple VideoToolbox backends, with automatic fallback to software encoding when GPU resources are unavailable. The skill detects available hardware encoders at runtime and selects the optimal pipeline. Quality validation runs VMAF perceptual scoring against source material to verify encoding quality meets configured thresholds. Failed encodes are automatically retried with adjusted CRF/bitrate parameters. Output includes detailed logs with per-file encoding statistics, compression ratios, and VMAF scores for quality assurance review.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcoder-skill/)
