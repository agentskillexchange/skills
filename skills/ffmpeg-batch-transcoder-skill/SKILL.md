---
title: "FFmpeg Batch Transcoder"
description: "Batch transcode media files using FFmpeg CLI with preset profiles for web, mobile, and broadcast delivery. Supports hardware-accelerated encoding via NVENC/VAAPI and automated quality analysis with VMAF scoring."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Media & Transcription"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "ffmpeg/ffmpeg"
  github_stars: 58972
---

# FFmpeg Batch Transcoder

Automate media transcoding workflows using FFmpeg command-line tools with configurable preset profiles optimized for different delivery targets.

This skill wraps FFmpeg and FFprobe to analyze input media, select appropriate encoding parameters, and batch-process multiple files in parallel. Preset profiles include web-optimized H.264/AAC at various bitrates, mobile-friendly HEVC with adaptive bitrate laddering, and broadcast-spec ProRes/DNxHR for post-production handoff.

Hardware acceleration is supported via NVIDIA NVENC, Intel VAAPI, and Apple VideoToolbox backends, with automatic fallback to software encoding when GPU resources are unavailable. The skill detects available hardware encoders at runtime and selects the optimal pipeline.

Quality validation runs VMAF perceptual scoring against source material to verify encoding quality meets configured thresholds. Failed encodes are automatically retried with adjusted CRF/bitrate parameters. Output includes detailed logs with per-file encoding statistics, compression ratios, and VMAF scores for quality assurance review.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ffmpeg-batch-transcoder-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ffmpeg-batch-transcoder-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcoder-skill/)
