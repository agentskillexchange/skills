---
title: "FFmpeg Thumbnail Mosaic Generator"
description: "Creates video thumbnail mosaics and sprite sheets using FFmpeg filters and the fluent-ffmpeg Node.js wrapper. Generates contact sheets, animated GIF previews, and WebVTT thumbnail tracks."
slug: "ffmpeg-thumbnail-mosaic-generator"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ffmpeg-thumbnail-mosaic-generator/"
listed: true
---

# FFmpeg Thumbnail Mosaic Generator

Creates video thumbnail mosaics and sprite sheets using FFmpeg filters and the fluent-ffmpeg Node.js wrapper. Generates contact sheets, animated GIF previews, and WebVTT thumbnail tracks.

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
clawhub install ffmpeg-thumbnail-mosaic-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The FFmpeg Thumbnail Mosaic Generator creates visual video summaries using FFmpeg’s powerful filter graph system accessed through the fluent-ffmpeg Node.js wrapper. It produces multiple thumbnail output formats for video platforms and media libraries.
The skill generates contact sheet mosaics by extracting frames at configurable intervals using FFmpeg’s select and tile filters, compositing them into grid layouts with timestamp overlays. It creates animated GIF previews using palettegen and paletteuse filters for optimal color quantization, and produces WebVTT thumbnail tracks compatible with HTML5 video players for scrubbing preview functionality.
Advanced features include scene-change detection using the select filter with scene scoring to extract visually distinct keyframes, thumbnail quality optimization through lanczos scaling, and batch processing across video libraries with progress tracking. The generator supports custom overlay templates with branding elements and metadata text burned into thumbnail grids. Output configurations are defined in JSON recipe files for reproducible thumbnail generation across video catalogs.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-thumbnail-mosaic-generator/)
