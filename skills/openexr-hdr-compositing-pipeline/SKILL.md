---
title: "OpenEXR HDR Compositing Pipeline"
description: "Processes OpenEXR high dynamic range images using the OpenImageIO (oiiotool) CLI and Imath library for multi-layer compositing, tone mapping with ACES color transforms, and cryptomatte-based object isolation."
verification: security_reviewed
source: "https://github.com/AcademySoftwareFoundation/openexr"
category:
  - "Image & Creative Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "academysoftwarefoundation/openexr"
  github_stars: 1795
  license: "BSD-3-Clause"
---

# OpenEXR HDR Compositing Pipeline

The OpenEXR HDR Compositing Pipeline handles professional-grade HDR image workflows using OpenImageIO’s oiiotool command-line interface and the Imath half-float math library. It reads multi-layer EXR files containing beauty passes, AOVs (arbitrary output variables), and cryptomatte channels, then composites them using additive, over, and multiply blend operations. The agent applies ACES (Academy Color Encoding System) color transforms via OpenColorIO (OCIO) config files for industry-standard tone mapping from scene-linear to display-referred color spaces. Cryptomatte object isolation uses the standardized manifest format to extract individual objects by name from a single EXR render. Batch processing leverages oiiotool’s expression syntax for operations across thousands of frames. Output includes EXR for further compositing, ACES-graded TIFF for print, and sRGB PNG/JPEG for web delivery. Integrates with Nuke, Blender, and DaVinci Resolve via shared OCIO configurations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/openexr-hdr-compositing-pipeline
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/openexr-hdr-compositing-pipeline` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openexr-hdr-compositing-pipeline/)
