---
name: FFmpeg Thumbnail Mosaic Generator
description: Creates video thumbnail mosaics and sprite sheets using FFmpeg filters
  and the fluent-ffmpeg Node.js wrapper. Generates contact sheets, animated GIF previews,
  and WebVTT thumbnail tracks.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-thumbnail-mosaic-generator/
category:
- Image &amp; Creative Automation
framework:
- Claude Code
---
# FFmpeg Thumbnail Mosaic Generator

The FFmpeg Thumbnail Mosaic Generator creates visual video summaries using FFmpeg's powerful filter graph system accessed through the fluent-ffmpeg Node.js wrapper. It produces multiple thumbnail output formats for video platforms and media libraries.
The skill generates contact sheet mosaics by extracting frames at configurable intervals using FFmpeg's select and tile filters, compositing them into grid layouts with timestamp overlays. It creates animated GIF previews using palettegen and paletteuse filters for optimal color quantization, and produces WebVTT thumbnail tracks compatible with HTML5 video players for scrubbing preview functionality.
Advanced features include scene-change detection using the select filter with scene scoring to extract visually distinct keyframes, thumbnail quality optimization through lanczos scaling, and batch processing across video libraries with progress tracking. The generator supports custom overlay templates with branding elements and metadata text burned into thumbnail grids. Output configurations are defined in JSON recipe files for reproducible thumbnail generation across video catalogs.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-thumbnail-mosaic-generator/)
