---
title: "ImageMagick Batch Converter CLI"
description: "Automates bulk image conversion using ImageMagick’s convert and mogrify commands with geometry expressions. Supports -density, -colorspace, and -profile flags for print-quality output."
verification: security_reviewed
source: "https://github.com/ImageMagick/ImageMagick"
category:
  - "Image &amp; Creative Automation"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imagemagick-batch-converter-cli/)
