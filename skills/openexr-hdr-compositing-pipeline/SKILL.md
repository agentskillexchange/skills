---
name: "OpenEXR HDR Compositing Pipeline"
description: "Processes OpenEXR high dynamic range images using the OpenImageIO (oiiotool) CLI and Imath library for multi-layer compositing, tone mapping with ACES color transforms, and cryptomatte-based object isolation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/openexr-hdr-compositing-pipeline/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "OpenClaw"
---

# OpenEXR HDR Compositing Pipeline

The OpenEXR HDR Compositing Pipeline handles professional-grade HDR image workflows using OpenImageIO's oiiotool command-line interface and the Imath half-float math library. It reads multi-layer EXR files containing beauty passes, AOVs (arbitrary output variables), and cryptomatte channels, then composites them using additive, over, and multiply blend operations. The agent applies ACES (Academy Color Encoding System) color transforms via OpenColorIO (OCIO) config files for industry-standard tone mapping from scene-linear to display-referred color spaces. Cryptomatte object isolation uses the standardized manifest format to extract individual objects by name from a single EXR render. Batch processing leverages oiiotool's expression syntax for operations across thousands of frames. Output includes EXR for further compositing, ACES-graded TIFF for print, and sRGB PNG/JPEG for web delivery. Integrates with Nuke, Blender, and DaVinci Resolve via shared OCIO configurations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openexr-hdr-compositing-pipeline/)
