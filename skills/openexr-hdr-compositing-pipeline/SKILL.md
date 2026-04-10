---
title: "OpenEXR HDR Compositing Pipeline"
description: "Processes OpenEXR high dynamic range images using the OpenImageIO (oiiotool) CLI and Imath library for multi-layer compositing, tone mapping with ACES color transforms, and cryptomatte-based object isolation."
slug: "openexr-hdr-compositing-pipeline"
category:
  - "Image &amp; Creative Automation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/openexr-hdr-compositing-pipeline/"
---

# OpenEXR HDR Compositing Pipeline

Processes OpenEXR high dynamic range images using the OpenImageIO (oiiotool) CLI and Imath library for multi-layer compositing, tone mapping with ACES color transforms, and cryptomatte-based object isolation.

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
clawhub install openexr-hdr-compositing-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OpenEXR HDR Compositing Pipeline handles professional-grade HDR image workflows using OpenImageIO’s oiiotool command-line interface and the Imath half-float math library. It reads multi-layer EXR files containing beauty passes, AOVs (arbitrary output variables), and cryptomatte channels, then composites them using additive, over, and multiply blend operations. The agent applies ACES (Academy Color Encoding System) color transforms via OpenColorIO (OCIO) config files for industry-standard tone mapping from scene-linear to display-referred color spaces. Cryptomatte object isolation uses the standardized manifest format to extract individual objects by name from a single EXR render. Batch processing leverages oiiotool’s expression syntax for operations across thousands of frames. Output includes EXR for further compositing, ACES-graded TIFF for print, and sRGB PNG/JPEG for web delivery. Integrates with Nuke, Blender, and DaVinci Resolve via shared OCIO configurations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openexr-hdr-compositing-pipeline/)
