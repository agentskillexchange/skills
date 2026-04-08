---
title: FFmpeg Batch Transcode Pipeline
description: Overview The FFmpeg Batch Transcode Pipeline orchestrates parallel video
  transcoding jobs with intelligent queue management and hardware acceleration detection.
  It maximizes throughput by distributing encoding workloads across available GPU
  and CPU resources while maintaining output quality standards. Key Capabilities This
  skill auto-detects hardware acceleration capabilities including NVIDIA NVENC via
  ffmpeg -hwaccels , Intel VAAPI through /dev/dri/renderD128 , and Apple VideoToolbox
  on macOS. It configures optimal encoder presets with bitrate ladders for adaptive
  streaming, supporting both H.264 and HEVC/H.265 encoding with lookahead and B-frame
  optimization. Streaming Output Generates HLS adaptive bitrate packages using ffmpeg
  -f hls with multiple -map stream selections, fMP4 segment formatting for DASH compatibility,
  and master playlist generation with bandwidth and resolution variant declarations.
  Supports subtitle track multiplexing, audio normalization via the loudnorm filter,
  and thumbnail sprite sheet generation using the fps and tile filters for video player
  scrubbing previews.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-batch-transcode-pipeline/
category:
- Media &amp; Transcription
framework:
- Custom Agents
---

# FFmpeg Batch Transcode Pipeline

Overview The FFmpeg Batch Transcode Pipeline orchestrates parallel video transcoding jobs with intelligent queue management and hardware acceleration detection. It maximizes throughput by distributing encoding workloads across available GPU and CPU resources while maintaining output quality standards. Key Capabilities This skill auto-detects hardware acceleration capabilities including NVIDIA NVENC via ffmpeg -hwaccels , Intel VAAPI through /dev/dri/renderD128 , and Apple VideoToolbox on macOS. It configures optimal encoder presets with bitrate ladders for adaptive streaming, supporting both H.264 and HEVC/H.265 encoding with lookahead and B-frame optimization. Streaming Output Generates HLS adaptive bitrate packages using ffmpeg -f hls with multiple -map stream selections, fMP4 segment formatting for DASH compatibility, and master playlist generation with bandwidth and resolution variant declarations. Supports subtitle track multiplexing, audio normalization via the loudnorm filter, and thumbnail sprite sheet generation using the fps and tile filters for video player scrubbing previews.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcode-pipeline/)
