---
name: "Sharp Image Pipeline Skill"
description: "Processes images using the Sharp npm library (libvips). Supports batch resize, format conversion (WebP/AVIF/JPEG XL), watermarking, and metadata extraction. Generates responsive image sets with srcset dimensions."
category: "Image & Creative Automation"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sharp-image-pipeline-skill/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sharp"  # from ase_tool_match
  github_stars: 32068  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 54450041  # from ase_npm_downloads
  github_repo: "lovell/sharp"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Sharp Image Pipeline Skill

Processes images using the Sharp npm library (libvips). Supports batch resize, format conversion (WebP/AVIF/JPEG XL), watermarking, and metadata extraction. Generates responsive image sets with srcset dimensions.

## Overview

The Sharp Image Pipeline Skill leverages the Sharp npm library (built on libvips) to give Claude fast, memory-efficient image processing capabilities. It handles single images and batch operations across directories with consistent quality and performance.

Core transformations include resize (with fit modes: cover, contain, fill, inside, outside), format conversion between JPEG, PNG, WebP, AVIF, JPEG XL, and TIFF, and quality optimization with configurable compression parameters per format. The skill generates responsive image sets by producing multiple sizes with corresponding srcset markup for HTML integration.

Compositing operations support watermark overlay with configurable position, opacity, and tiling. The skill handles text overlay by rendering SVG text buffers and compositing them onto images. Color manipulation includes tint, greyscale, normalisation, and modulation of brightness, saturation, and hue.

Metadata extraction reads EXIF, IPTC, and XMP data from images, useful for cataloging and rights management. The skill strips or preserves metadata during processing based on configuration. Pipeline operations are chainable — a single command can resize, convert, watermark, and optimize in one pass without intermediate files. Designed for web developers optimizing image assets and content teams processing media libraries.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sharp-image-pipeline-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sharp-image-pipeline-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sharp-image-pipeline-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sharp-image-pipeline-skill -a codex
```

### OpenClaw

```bash
clawhub install sharp-image-pipeline-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sharp-image-pipeline-skill/
