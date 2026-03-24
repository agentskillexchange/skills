---
name: "FFmpeg Batch Transcode Pipeline"
description: "Orchestrates parallel FFmpeg transcoding jobs with hardware-accelerated encoding via NVENC, VAAPI, or VideoToolbox. Supports HLS adaptive bitrate packaging using ffmpeg -f hls with multiple -map streams and fmp4 segment formatting for DASH output."
category: "Media & Transcription"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ffmpeg-batch-transcode-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ffmpeg"  # from ase_tool_match
  github_stars: 58257  # from ase_github_stars (integer, not string)
  github_repo: "FFmpeg/FFmpeg"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# FFmpeg Batch Transcode Pipeline

Orchestrates parallel FFmpeg transcoding jobs with hardware-accelerated encoding via NVENC, VAAPI, or VideoToolbox. Supports HLS adaptive bitrate packaging using ffmpeg -f hls with multiple -map streams and fmp4 segment formatting for DASH output.

## Overview

Overview

The FFmpeg Batch Transcode Pipeline orchestrates parallel video transcoding jobs with intelligent queue management and hardware acceleration detection. It maximizes throughput by distributing encoding workloads across available GPU and CPU resources while maintaining output quality standards.

Key Capabilities

This skill auto-detects hardware acceleration capabilities including NVIDIA NVENC via `ffmpeg -hwaccels`, Intel VAAPI through `/dev/dri/renderD128`, and Apple VideoToolbox on macOS. It configures optimal encoder presets with bitrate ladders for adaptive streaming, supporting both H.264 and HEVC/H.265 encoding with lookahead and B-frame optimization.

Streaming Output

Generates HLS adaptive bitrate packages using `ffmpeg -f hls` with multiple `-map` stream selections, fMP4 segment formatting for DASH compatibility, and master playlist generation with bandwidth and resolution variant declarations. Supports subtitle track multiplexing, audio normalization via the `loudnorm` filter, and thumbnail sprite sheet generation using the `fps` and `tile` filters for video player scrubbing previews.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-batch-transcode-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-batch-transcode-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-batch-transcode-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-batch-transcode-pipeline -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-batch-transcode-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ffmpeg-batch-transcode-pipeline/
