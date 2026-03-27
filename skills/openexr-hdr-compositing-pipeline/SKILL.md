---
name: "OpenEXR HDR Compositing Pipeline"
description: "Processes OpenEXR high dynamic range images using the OpenImageIO (oiiotool) CLI and Imath library for multi-layer compositing, tone mapping with ACES color transforms, and cryptomatte-based object isolation."
category: "Image & Creative Automation"
framework: "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/openexr-hdr-compositing-pipeline/"
---

# OpenEXR HDR Compositing Pipeline

Processes OpenEXR high dynamic range images using the OpenImageIO (oiiotool) CLI and Imath library for multi-layer compositing, tone mapping with ACES color transforms, and cryptomatte-based object isolation.

## Overview

The OpenEXR HDR Compositing Pipeline handles professional-grade HDR image workflows using OpenImageIO’s oiiotool command-line interface and the Imath half-float math library. It reads multi-layer EXR files containing beauty passes, AOVs (arbitrary output variables), and cryptomatte channels, then composites them using additive, over, and multiply blend operations. The agent applies ACES (Academy Color Encoding System) color transforms via OpenColorIO (OCIO) config files for industry-standard tone mapping from scene-linear to display-referred color spaces. Cryptomatte object isolation uses the standardized manifest format to extract individual objects by name from a single EXR render. Batch processing leverages oiiotool’s expression syntax for operations across thousands of frames. Output includes EXR for further compositing, ACES-graded TIFF for print, and sRGB PNG/JPEG for web delivery. Integrates with Nuke, Blender, and DaVinci Resolve via shared OCIO configurations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openexr-hdr-compositing-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openexr-hdr-compositing-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openexr-hdr-compositing-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openexr-hdr-compositing-pipeline -a codex
```

### OpenClaw

```bash
clawhub install openexr-hdr-compositing-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/openexr-hdr-compositing-pipeline/
