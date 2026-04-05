---
name: "ImageMagick Batch Processor"
description: "Batch image processing using ImageMagick’s convert and mogrify commands with support for resize, crop, watermark, and format conversion. Integrates with libvips for high-performance thumbnail generation."
category: "Image &amp; Creative Automation"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/imagemagick-batch-processor/"
---
# ImageMagick Batch Processor

Batch image processing using ImageMagick’s convert and mogrify commands with support for resize, crop, watermark, and format conversion. Integrates with libvips for high-performance thumbnail generation.

The ImageMagick Batch Processor automates large-scale image transformations using ImageMagick’s CLI tools (convert, mogrify, identify) and the MagickWand API. It handles batch operations including resize with aspect ratio preservation (-geometry), smart cropping (-gravity center -crop), watermark overlay (-composite), and format conversion between JPEG, PNG, WebP, AVIF, and TIFF.

The skill leverages libvips integration for high-throughput thumbnail generation, achieving 5-10x faster processing compared to pure ImageMagick for resize operations. It supports ICC color profile management (-profile sRGB.icc), EXIF metadata preservation and stripping (-strip), and progressive JPEG encoding (-interlace Plane) for web optimization.

Advanced features include batch rename with template patterns, directory watching for automated processing of new uploads, quality optimization using perceptual metrics (SSIM scoring via -compare), and parallel processing across CPU cores. Output includes processing reports with file size reduction statistics, dimension changes, and format conversion summaries.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-processor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-processor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-processor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-processor -a codex
```

### OpenClaw

```bash
clawhub install imagemagick-batch-processor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-processor/)
