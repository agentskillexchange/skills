---
title: "FFmpeg Batch Transcode Pipeline"
description: "Orchestrates parallel FFmpeg transcoding jobs with hardware-accelerated encoding via NVENC, VAAPI, or VideoToolbox. Supports HLS adaptive bitrate packaging using ffmpeg -f hls with multiple -map streams and fmp4 segment formatting for DASH output."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Media &amp; Transcription"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "ffmpeg/ffmpeg"
  github_stars: 58972
---

# FFmpeg Batch Transcode Pipeline

Overview
The FFmpeg Batch Transcode Pipeline orchestrates parallel video transcoding jobs with intelligent queue management and hardware acceleration detection. It maximizes throughput by distributing encoding workloads across available GPU and CPU resources while maintaining output quality standards.

Key Capabilities
This skill auto-detects hardware acceleration capabilities including NVIDIA NVENC via ffmpeg -hwaccels, Intel VAAPI through /dev/dri/renderD128, and Apple VideoToolbox on macOS. It configures optimal encoder presets with bitrate ladders for adaptive streaming, supporting both H.264 and HEVC/H.265 encoding with lookahead and B-frame optimization.

Streaming Output
Generates HLS adaptive bitrate packages using ffmpeg -f hls with multiple -map stream selections, fMP4 segment formatting for DASH compatibility, and master playlist generation with bandwidth and resolution variant declarations. Supports subtitle track multiplexing, audio normalization via the loudnorm filter, and thumbnail sprite sheet generation using the fps and tile filters for video player scrubbing previews.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcode-pipeline/)
