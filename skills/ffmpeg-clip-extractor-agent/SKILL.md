---
title: "FFmpeg Clip Extractor"
description: "Extracts video clips and segments using FFmpeg libavformat and libavcodec APIs. Supports keyframe-accurate cutting with -ss/-to flags, stream copy mode, and re-encoding via libx264/libx265 presets."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Media &amp; Transcription"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-clip-extractor-agent/)
