---
title: "FFmpeg Thumbnail Mosaic Generator"
description: "The FFmpeg Thumbnail Mosaic Generator creates visual video summaries using FFmpeg&#8217;s powerful filter graph system accessed through the fluent-ffmpeg Node.js wrapper. It produces multiple thumbnail output formats for video platforms and media libraries. The skill generates contact sheet mosaics by extracting frames at configurable intervals using FFmpeg&#8217;s select and tile filters, compositing them into grid layouts with timestamp overlays. It creates animated GIF previews using palettegen and paletteuse filters for optimal color quantization, and produces WebVTT thumbnail tracks compatible with HTML5 video players for scrubbing preview functionality. Advanced features include scene-change detection using the select filter with scene scoring to extract visually distinct keyframes, thumbnail quality optimization through lanczos scaling, and batch processing across video libraries with progress tracking. The generator supports custom overlay templates with branding elements and metadata text burned into thumbnail grids. Output configurations are defined in JSON recipe files for reproducible thumbnail generation across video catalogs."
source: "https://github.com/FFmpeg/FFmpeg"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "ffmpeg/ffmpeg"
  github_stars: 58972
---

# FFmpeg Thumbnail Mosaic Generator

The FFmpeg Thumbnail Mosaic Generator creates visual video summaries using FFmpeg&#8217;s powerful filter graph system accessed through the fluent-ffmpeg Node.js wrapper. It produces multiple thumbnail output formats for video platforms and media libraries. The skill generates contact sheet mosaics by extracting frames at configurable intervals using FFmpeg&#8217;s select and tile filters, compositing them into grid layouts with timestamp overlays. It creates animated GIF previews using palettegen and paletteuse filters for optimal color quantization, and produces WebVTT thumbnail tracks compatible with HTML5 video players for scrubbing preview functionality. Advanced features include scene-change detection using the select filter with scene scoring to extract visually distinct keyframes, thumbnail quality optimization through lanczos scaling, and batch processing across video libraries with progress tracking. The generator supports custom overlay templates with branding elements and metadata text burned into thumbnail grids. Output configurations are defined in JSON recipe files for reproducible thumbnail generation across video catalogs.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ffmpeg-thumbnail-mosaic-generator/)
