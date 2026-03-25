---
name: "Sharp Image Pipeline Processor"
description: "Builds composable image transformation pipelines using the Sharp library with operations like resize(), composite(), and toFormat(). Leverages libvips bindings for high-performance batch processing."
category: "Image & Creative Automation"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sharp-image-pipeline-processor-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sharp"  # from ase_tool_match
  github_stars: 32074  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 54450041  # from ase_npm_downloads
  github_repo: "lovell/sharp"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Sharp Image Pipeline Processor

Builds composable image transformation pipelines using the Sharp library with operations like resize(), composite(), and toFormat(). Leverages libvips bindings for high-performance batch processing.

## Overview

The Sharp Image Pipeline Processor creates composable image transformation workflows using the Sharp library’s fluent API backed by libvips native bindings. It chains operations like sharp(input).resize({ width, height, fit: “cover” }).composite([{ input: watermark, gravity: “southeast” }]).toFormat(“webp”, { quality: 80 }) for efficient multi-step processing.

Core capabilities include intelligent resizing with sharp.fit options (cover, contain, fill, inside, outside), metadata-aware orientation correction via rotate() with EXIF auto-rotation, and color space manipulation through toColorspace() for print-ready CMYK output. The processor handles batch operations using sharp.concurrency() tuning for optimal CPU utilization.

Advanced features include SVG overlay compositing with blend modes, animated GIF/WebP processing through the pages option for frame manipulation, and tile generation via .tile({ size: 256 }) for deep-zoom image viewers. It supports ICC profile embedding through withMetadata({ icc }) and provides streaming pipelines via sharp().pipe() for memory-efficient processing of large images without buffering entire files.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sharp-image-pipeline-processor-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sharp-image-pipeline-processor-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sharp-image-pipeline-processor-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sharp-image-pipeline-processor-2 -a codex
```

### OpenClaw

```bash
clawhub install sharp-image-pipeline-processor-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sharp-image-pipeline-processor-2/
