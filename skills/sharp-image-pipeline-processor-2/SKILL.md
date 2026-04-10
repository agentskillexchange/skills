---
name: "Sharp Image Pipeline Processor"
description: "Builds composable image transformation pipelines using the Sharp library with operations like resize(), composite(), and toFormat(). Leverages libvips bindings for high-performance batch processing."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sharp-image-pipeline-processor-2/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Code"
---

# Sharp Image Pipeline Processor

The Sharp Image Pipeline Processor creates composable image transformation workflows using the Sharp library's fluent API backed by libvips native bindings. It chains operations like sharp(input).resize({ width, height, fit: &#8220;cover&#8221; }).composite([{ input: watermark, gravity: &#8220;southeast&#8221; }]).toFormat(&#8220;webp&#8221;, { quality: 80 }) for efficient multi-step processing.
Core capabilities include intelligent resizing with sharp.fit options (cover, contain, fill, inside, outside), metadata-aware orientation correction via rotate() with EXIF auto-rotation, and color space manipulation through toColorspace() for print-ready CMYK output. The processor handles batch operations using sharp.concurrency() tuning for optimal CPU utilization.
Advanced features include SVG overlay compositing with blend modes, animated GIF/WebP processing through the pages option for frame manipulation, and tile generation via .tile({ size: 256 }) for deep-zoom image viewers. It supports ICC profile embedding through withMetadata({ icc }) and provides streaming pipelines via sharp().pipe() for memory-efficient processing of large images without buffering entire files.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sharp-image-pipeline-processor-2/)
