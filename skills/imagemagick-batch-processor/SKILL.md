---
title: ImageMagick Batch Processor
description: The ImageMagick Batch Processor automates large-scale image transformations
  using ImageMagick’s CLI tools (convert, mogrify, identify) and the MagickWand API.
  It handles batch operations including resize with aspect ratio preservation (-geometry),
  smart cropping (-gravity center -crop), watermark overlay (-composite), and format
  conversion between JPEG, PNG, WebP, AVIF, and TIFF. The skill leverages libvips
  integration for high-throughput thumbnail generation, achieving 5-10x faster processing
  compared to pure ImageMagick for resize operations. It supports ICC color profile
  management (-profile sRGB.icc), EXIF metadata preservation and stripping (-strip),
  and progressive JPEG encoding (-interlace Plane) for web optimization. Advanced
  features include batch rename with template patterns, directory watching for automated
  processing of new uploads, quality optimization using perceptual metrics (SSIM scoring
  via -compare), and parallel processing across CPU cores. Output includes processing
  reports with file size reduction statistics, dimension changes, and format conversion
  summaries.
verification: security_reviewed
source: https://agentskillexchange.com/skills/imagemagick-batch-processor/
category:
- Image &amp; Creative Automation
framework:
- MCP
---

# ImageMagick Batch Processor

The ImageMagick Batch Processor automates large-scale image transformations using ImageMagick’s CLI tools (convert, mogrify, identify) and the MagickWand API. It handles batch operations including resize with aspect ratio preservation (-geometry), smart cropping (-gravity center -crop), watermark overlay (-composite), and format conversion between JPEG, PNG, WebP, AVIF, and TIFF. The skill leverages libvips integration for high-throughput thumbnail generation, achieving 5-10x faster processing compared to pure ImageMagick for resize operations. It supports ICC color profile management (-profile sRGB.icc), EXIF metadata preservation and stripping (-strip), and progressive JPEG encoding (-interlace Plane) for web optimization. Advanced features include batch rename with template patterns, directory watching for automated processing of new uploads, quality optimization using perceptual metrics (SSIM scoring via -compare), and parallel processing across CPU cores. Output includes processing reports with file size reduction statistics, dimension changes, and format conversion summaries.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-processor/)
