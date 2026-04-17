---
title: "FFmpeg Clip Extractor"
description: "FFmpeg Clip Extractor provides intelligent video segment extraction powered by FFmpeg’s core libraries. It uses -ss (seek) and -to (end position) flags with input-level seeking for keyframe-accurate cuts, falling back to output-level seeking with re-encoding when frame-exact precision is required.\nThe agent supports stream copy mode (-c copy) for near-instant extraction without quality loss when cuts align with keyframes. For precise cuts, it re-encodes using libx264 with CRF quality control or libx265 for HEVC output, with configurable presets from ultrafast to veryslow.\nHandles multi-stream files by selecting specific video (-map 0:v:0), audio (-map 0:a:0), and subtitle streams. Supports batch extraction from timestamp lists, scene detection via select=gt(scene,0.4) filter, and thumbnail generation with -vf fps=1/60. Outputs to MP4, MKV, WebM, or GIF with proper container metadata via -movflags +faststart."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "ffmpeg/ffmpeg"
  github_stars: 58972
---

# FFmpeg Clip Extractor

FFmpeg Clip Extractor provides intelligent video segment extraction powered by FFmpeg’s core libraries. It uses -ss (seek) and -to (end position) flags with input-level seeking for keyframe-accurate cuts, falling back to output-level seeking with re-encoding when frame-exact precision is required.
The agent supports stream copy mode (-c copy) for near-instant extraction without quality loss when cuts align with keyframes. For precise cuts, it re-encodes using libx264 with CRF quality control or libx265 for HEVC output, with configurable presets from ultrafast to veryslow.
Handles multi-stream files by selecting specific video (-map 0:v:0), audio (-map 0:a:0), and subtitle streams. Supports batch extraction from timestamp lists, scene detection via select=gt(scene,0.4) filter, and thumbnail generation with -vf fps=1/60. Outputs to MP4, MKV, WebM, or GIF with proper container metadata via -movflags +faststart.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ffmpeg-clip-extractor-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ffmpeg-clip-extractor-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-clip-extractor-agent/)
