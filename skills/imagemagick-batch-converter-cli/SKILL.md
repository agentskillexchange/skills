---
name: "ImageMagick Batch Converter CLI"
description: "Automates bulk image conversion using ImageMagick's convert and mogrify commands with geometry expressions. Supports -density, -colorspace, and -profile flags for print-quality output."
category: "Image &amp; Creative Automation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/"
---
# ImageMagick Batch Converter CLI

Automates bulk image conversion using ImageMagick's convert and mogrify commands with geometry expressions. Supports -density, -colorspace, and -profile flags for print-quality output.

## Overview

The ImageMagick Batch Converter CLI automates bulk image transformation workflows using ImageMagick's command-line tools. It constructs convert pipelines with geometry expressions like -resize "1200&#215;800>" for conditional resizing, -gravity center -crop for aspect-ratio-aware cropping, and -quality 85 for output optimization.

Core operations include format conversion chains using convert input.tiff -colorspace sRGB -depth 8 output.webp, batch processing with mogrify -format png -path output/ *.tiff for in-place directory conversion, and montage for contact sheet generation from image collections. The skill handles color management through -profile sRGB.icc and -intent Perceptual for consistent color reproduction.

Advanced features include text overlay rendering with -annotate and -font flags supporting TrueType fonts, multi-layer composition via -composite with blend modes (-compose Multiply), and animated GIF creation through convert -delay 10 -loop 0 frames/*.png output.gif. It supports PDF-to-image extraction using -density 300 for high-resolution rasterization and provides histogram analysis through -format "%[fx:mean]" for automated exposure correction across batch operations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-converter-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-converter-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-converter-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-converter-cli -a codex
```

### OpenClaw

```bash
clawhub install imagemagick-batch-converter-cli
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/)
