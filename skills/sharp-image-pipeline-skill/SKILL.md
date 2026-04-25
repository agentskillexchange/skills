---
title: "Sharp Image Pipeline Skill"
description: "Processes images using the Sharp npm library (libvips). Supports batch resize, format conversion (WebP/AVIF/JPEG XL), watermarking, and metadata extraction. Generates responsive image sets with srcset dimensions."
verification: "security_reviewed"
source: "https://github.com/lovell/sharp"
category:
  - "Image & Creative Automation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "lovell/sharp"
  github_stars: 32138
  npm_package: "sharp"
  npm_weekly_downloads: 52472150
---

# Sharp Image Pipeline Skill

The Sharp Image Pipeline Skill leverages the Sharp npm library (built on libvips) to give Claude fast, memory-efficient image processing capabilities. It handles single images and batch operations across directories with consistent quality and performance. Core transformations include resize (with fit modes: cover, contain, fill, inside, outside), format conversion between JPEG, PNG, WebP, AVIF, JPEG XL, and TIFF, and quality optimization with configurable compression parameters per format. The skill generates responsive image sets by producing multiple sizes with corresponding srcset markup for HTML integration. Compositing operations support watermark overlay with configurable position, opacity, and tiling. The skill handles text overlay by rendering SVG text buffers and compositing them onto images. Color manipulation includes tint, greyscale, normalisation, and modulation of brightness, saturation, and hue. Metadata extraction reads EXIF, IPTC, and XMP data from images, useful for cataloging and rights management. The skill strips or preserves metadata during processing based on configuration. Pipeline operations are chainable — a single command can resize, convert, watermark, and optimize in one pass without intermediate files. Designed for web developers optimizing image assets and content teams processing media libraries.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sharp-image-pipeline-skill/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sharp-image-pipeline-skill
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sharp-image-pipeline-skill`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sharp-image-pipeline-skill/)
