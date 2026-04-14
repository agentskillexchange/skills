---
title: "FFmpeg Thumbnail Grid Generator"
description: "Generates contact-sheet-style thumbnail grids from video files using FFmpeg tile filter and libvips. Supports customizable grid dimensions, timestamp overlays, and batch processing across directories."
verification: security_reviewed
source: "https://github.com/FFmpeg/FFmpeg"
category:
  - "Image &amp; Creative Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "ffmpeg/ffmpeg"
  github_stars: 58972
---

# FFmpeg Thumbnail Grid Generator

The FFmpeg Thumbnail Grid Generator automates the creation of visual contact sheets from video files, commonly needed for media libraries, video review workflows, and content cataloging. It leverages FFmpeg’s tile video filter to extract frames at configurable intervals and arrange them into grid layouts. The tool supports multiple output formats including PNG, JPEG, and WebP through libvips post-processing for optimal compression. Users can configure grid dimensions (e.g., 4×4, 6×3), add burned-in timestamp overlays using FFmpeg’s drawtext filter, and apply custom styling to borders and padding. Batch mode processes entire directories with configurable concurrency via GNU Parallel. The skill integrates with S3-compatible storage via aws-cli for automatic upload of generated grids. It handles edge cases like variable frame rates, HDR tone-mapping via libplacebo, and ultra-short clips gracefully. Ideal for media asset management pipelines and video production teams.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-thumbnail-grid-generator/)
