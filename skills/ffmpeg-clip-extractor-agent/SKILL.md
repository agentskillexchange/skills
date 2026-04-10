---
title: "FFmpeg Clip Extractor"
description: "Extracts video clips and segments using FFmpeg libavformat and libavcodec APIs. Supports keyframe-accurate cutting with -ss/-to flags, stream copy mode, and re-encoding via libx264/libx265 presets."
slug: "ffmpeg-clip-extractor-agent"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ffmpeg-clip-extractor-agent/"
listed: true
---

# FFmpeg Clip Extractor

Extracts video clips and segments using FFmpeg libavformat and libavcodec APIs. Supports keyframe-accurate cutting with -ss/-to flags, stream copy mode, and re-encoding via libx264/libx265 presets.

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
clawhub install ffmpeg-clip-extractor-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

FFmpeg Clip Extractor provides intelligent video segment extraction powered by FFmpeg’s core libraries. It uses -ss (seek) and -to (end position) flags with input-level seeking for keyframe-accurate cuts, falling back to output-level seeking with re-encoding when frame-exact precision is required.
The agent supports stream copy mode (-c copy) for near-instant extraction without quality loss when cuts align with keyframes. For precise cuts, it re-encodes using libx264 with CRF quality control or libx265 for HEVC output, with configurable presets from ultrafast to veryslow.
Handles multi-stream files by selecting specific video (-map 0:v:0), audio (-map 0:a:0), and subtitle streams. Supports batch extraction from timestamp lists, scene detection via select=gt(scene,0.4) filter, and thumbnail generation with -vf fps=1/60. Outputs to MP4, MKV, WebM, or GIF with proper container metadata via -movflags +faststart.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-clip-extractor-agent/)
