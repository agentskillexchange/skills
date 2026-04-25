---
title: "Photoshop Batch Action Automator"
description: "Automates Adobe Photoshop batch processing via the UXP Scripting API and CEP ExtendScript. Handles bulk resize, watermarking, color profile conversion (ICC), and smart object replacement using photoshop-connection npm package."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/photoshop-batch-action-automator/"
category:
  - "Image & Creative Automation"
framework:
  - "Custom Agents"
---

# Photoshop Batch Action Automator

The Photoshop Batch Action Automator drives Adobe Photoshop programmatically through the UXP Scripting API for modern plugin workflows and CEP ExtendScript for legacy automation compatibility. It connects to running Photoshop instances via the photoshop-connection npm package for remote command execution. Batch operations include intelligent resizing with content-aware scaling for non-standard aspect ratios, watermark placement with configurable opacity and positioning, and ICC color profile conversion between sRGB, Adobe RGB, and CMYK profiles for print preparation. Smart Object replacement enables template-based batch generation where placeholder layers are swapped with source images while preserving transformations and effects. The skill handles file format conversion across PSD, TIFF, PNG, JPEG, and WebP with per-format quality and compression settings. Metadata preservation ensures EXIF, IPTC, and XMP data survives processing. Progress tracking provides per-file status updates with error recovery that skips corrupt files and logs failures for manual review. Output organization sorts processed files into configurable directory structures based on dimensions, color space, or custom naming templates.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/photoshop-batch-action-automator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/photoshop-batch-action-automator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/photoshop-batch-action-automator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/photoshop-batch-action-automator/)
