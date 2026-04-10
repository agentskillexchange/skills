---
title: "FFmpeg Thumbnail Grid Generator"
description: "Generates contact-sheet-style thumbnail grids from video files using FFmpeg tile filter and libvips. Supports customizable grid dimensions, timestamp overlays, and batch processing across directories."
slug: "ffmpeg-thumbnail-grid-generator"
category:
  - "Image &amp; Creative Automation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ffmpeg-thumbnail-grid-generator/"
listed: true
---

# FFmpeg Thumbnail Grid Generator

Generates contact-sheet-style thumbnail grids from video files using FFmpeg tile filter and libvips. Supports customizable grid dimensions, timestamp overlays, and batch processing across directories.

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
clawhub install ffmpeg-thumbnail-grid-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The FFmpeg Thumbnail Grid Generator automates the creation of visual contact sheets from video files, commonly needed for media libraries, video review workflows, and content cataloging. It leverages FFmpeg’s tile video filter to extract frames at configurable intervals and arrange them into grid layouts. The tool supports multiple output formats including PNG, JPEG, and WebP through libvips post-processing for optimal compression. Users can configure grid dimensions (e.g., 4×4, 6×3), add burned-in timestamp overlays using FFmpeg’s drawtext filter, and apply custom styling to borders and padding. Batch mode processes entire directories with configurable concurrency via GNU Parallel. The skill integrates with S3-compatible storage via aws-cli for automatic upload of generated grids. It handles edge cases like variable frame rates, HDR tone-mapping via libplacebo, and ultra-short clips gracefully. Ideal for media asset management pipelines and video production teams.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-thumbnail-grid-generator/)
