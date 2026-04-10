---
name: FFmpeg Thumbnail Grid Generator
description: Generates contact-sheet-style thumbnail grids from video files using
  FFmpeg tile filter and libvips. Supports customizable grid dimensions, timestamp
  overlays, and batch processing across directories.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-thumbnail-grid-generator/
category:
- Image &amp; Creative Automation
framework:
- OpenClaw
---
# FFmpeg Thumbnail Grid Generator

The FFmpeg Thumbnail Grid Generator automates the creation of visual contact sheets from video files, commonly needed for media libraries, video review workflows, and content cataloging. It leverages FFmpeg's tile video filter to extract frames at configurable intervals and arrange them into grid layouts. The tool supports multiple output formats including PNG, JPEG, and WebP through libvips post-processing for optimal compression. Users can configure grid dimensions (e.g., 4&#215;4, 6&#215;3), add burned-in timestamp overlays using FFmpeg's drawtext filter, and apply custom styling to borders and padding. Batch mode processes entire directories with configurable concurrency via GNU Parallel. The skill integrates with S3-compatible storage via aws-cli for automatic upload of generated grids. It handles edge cases like variable frame rates, HDR tone-mapping via libplacebo, and ultra-short clips gracefully. Ideal for media asset management pipelines and video production teams.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-thumbnail-grid-generator/)
