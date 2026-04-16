---
title: "ImageMagick Batch Processor"
description: "Batch image processing using ImageMagick’s convert and mogrify commands with support for resize, crop, watermark, and format conversion. Integrates with libvips for high-performance thumbnail generation."
verification: "security_reviewed"
source: "https://github.com/ImageMagick/ImageMagick"
category:
  - "Image &amp; Creative Automation"
framework:
  - "MCP"
---

# ImageMagick Batch Processor

The ImageMagick Batch Processor automates large-scale image transformations using ImageMagick’s CLI tools (convert, mogrify, identify) and the MagickWand API. It handles batch operations including resize with aspect ratio preservation (-geometry), smart cropping (-gravity center -crop), watermark overlay (-composite), and format conversion between JPEG, PNG, WebP, AVIF, and TIFF.

The skill leverages libvips integration for high-throughput thumbnail generation, achieving 5-10x faster processing compared to pure ImageMagick for resize operations. It supports ICC color profile management (-profile sRGB.icc), EXIF metadata preservation and stripping (-strip), and progressive JPEG encoding (-interlace Plane) for web optimization.

Advanced features include batch rename with template patterns, directory watching for automated processing of new uploads, quality optimization using perceptual metrics (SSIM scoring via -compare), and parallel processing across CPU cores. Output includes processing reports with file size reduction statistics, dimension changes, and format conversion summaries.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-processor/)
