---
title: "FFmpeg Thumbnail Mosaic Generator"
description: "Creates video thumbnail mosaics and sprite sheets using FFmpeg filters and the fluent-ffmpeg Node.js wrapper. Generates contact sheets, animated GIF previews, and WebVTT thumbnail tracks."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Image & Creative Automation"
framework:
  - "Claude Code"
---

# FFmpeg Thumbnail Mosaic Generator

The FFmpeg Thumbnail Mosaic Generator creates visual video summaries using FFmpeg’s powerful filter graph system accessed through the fluent-ffmpeg Node.js wrapper. It produces multiple thumbnail output formats for video platforms and media libraries.

The skill generates contact sheet mosaics by extracting frames at configurable intervals using FFmpeg’s select and tile filters, compositing them into grid layouts with timestamp overlays. It creates animated GIF previews using palettegen and paletteuse filters for optimal color quantization, and produces WebVTT thumbnail tracks compatible with HTML5 video players for scrubbing preview functionality.

Advanced features include scene-change detection using the select filter with scene scoring to extract visually distinct keyframes, thumbnail quality optimization through lanczos scaling, and batch processing across video libraries with progress tracking. The generator supports custom overlay templates with branding elements and metadata text burned into thumbnail grids. Output configurations are defined in JSON recipe files for reproducible thumbnail generation across video catalogs.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ffmpeg-thumbnail-mosaic-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ffmpeg-thumbnail-mosaic-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-thumbnail-mosaic-generator/)
