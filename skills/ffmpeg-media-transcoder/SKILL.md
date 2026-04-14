---
title: "FFmpeg Media Transcoder"
description: "Automated video and audio transcoding using FFmpeg with hardware-accelerated encoding via NVENC/VAAPI, HLS adaptive streaming output, and MediaInfo-based quality validation."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "ffmpeg/ffmpeg"
  github_stars: 58972
---

# FFmpeg Media Transcoder

The FFmpeg Media Transcoder skill automates media transcoding workflows using FFmpeg with intelligent codec selection. It supports H.264, H.265/HEVC, AV1, VP9 for video and AAC, Opus, FLAC for audio, with automatic hardware acceleration detection for NVIDIA NVENC, Intel VAAPI/QSV, and Apple VideoToolbox.

HLS (HTTP Live Streaming) output generates multi-bitrate adaptive streaming packages with configurable rendition ladders following Apple’s HLS Authoring Specification. The skill creates master playlists, segment files, and byte-range indexed fMP4 segments with proper EXT-X-STREAM-INF tags including resolution, bandwidth, and codec parameters.

Quality validation uses MediaInfo to parse output container metadata and verify codec parameters, bitrate compliance, and audio channel configuration. The skill performs VMAF (Video Multi-Method Assessment Fusion) scoring for perceptual quality measurement against source files. A job queue system manages concurrent transcoding jobs with priority scheduling, progress tracking via FFmpeg’s progress protocol, and webhook notifications on job completion or failure.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-media-transcoder/)
