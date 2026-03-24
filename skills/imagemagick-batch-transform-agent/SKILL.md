---
name: "ImageMagick Batch Transform Agent"
description: "Automates ImageMagick convert and mogrify operations for bulk image processing including responsive srcset generation, WebP/AVIF conversion, and ICC color profile management with Little CMS integration."
category: "Image & Creative Automation"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/imagemagick-batch-transform-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "imagemagick"  # from ase_tool_match
  github_stars: 15991  # from ase_github_stars (integer, not string)
  github_repo: "ImageMagick/ImageMagick"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ImageMagick Batch Transform Agent

Automates ImageMagick convert and mogrify operations for bulk image processing including responsive srcset generation, WebP/AVIF conversion, and ICC color profile management with Little CMS integration.

## Overview

The ImageMagick Batch Transform Agent orchestrates complex image manipulation workflows using ImageMagick 7 command-line tools (magick convert, mogrify, composite). It generates responsive image srcsets with configurable breakpoints, outputting WebP, AVIF, and JPEG fallbacks with optimal quality settings determined by SSIM perceptual analysis.

Color management leverages Little CMS (LCMS2) for ICC profile conversions between sRGB, Adobe RGB, and CMYK color spaces, ensuring print-ready output. The skill handles EXIF metadata preservation or stripping based on privacy requirements, auto-orients images from camera rotation tags, and applies smart cropping using entropy-based region detection.

Batch operations support glob patterns, recursive directory traversal, and parallel processing via GNU Parallel for throughput on multi-core systems. Watermark compositing uses alpha channel blending with configurable opacity and positioning. The agent generates contact sheets, animated GIF assembly from frame sequences, and SVG-to-raster conversion at arbitrary DPI for print workflows. Processing manifests in JSON track all transformations for audit compliance.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-transform-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-transform-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-transform-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill imagemagick-batch-transform-agent -a codex
```

### OpenClaw

```bash
clawhub install imagemagick-batch-transform-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/imagemagick-batch-transform-agent/
