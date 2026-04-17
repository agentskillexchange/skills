---
title: "ImageMagick Batch Converter CLI"
description: "The ImageMagick Batch Converter CLI automates bulk image transformation workflows using ImageMagick’s command-line tools. It constructs convert pipelines with geometry expressions like -resize “1200×800>” for conditional resizing, -gravity center -crop for aspect-ratio-aware cropping, and -quality 85 for output optimization.\nCore operations include format conversion chains using convert input.tiff -colorspace sRGB -depth 8 output.webp, batch processing with mogrify -format png -path output/ *.tiff for in-place directory conversion, and montage for contact sheet generation from image collections. The skill handles color management through -profile sRGB.icc and -intent Perceptual for consistent color reproduction.\nAdvanced features include text overlay rendering with -annotate and -font flags supporting TrueType fonts, multi-layer composition via -composite with blend modes (-compose Multiply), and animated GIF creation through convert -delay 10 -loop 0 frames/*.png output.gif. It supports PDF-to-image extraction using -density 300 for high-resolution rasterization and provides histogram analysis through -format “%[fx:mean]” for automated exposure correction across batch operations."
verification: security_reviewed
source: "https://github.com/ImageMagick/ImageMagick"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "imagemagick/imagemagick"
  github_stars: 16152
---

# ImageMagick Batch Converter CLI

The ImageMagick Batch Converter CLI automates bulk image transformation workflows using ImageMagick’s command-line tools. It constructs convert pipelines with geometry expressions like -resize “1200×800>” for conditional resizing, -gravity center -crop for aspect-ratio-aware cropping, and -quality 85 for output optimization.
Core operations include format conversion chains using convert input.tiff -colorspace sRGB -depth 8 output.webp, batch processing with mogrify -format png -path output/ *.tiff for in-place directory conversion, and montage for contact sheet generation from image collections. The skill handles color management through -profile sRGB.icc and -intent Perceptual for consistent color reproduction.
Advanced features include text overlay rendering with -annotate and -font flags supporting TrueType fonts, multi-layer composition via -composite with blend modes (-compose Multiply), and animated GIF creation through convert -delay 10 -loop 0 frames/*.png output.gif. It supports PDF-to-image extraction using -density 300 for high-resolution rasterization and provides histogram analysis through -format “%[fx:mean]” for automated exposure correction across batch operations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/imagemagick-batch-converter-cli
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/imagemagick-batch-converter-cli` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/)
