---
name: FFmpeg Clip Extractor
description: Extracts video clips and segments using FFmpeg libavformat and libavcodec
  APIs. Supports keyframe-accurate cutting with -ss/-to flags, stream copy mode, and
  re-encoding via libx264/libx265 presets.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-clip-extractor-agent/
category:
- Media &amp; Transcription
framework:
- Claude Code
---
# FFmpeg Clip Extractor

FFmpeg Clip Extractor provides intelligent video segment extraction powered by FFmpeg's core libraries. It uses -ss (seek) and -to (end position) flags with input-level seeking for keyframe-accurate cuts, falling back to output-level seeking with re-encoding when frame-exact precision is required.
The agent supports stream copy mode (-c copy) for near-instant extraction without quality loss when cuts align with keyframes. For precise cuts, it re-encodes using libx264 with CRF quality control or libx265 for HEVC output, with configurable presets from ultrafast to veryslow.
Handles multi-stream files by selecting specific video (-map 0:v:0), audio (-map 0:a:0), and subtitle streams. Supports batch extraction from timestamp lists, scene detection via select=gt(scene,0.4) filter, and thumbnail generation with -vf fps=1/60. Outputs to MP4, MKV, WebM, or GIF with proper container metadata via -movflags +faststart.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-clip-extractor-agent/)
