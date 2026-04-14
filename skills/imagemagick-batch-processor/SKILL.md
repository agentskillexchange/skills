---
title: "ImageMagick Batch Processor"
description: "Batch image processing using ImageMagick’s convert and mogrify commands with support for resize, crop, watermark, and format conversion. Integrates with libvips for high-performance thumbnail generation."
verification: security_reviewed
source: "https://github.com/ImageMagick/ImageMagick"
category:
  - "Image &amp; Creative Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "imagemagick/imagemagick"
  github_stars: 16152
---

# ImageMagick Batch Processor

The ImageMagick Batch Processor automates large-scale image transformations using ImageMagick’s CLI tools (convert, mogrify, identify) and the MagickWand API. It handles batch operations including resize with aspect ratio preservation (-geometry), smart cropping (-gravity center -crop), watermark overlay (-composite), and format conversion between JPEG, PNG, WebP, AVIF, and TIFF.

The skill leverages libvips integration for high-throughput thumbnail generation, achieving 5-10x faster processing compared to pure ImageMagick for resize operations. It supports ICC color profile management (-profile sRGB.icc), EXIF metadata preservation and stripping (-strip), and progressive JPEG encoding (-interlace Plane) for web optimization.

Advanced features include batch rename with template patterns, directory watching for automated processing of new uploads, quality optimization using perceptual metrics (SSIM scoring via -compare), and parallel processing across CPU cores. Output includes processing reports with file size reduction statistics, dimension changes, and format conversion summaries.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-processor/)
