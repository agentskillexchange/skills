---
title: FFmpeg Media Transcoder
description: The FFmpeg Media Transcoder skill automates media transcoding workflows
  using FFmpeg with intelligent codec selection. It supports H.264, H.265/HEVC, AV1,
  VP9 for video and AAC, Opus, FLAC for audio, with automatic hardware acceleration
  detection for NVIDIA NVENC, Intel VAAPI/QSV, and Apple VideoToolbox. HLS (HTTP Live
  Streaming) output generates multi-bitrate adaptive streaming packages with configurable
  rendition ladders following Apple’s HLS Authoring Specification. The skill creates
  master playlists, segment files, and byte-range indexed fMP4 segments with proper
  EXT-X-STREAM-INF tags including resolution, bandwidth, and codec parameters. Quality
  validation uses MediaInfo to parse output container metadata and verify codec parameters,
  bitrate compliance, and audio channel configuration. The skill performs VMAF (Video
  Multi-Method Assessment Fusion) scoring for perceptual quality measurement against
  source files. A job queue system manages concurrent transcoding jobs with priority
  scheduling, progress tracking via FFmpeg’s progress protocol, and webhook notifications
  on job completion or failure.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-media-transcoder/
category:
- Image &amp; Creative Automation
framework:
- Claude Code
---

# FFmpeg Media Transcoder

The FFmpeg Media Transcoder skill automates media transcoding workflows using FFmpeg with intelligent codec selection. It supports H.264, H.265/HEVC, AV1, VP9 for video and AAC, Opus, FLAC for audio, with automatic hardware acceleration detection for NVIDIA NVENC, Intel VAAPI/QSV, and Apple VideoToolbox. HLS (HTTP Live Streaming) output generates multi-bitrate adaptive streaming packages with configurable rendition ladders following Apple’s HLS Authoring Specification. The skill creates master playlists, segment files, and byte-range indexed fMP4 segments with proper EXT-X-STREAM-INF tags including resolution, bandwidth, and codec parameters. Quality validation uses MediaInfo to parse output container metadata and verify codec parameters, bitrate compliance, and audio channel configuration. The skill performs VMAF (Video Multi-Method Assessment Fusion) scoring for perceptual quality measurement against source files. A job queue system manages concurrent transcoding jobs with priority scheduling, progress tracking via FFmpeg’s progress protocol, and webhook notifications on job completion or failure.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-media-transcoder/)
