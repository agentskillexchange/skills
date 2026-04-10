---
title: "ImageMagick Batch Converter CLI"
description: "Automates bulk image conversion using ImageMagick’s convert and mogrify commands with geometry expressions. Supports -density, -colorspace, and -profile flags for print-quality output."
slug: "imagemagick-batch-converter-cli"
category:
  - "Image &amp; Creative Automation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/"
---

# ImageMagick Batch Converter CLI

Automates bulk image conversion using ImageMagick’s convert and mogrify commands with geometry expressions. Supports -density, -colorspace, and -profile flags for print-quality output.

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
clawhub install imagemagick-batch-converter-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ImageMagick Batch Converter CLI automates bulk image transformation workflows using ImageMagick’s command-line tools. It constructs convert pipelines with geometry expressions like -resize “1200×800>” for conditional resizing, -gravity center -crop for aspect-ratio-aware cropping, and -quality 85 for output optimization.
Core operations include format conversion chains using convert input.tiff -colorspace sRGB -depth 8 output.webp, batch processing with mogrify -format png -path output/ *.tiff for in-place directory conversion, and montage for contact sheet generation from image collections. The skill handles color management through -profile sRGB.icc and -intent Perceptual for consistent color reproduction.
Advanced features include text overlay rendering with -annotate and -font flags supporting TrueType fonts, multi-layer composition via -composite with blend modes (-compose Multiply), and animated GIF creation through convert -delay 10 -loop 0 frames/*.png output.gif. It supports PDF-to-image extraction using -density 300 for high-resolution rasterization and provides histogram analysis through -format “%[fx:mean]” for automated exposure correction across batch operations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/)
