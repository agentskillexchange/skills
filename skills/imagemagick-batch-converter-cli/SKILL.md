---
title: ImageMagick Batch Converter CLI
description: The ImageMagick Batch Converter CLI automates bulk image transformation
  workflows using ImageMagick’s command-line tools. It constructs convert pipelines
  with geometry expressions like -resize “1200×800>” for conditional resizing, -gravity
  center -crop for aspect-ratio-aware cropping, and -quality 85 for output optimization.
  Core operations include format conversion chains using convert input.tiff -colorspace
  sRGB -depth 8 output.webp, batch processing with mogrify -format png -path output/
  *.tiff for in-place directory conversion, and montage for contact sheet generation
  from image collections. The skill handles color management through -profile sRGB.icc
  and -intent Perceptual for consistent color reproduction. Advanced features include
  text overlay rendering with -annotate and -font flags supporting TrueType fonts,
  multi-layer composition via -composite with blend modes (-compose Multiply), and
  animated GIF creation through convert -delay 10 -loop 0 frames/*.png output.gif.
  It supports PDF-to-image extraction using -density 300 for high-resolution rasterization
  and provides histogram analysis through -format “%[fx:mean]” for automated exposure
  correction across batch operations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/
category:
- Image &amp; Creative Automation
framework:
- OpenClaw
---

# ImageMagick Batch Converter CLI

The ImageMagick Batch Converter CLI automates bulk image transformation workflows using ImageMagick’s command-line tools. It constructs convert pipelines with geometry expressions like -resize “1200×800>” for conditional resizing, -gravity center -crop for aspect-ratio-aware cropping, and -quality 85 for output optimization. Core operations include format conversion chains using convert input.tiff -colorspace sRGB -depth 8 output.webp, batch processing with mogrify -format png -path output/ *.tiff for in-place directory conversion, and montage for contact sheet generation from image collections. The skill handles color management through -profile sRGB.icc and -intent Perceptual for consistent color reproduction. Advanced features include text overlay rendering with -annotate and -font flags supporting TrueType fonts, multi-layer composition via -composite with blend modes (-compose Multiply), and animated GIF creation through convert -delay 10 -loop 0 frames/*.png output.gif. It supports PDF-to-image extraction using -density 300 for high-resolution rasterization and provides histogram analysis through -format “%[fx:mean]” for automated exposure correction across batch operations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/)
