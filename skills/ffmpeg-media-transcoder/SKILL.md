---
title: "FFmpeg Media Transcoder"
description: "Automated video and audio transcoding using FFmpeg with hardware-accelerated encoding via NVENC/VAAPI, HLS adaptive streaming output, and MediaInfo-based quality validation."
slug: "ffmpeg-media-transcoder"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ffmpeg-media-transcoder/"
listed: true
---

# FFmpeg Media Transcoder

Automated video and audio transcoding using FFmpeg with hardware-accelerated encoding via NVENC/VAAPI, HLS adaptive streaming output, and MediaInfo-based quality validation.

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
clawhub install ffmpeg-media-transcoder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The FFmpeg Media Transcoder skill automates media transcoding workflows using FFmpeg with intelligent codec selection. It supports H.264, H.265/HEVC, AV1, VP9 for video and AAC, Opus, FLAC for audio, with automatic hardware acceleration detection for NVIDIA NVENC, Intel VAAPI/QSV, and Apple VideoToolbox.
HLS (HTTP Live Streaming) output generates multi-bitrate adaptive streaming packages with configurable rendition ladders following Apple’s HLS Authoring Specification. The skill creates master playlists, segment files, and byte-range indexed fMP4 segments with proper EXT-X-STREAM-INF tags including resolution, bandwidth, and codec parameters.
Quality validation uses MediaInfo to parse output container metadata and verify codec parameters, bitrate compliance, and audio channel configuration. The skill performs VMAF (Video Multi-Method Assessment Fusion) scoring for perceptual quality measurement against source files. A job queue system manages concurrent transcoding jobs with priority scheduling, progress tracking via FFmpeg’s progress protocol, and webhook notifications on job completion or failure.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-media-transcoder/)
