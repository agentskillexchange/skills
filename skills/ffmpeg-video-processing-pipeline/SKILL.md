---
name: "FFmpeg Video Processing Pipeline"
description: "Builds complex FFmpeg filtergraph chains for batch video transcoding, thumbnail sprite generation, and HLS adaptive bitrate packaging. Supports NVIDIA NVENC hardware acceleration and HDR tone mapping."
category: "Image &amp; Creative Automation"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ffmpeg-video-processing-pipeline/"
---
# FFmpeg Video Processing Pipeline

Builds complex FFmpeg filtergraph chains for batch video transcoding, thumbnail sprite generation, and HLS adaptive bitrate packaging. Supports NVIDIA NVENC hardware acceleration and HDR tone mapping.

The FFmpeg Video Processing Pipeline constructs sophisticated filtergraph chains for professional video workflows. It handles batch transcoding across codecs (H.264, H.265/HEVC, AV1, VP9) with configurable CRF/bitrate targets, two-pass encoding, and per-title encoding optimization that selects bitrate ladders based on content complexity analysis.

Hardware acceleration is supported via NVIDIA NVENC, Intel QuickSync (QSV), and Apple VideoToolbox, with automatic fallback to software encoding when GPU resources are unavailable. HDR workflows include PQ-to-HLG conversion, HDR10+ dynamic metadata passthrough, and Dolby Vision profile 8.1 remuxing.

The skill generates thumbnail sprite sheets (WebVTT + contact sheet images) for video player scrubbing, creates HLS and DASH adaptive streaming packages with proper segment alignment, and handles audio normalization via EBU R128 loudness standards. Subtitle extraction (SRT, ASS, VobSub OCR) and burn-in with configurable styling round out the post-production capabilities. Scene detection via ffprobe enables intelligent chapter marker generation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-video-processing-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-video-processing-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-video-processing-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-video-processing-pipeline -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-video-processing-pipeline
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-video-processing-pipeline/)
