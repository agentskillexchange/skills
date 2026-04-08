---
title: Photoshop Batch Action Automator
description: The Photoshop Batch Action Automator drives Adobe Photoshop programmatically
  through the UXP Scripting API for modern plugin workflows and CEP ExtendScript for
  legacy automation compatibility. It connects to running Photoshop instances via
  the photoshop-connection npm package for remote command execution. Batch operations
  include intelligent resizing with content-aware scaling for non-standard aspect
  ratios, watermark placement with configurable opacity and positioning, and ICC color
  profile conversion between sRGB, Adobe RGB, and CMYK profiles for print preparation.
  Smart Object replacement enables template-based batch generation where placeholder
  layers are swapped with source images while preserving transformations and effects.
  The skill handles file format conversion across PSD, TIFF, PNG, JPEG, and WebP with
  per-format quality and compression settings. Metadata preservation ensures EXIF,
  IPTC, and XMP data survives processing. Progress tracking provides per-file status
  updates with error recovery that skips corrupt files and logs failures for manual
  review. Output organization sorts processed files into configurable directory structures
  based on dimensions, color space, or custom naming templates.
verification: security_reviewed
source: https://agentskillexchange.com/skills/photoshop-batch-action-automator/
category:
- Image &amp; Creative Automation
framework:
- Custom Agents
---

# Photoshop Batch Action Automator

The Photoshop Batch Action Automator drives Adobe Photoshop programmatically through the UXP Scripting API for modern plugin workflows and CEP ExtendScript for legacy automation compatibility. It connects to running Photoshop instances via the photoshop-connection npm package for remote command execution. Batch operations include intelligent resizing with content-aware scaling for non-standard aspect ratios, watermark placement with configurable opacity and positioning, and ICC color profile conversion between sRGB, Adobe RGB, and CMYK profiles for print preparation. Smart Object replacement enables template-based batch generation where placeholder layers are swapped with source images while preserving transformations and effects. The skill handles file format conversion across PSD, TIFF, PNG, JPEG, and WebP with per-format quality and compression settings. Metadata preservation ensures EXIF, IPTC, and XMP data survives processing. Progress tracking provides per-file status updates with error recovery that skips corrupt files and logs failures for manual review. Output organization sorts processed files into configurable directory structures based on dimensions, color space, or custom naming templates.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/photoshop-batch-action-automator/)
