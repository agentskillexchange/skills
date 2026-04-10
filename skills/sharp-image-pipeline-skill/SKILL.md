---
title: "Sharp Image Pipeline Skill"
description: "Processes images using the Sharp npm library (libvips). Supports batch resize, format conversion (WebP/AVIF/JPEG XL), watermarking, and metadata extraction. Generates responsive image sets with srcset dimensions."
slug: "sharp-image-pipeline-skill"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sharp-image-pipeline-skill/"
---

# Sharp Image Pipeline Skill

Processes images using the Sharp npm library (libvips). Supports batch resize, format conversion (WebP/AVIF/JPEG XL), watermarking, and metadata extraction. Generates responsive image sets with srcset dimensions.

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
clawhub install sharp-image-pipeline-skill
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Sharp Image Pipeline Skill leverages the Sharp npm library (built on libvips) to give Claude fast, memory-efficient image processing capabilities. It handles single images and batch operations across directories with consistent quality and performance.
Core transformations include resize (with fit modes: cover, contain, fill, inside, outside), format conversion between JPEG, PNG, WebP, AVIF, JPEG XL, and TIFF, and quality optimization with configurable compression parameters per format. The skill generates responsive image sets by producing multiple sizes with corresponding srcset markup for HTML integration.
Compositing operations support watermark overlay with configurable position, opacity, and tiling. The skill handles text overlay by rendering SVG text buffers and compositing them onto images. Color manipulation includes tint, greyscale, normalisation, and modulation of brightness, saturation, and hue.
Metadata extraction reads EXIF, IPTC, and XMP data from images, useful for cataloging and rights management. The skill strips or preserves metadata during processing based on configuration. Pipeline operations are chainable — a single command can resize, convert, watermark, and optimize in one pass without intermediate files. Designed for web developers optimizing image assets and content teams processing media libraries.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sharp-image-pipeline-skill/)
