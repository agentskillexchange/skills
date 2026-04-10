---
name: ImageMagick Batch Converter CLI
description: Automates bulk image conversion using ImageMagick&#8217;s convert and
  mogrify commands with geometry expressions. Supports -density, -colorspace, and
  -profile flags for print-quality output.
verification: security_reviewed
source: https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/
category:
- Image &amp; Creative Automation
framework:
- OpenClaw
---
# ImageMagick Batch Converter CLI

The ImageMagick Batch Converter CLI automates bulk image transformation workflows using ImageMagick's command-line tools. It constructs convert pipelines with geometry expressions like -resize &#8220;1200&#215;800>&#8221; for conditional resizing, -gravity center -crop for aspect-ratio-aware cropping, and -quality 85 for output optimization.
Core operations include format conversion chains using convert input.tiff -colorspace sRGB -depth 8 output.webp, batch processing with mogrify -format png -path output/ *.tiff for in-place directory conversion, and montage for contact sheet generation from image collections. The skill handles color management through -profile sRGB.icc and -intent Perceptual for consistent color reproduction.
Advanced features include text overlay rendering with -annotate and -font flags supporting TrueType fonts, multi-layer composition via -composite with blend modes (-compose Multiply), and animated GIF creation through convert -delay 10 -loop 0 frames/*.png output.gif. It supports PDF-to-image extraction using -density 300 for high-resolution rasterization and provides histogram analysis through -format &#8220;%[fx:mean]&#8221; for automated exposure correction across batch operations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/)
