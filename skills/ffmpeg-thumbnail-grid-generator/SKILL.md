---
name: "FFmpeg Thumbnail Grid Generator"
description: "Generates contact-sheet-style thumbnail grids from video files using FFmpeg tile filter and libvips. Supports customizable grid dimensions, timestamp overlays, and batch processing across directories."
category: "Image & Creative Automation"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ffmpeg-thumbnail-grid-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ffmpeg"  # from ase_tool_match
  github_stars: 58257  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "FFmpeg/FFmpeg"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# FFmpeg Thumbnail Grid Generator

Generates contact-sheet-style thumbnail grids from video files using FFmpeg tile filter and libvips. Supports customizable grid dimensions, timestamp overlays, and batch processing across directories.

## Overview

The FFmpeg Thumbnail Grid Generator automates the creation of visual contact sheets from video files, commonly needed for media libraries, video review workflows, and content cataloging. It leverages FFmpeg’s tile video filter to extract frames at configurable intervals and arrange them into grid layouts. The tool supports multiple output formats including PNG, JPEG, and WebP through libvips post-processing for optimal compression. Users can configure grid dimensions (e.g., 4×4, 6×3), add burned-in timestamp overlays using FFmpeg’s drawtext filter, and apply custom styling to borders and padding. Batch mode processes entire directories with configurable concurrency via GNU Parallel. The skill integrates with S3-compatible storage via aws-cli for automatic upload of generated grids. It handles edge cases like variable frame rates, HDR tone-mapping via libplacebo, and ultra-short clips gracefully. Ideal for media asset management pipelines and video production teams.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-thumbnail-grid-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-thumbnail-grid-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-thumbnail-grid-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ffmpeg-thumbnail-grid-generator -a codex
```

### OpenClaw

```bash
clawhub install ffmpeg-thumbnail-grid-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ffmpeg-thumbnail-grid-generator/
