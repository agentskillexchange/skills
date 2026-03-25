---
name: "FFmpeg Intelligent Media Processor"
description: "Orchestrates complex video and audio processing pipelines using FFmpeg and FFprobe with scene detection via PySceneDetect. Handles format conversion, thumbnail generation, HLS packaging, and loudness normalization per EBU R128."
category: "Image & Creative Automation"
framework: "OpenClaw"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ffmpeg-intelligent-media-processor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ffmpeg"  # from ase_tool_match
  github_stars: 58257  # from ase_github_stars (integer, not string)
  github_repo: "FFmpeg/FFmpeg"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# FFmpeg Intelligent Media Processor

Orchestrates complex video and audio processing pipelines using FFmpeg and FFprobe with scene detection via PySceneDetect. Handles format conversion, thumbnail generation, HLS packaging, and loudness normalization per EBU R128.

## Overview

The FFmpeg Intelligent Media Processor automates multimedia workflows by constructing optimized FFmpeg filter graphs based on input analysis from FFprobe. It performs intelligent scene detection using PySceneDetect ContentDetector to identify optimal thumbnail frames and chapter boundaries.

The skill handles adaptive bitrate HLS packaging with multiple renditions, generating compliant m3u8 playlists for streaming platforms. Audio processing includes EBU R128 loudness normalization, silence detection and trimming, and multi-track mixing with per-channel gain control.

Advanced features include hardware-accelerated encoding via NVENC, VAAPI, or VideoToolbox with automatic capability detection. The processor supports subtitle extraction from MKV containers, burn-in rendering, and WebVTT conversion. Batch processing handles entire directories with progress tracking, and failed jobs are retried with adjusted parameters. Output validation checks codec compliance, bitrate targets, and container integrity before marking jobs complete.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-intelligent-media-processor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-intelligent-media-processor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-intelligent-media-processor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-intelligent-media-processor -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-intelligent-media-processor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ffmpeg-intelligent-media-processor/
