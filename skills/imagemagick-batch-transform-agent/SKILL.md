---
title: "ImageMagick Batch Transform Agent"
description: "Automates ImageMagick convert and mogrify operations for bulk image processing including responsive srcset generation, WebP/AVIF conversion, and ICC color profile management with Little CMS integration."
verification: security_reviewed
source: "https://github.com/ImageMagick/ImageMagick"
category:
  - "Image & Creative Automation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "imagemagick/imagemagick"
  github_stars: 16152
---

# ImageMagick Batch Transform Agent

The ImageMagick Batch Transform Agent orchestrates complex image manipulation workflows using ImageMagick 7 command-line tools (magick convert, mogrify, composite). It generates responsive image srcsets with configurable breakpoints, outputting WebP, AVIF, and JPEG fallbacks with optimal quality settings determined by SSIM perceptual analysis.

Color management leverages Little CMS (LCMS2) for ICC profile conversions between sRGB, Adobe RGB, and CMYK color spaces, ensuring print-ready output. The skill handles EXIF metadata preservation or stripping based on privacy requirements, auto-orients images from camera rotation tags, and applies smart cropping using entropy-based region detection.

Batch operations support glob patterns, recursive directory traversal, and parallel processing via GNU Parallel for throughput on multi-core systems. Watermark compositing uses alpha channel blending with configurable opacity and positioning. The agent generates contact sheets, animated GIF assembly from frame sequences, and SVG-to-raster conversion at arbitrary DPI for print workflows. Processing manifests in JSON track all transformations for audit compliance.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/imagemagick-batch-transform-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/imagemagick-batch-transform-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-transform-agent/)
