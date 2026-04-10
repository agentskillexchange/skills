---
name: "Sharp Image Pipeline Skill"
description: "Processes images using the Sharp npm library (libvips). Supports batch resize, format conversion (WebP/AVIF/JPEG XL), watermarking, and metadata extraction. Generates responsive image sets with srcset dimensions."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sharp-image-pipeline-skill/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Code"
---

# Sharp Image Pipeline Skill

The Sharp Image Pipeline Skill leverages the Sharp npm library (built on libvips) to give Claude fast, memory-efficient image processing capabilities. It handles single images and batch operations across directories with consistent quality and performance.
Core transformations include resize (with fit modes: cover, contain, fill, inside, outside), format conversion between JPEG, PNG, WebP, AVIF, JPEG XL, and TIFF, and quality optimization with configurable compression parameters per format. The skill generates responsive image sets by producing multiple sizes with corresponding srcset markup for HTML integration.
Compositing operations support watermark overlay with configurable position, opacity, and tiling. The skill handles text overlay by rendering SVG text buffers and compositing them onto images. Color manipulation includes tint, greyscale, normalisation, and modulation of brightness, saturation, and hue.
Metadata extraction reads EXIF, IPTC, and XMP data from images, useful for cataloging and rights management. The skill strips or preserves metadata during processing based on configuration. Pipeline operations are chainable — a single command can resize, convert, watermark, and optimize in one pass without intermediate files. Designed for web developers optimizing image assets and content teams processing media libraries.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sharp-image-pipeline-skill/)
