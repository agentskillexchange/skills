---
title: "ImageMagick Batch Converter CLI"
description: "The ImageMagick Batch Converter CLI automates bulk image transformation workflows using ImageMagick&#8217;s command-line tools. It constructs convert pipelines with geometry expressions like -resize &#8220;1200&#215;800>&#8221; for conditional resizing, -gravity center -crop for aspect-ratio-aware cropping, and -quality 85 for output optimization. Core operations include format conversion chains using convert input.tiff -colorspace sRGB -depth 8 output.webp, batch processing with mogrify -format png -path output/ *.tiff for in-place directory conversion, and montage for contact sheet generation from image collections. The skill handles color management through -profile sRGB.icc and -intent Perceptual for consistent color reproduction. Advanced features include text overlay rendering with -annotate and -font flags supporting TrueType fonts, multi-layer composition via -composite with blend modes (-compose Multiply), and animated GIF creation through convert -delay 10 -loop 0 frames/*.png output.gif. It supports PDF-to-image extraction using -density 300 for high-resolution rasterization and provides histogram analysis through -format &#8220;%[fx:mean]&#8221; for automated exposure correction across batch operations."
source: "https://github.com/ImageMagick/ImageMagick"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "OpenClaw"
---

# ImageMagick Batch Converter CLI

The ImageMagick Batch Converter CLI automates bulk image transformation workflows using ImageMagick&#8217;s command-line tools. It constructs convert pipelines with geometry expressions like -resize &#8220;1200&#215;800>&#8221; for conditional resizing, -gravity center -crop for aspect-ratio-aware cropping, and -quality 85 for output optimization. Core operations include format conversion chains using convert input.tiff -colorspace sRGB -depth 8 output.webp, batch processing with mogrify -format png -path output/ *.tiff for in-place directory conversion, and montage for contact sheet generation from image collections. The skill handles color management through -profile sRGB.icc and -intent Perceptual for consistent color reproduction. Advanced features include text overlay rendering with -annotate and -font flags supporting TrueType fonts, multi-layer composition via -composite with blend modes (-compose Multiply), and animated GIF creation through convert -delay 10 -loop 0 frames/*.png output.gif. It supports PDF-to-image extraction using -density 300 for high-resolution rasterization and provides histogram analysis through -format &#8220;%[fx:mean]&#8221; for automated exposure correction across batch operations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/)
