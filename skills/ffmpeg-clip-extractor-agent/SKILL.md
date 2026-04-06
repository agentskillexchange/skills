---
name: FFmpeg Clip Extractor
description: Extracts video clips and segments using FFmpeg libavformat and libavcodec
  APIs. Supports keyframe-accurate cutting with -ss/-to flags, stream copy mode, and
  re-encoding via libx264/libx265 presets.
category: "Media &amp; Transcription"
framework: Claude Code
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ffmpeg-clip-extractor-agent/"
---
# FFmpeg Clip Extractor

Extracts video clips and segments using FFmpeg libavformat and libavcodec APIs. Supports keyframe-accurate cutting with -ss/-to flags, stream copy mode, and re-encoding via libx264/libx265 presets.

FFmpeg Clip Extractor provides intelligent video segment extraction powered by FFmpeg’s core libraries. It uses -ss (seek) and -to (end position) flags with input-level seeking for keyframe-accurate cuts, falling back to output-level seeking with re-encoding when frame-exact precision is required.

The agent supports stream copy mode (-c copy) for near-instant extraction without quality loss when cuts align with keyframes. For precise cuts, it re-encodes using libx264 with CRF quality control or libx265 for HEVC output, with configurable presets from ultrafast to veryslow.

Handles multi-stream files by selecting specific video (-map 0:v:0), audio (-map 0:a:0), and subtitle streams. Supports batch extraction from timestamp lists, scene detection via select=gt(scene,0.4) filter, and thumbnail generation with -vf fps=1/60. Outputs to MP4, MKV, WebM, or GIF with proper container metadata via -movflags +faststart.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-clip-extractor-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-clip-extractor-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-clip-extractor-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-clip-extractor-agent -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-clip-extractor-agent
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-clip-extractor-agent/)
