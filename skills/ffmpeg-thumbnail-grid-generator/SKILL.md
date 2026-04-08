---
title: FFmpeg Thumbnail Grid Generator
description: The FFmpeg Thumbnail Grid Generator automates the creation of visual
  contact sheets from video files, commonly needed for media libraries, video review
  workflows, and content cataloging. It leverages FFmpeg’s tile video filter to extract
  frames at configurable intervals and arrange them into grid layouts. The tool supports
  multiple output formats including PNG, JPEG, and WebP through libvips post-processing
  for optimal compression. Users can configure grid dimensions (e.g., 4×4, 6×3), add
  burned-in timestamp overlays using FFmpeg’s drawtext filter, and apply custom styling
  to borders and padding. Batch mode processes entire directories with configurable
  concurrency via GNU Parallel. The skill integrates with S3-compatible storage via
  aws-cli for automatic upload of generated grids. It handles edge cases like variable
  frame rates, HDR tone-mapping via libplacebo, and ultra-short clips gracefully.
  Ideal for media asset management pipelines and video production teams.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ffmpeg-thumbnail-grid-generator/
category:
- Image &amp; Creative Automation
framework:
- OpenClaw
---

# FFmpeg Thumbnail Grid Generator

The FFmpeg Thumbnail Grid Generator automates the creation of visual contact sheets from video files, commonly needed for media libraries, video review workflows, and content cataloging. It leverages FFmpeg’s tile video filter to extract frames at configurable intervals and arrange them into grid layouts. The tool supports multiple output formats including PNG, JPEG, and WebP through libvips post-processing for optimal compression. Users can configure grid dimensions (e.g., 4×4, 6×3), add burned-in timestamp overlays using FFmpeg’s drawtext filter, and apply custom styling to borders and padding. Batch mode processes entire directories with configurable concurrency via GNU Parallel. The skill integrates with S3-compatible storage via aws-cli for automatic upload of generated grids. It handles edge cases like variable frame rates, HDR tone-mapping via libplacebo, and ultra-short clips gracefully. Ideal for media asset management pipelines and video production teams.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-thumbnail-grid-generator/)
