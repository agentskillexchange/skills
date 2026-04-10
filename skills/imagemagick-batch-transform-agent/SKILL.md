---
name: ImageMagick Batch Transform Agent
description: Automates ImageMagick convert and mogrify operations for bulk image processing
  including responsive srcset generation, WebP/AVIF conversion, and ICC color profile
  management with Little CMS integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/imagemagick-batch-transform-agent/
category:
- Image &amp; Creative Automation
framework:
- Cursor
---
# ImageMagick Batch Transform Agent

The ImageMagick Batch Transform Agent orchestrates complex image manipulation workflows using ImageMagick 7 command-line tools (magick convert, mogrify, composite). It generates responsive image srcsets with configurable breakpoints, outputting WebP, AVIF, and JPEG fallbacks with optimal quality settings determined by SSIM perceptual analysis.
Color management leverages Little CMS (LCMS2) for ICC profile conversions between sRGB, Adobe RGB, and CMYK color spaces, ensuring print-ready output. The skill handles EXIF metadata preservation or stripping based on privacy requirements, auto-orients images from camera rotation tags, and applies smart cropping using entropy-based region detection.
Batch operations support glob patterns, recursive directory traversal, and parallel processing via GNU Parallel for throughput on multi-core systems. Watermark compositing uses alpha channel blending with configurable opacity and positioning. The agent generates contact sheets, animated GIF assembly from frame sequences, and SVG-to-raster conversion at arbitrary DPI for print workflows. Processing manifests in JSON track all transformations for audit compliance.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-transform-agent/)
