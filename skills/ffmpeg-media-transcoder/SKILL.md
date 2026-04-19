---
title: "FFmpeg Media Transcoder"
description: "The FFmpeg Media Transcoder skill automates media transcoding workflows using FFmpeg with intelligent codec selection. It supports H.264, H.265/HEVC, AV1, VP9 for video and AAC, Opus, FLAC for audio, with automatic hardware acceleration detection for NVIDIA NVENC, Intel VAAPI/QSV, and Apple VideoToolbox. HLS (HTTP Live Streaming) output generates multi-bitrate adaptive streaming packages with configurable rendition ladders following Apple&#8217;s HLS Authoring Specification. The skill creates master playlists, segment files, and byte-range indexed fMP4 segments with proper EXT-X-STREAM-INF tags including resolution, bandwidth, and codec parameters. Quality validation uses MediaInfo to parse output container metadata and verify codec parameters, bitrate compliance, and audio channel configuration. The skill performs VMAF (Video Multi-Method Assessment Fusion) scoring for perceptual quality measurement against source files. A job queue system manages concurrent transcoding jobs with priority scheduling, progress tracking via FFmpeg&#8217;s progress protocol, and webhook notifications on job completion or failure."
source: "https://github.com/FFmpeg/FFmpeg"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Code"
---

# FFmpeg Media Transcoder

The FFmpeg Media Transcoder skill automates media transcoding workflows using FFmpeg with intelligent codec selection. It supports H.264, H.265/HEVC, AV1, VP9 for video and AAC, Opus, FLAC for audio, with automatic hardware acceleration detection for NVIDIA NVENC, Intel VAAPI/QSV, and Apple VideoToolbox. HLS (HTTP Live Streaming) output generates multi-bitrate adaptive streaming packages with configurable rendition ladders following Apple&#8217;s HLS Authoring Specification. The skill creates master playlists, segment files, and byte-range indexed fMP4 segments with proper EXT-X-STREAM-INF tags including resolution, bandwidth, and codec parameters. Quality validation uses MediaInfo to parse output container metadata and verify codec parameters, bitrate compliance, and audio channel configuration. The skill performs VMAF (Video Multi-Method Assessment Fusion) scoring for perceptual quality measurement against source files. A job queue system manages concurrent transcoding jobs with priority scheduling, progress tracking via FFmpeg&#8217;s progress protocol, and webhook notifications on job completion or failure.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-media-transcoder/)
