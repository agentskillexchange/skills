---
title: "ImageMagick Batch Converter CLI"
description: "Automates bulk image conversion using ImageMagick’s convert and mogrify commands with geometry expressions. Supports -density, -colorspace, and -profile flags for print-quality output."
verification: "security_reviewed"
source: "https://github.com/ImageMagick/ImageMagick"
category:
  - "Image & Creative Automation"
framework:
  - "OpenClaw"
---

# ImageMagick Batch Converter CLI

The ImageMagick Batch Converter CLI automates bulk image transformation workflows using ImageMagick’s command-line tools. It constructs convert pipelines with geometry expressions like -resize “1200×800>” for conditional resizing, -gravity center -crop for aspect-ratio-aware cropping, and -quality 85 for output optimization.


Core operations include format conversion chains using convert input.tiff -colorspace sRGB -depth 8 output.webp, batch processing with mogrify -format png -path output/ *.tiff for in-place directory conversion, and montage for contact sheet generation from image collections. The skill handles color management through -profile sRGB.icc and -intent Perceptual for consistent color reproduction.


Advanced features include text overlay rendering with -annotate and -font flags supporting TrueType fonts, multi-layer composition via -composite with blend modes (-compose Multiply), and animated GIF creation through convert -delay 10 -loop 0 frames/*.png output.gif. It supports PDF-to-image extraction using -density 300 for high-resolution rasterization and provides histogram analysis through -format “%[fx:mean]” for automated exposure correction across batch operations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/)
