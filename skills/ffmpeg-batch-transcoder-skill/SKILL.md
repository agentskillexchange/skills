---
name: FFmpeg Batch Transcoder
description: Batch transcode media files using FFmpeg CLI with preset profiles for
  web, mobile, and broadcast delivery. Supports hardware-accelerated encoding via
  NVENC/VAAPI and automated quality analysis with VMAF scoring.
category: "Media &amp; Transcription"
framework: Cursor
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ffmpeg-batch-transcoder-skill/"
---
# FFmpeg Batch Transcoder

Batch transcode media files using FFmpeg CLI with preset profiles for web, mobile, and broadcast delivery. Supports hardware-accelerated encoding via NVENC/VAAPI and automated quality analysis with VMAF scoring.

Automate media transcoding workflows using FFmpeg command-line tools with configurable preset profiles optimized for different delivery targets.

This skill wraps FFmpeg and FFprobe to analyze input media, select appropriate encoding parameters, and batch-process multiple files in parallel. Preset profiles include web-optimized H.264/AAC at various bitrates, mobile-friendly HEVC with adaptive bitrate laddering, and broadcast-spec ProRes/DNxHR for post-production handoff.

Hardware acceleration is supported via NVIDIA NVENC, Intel VAAPI, and Apple VideoToolbox backends, with automatic fallback to software encoding when GPU resources are unavailable. The skill detects available hardware encoders at runtime and selects the optimal pipeline.

Quality validation runs VMAF perceptual scoring against source material to verify encoding quality meets configured thresholds. Failed encodes are automatically retried with adjusted CRF/bitrate parameters. Output includes detailed logs with per-file encoding statistics, compression ratios, and VMAF scores for quality assurance review.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-batch-transcoder-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-batch-transcoder-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-batch-transcoder-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-batch-transcoder-skill -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-batch-transcoder-skill
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-batch-transcoder-skill/)
