---
name: "Photoshop Batch Action Automator"
description: "Automates Adobe Photoshop batch processing via the UXP Scripting API and CEP ExtendScript. Handles bulk resize, watermarking, color profile conversion (ICC), and smart object replacement using photoshop-connection npm package."
category: "Image & Creative Automation"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/photoshop-batch-action-automator/"
---

# Photoshop Batch Action Automator

Automates Adobe Photoshop batch processing via the UXP Scripting API and CEP ExtendScript. Handles bulk resize, watermarking, color profile conversion (ICC), and smart object replacement using photoshop-connection npm package.

## Overview

The Photoshop Batch Action Automator drives Adobe Photoshop programmatically through the UXP Scripting API for modern plugin workflows and CEP ExtendScript for legacy automation compatibility. It connects to running Photoshop instances via the photoshop-connection npm package for remote command execution.

Batch operations include intelligent resizing with content-aware scaling for non-standard aspect ratios, watermark placement with configurable opacity and positioning, and ICC color profile conversion between sRGB, Adobe RGB, and CMYK profiles for print preparation. Smart Object replacement enables template-based batch generation where placeholder layers are swapped with source images while preserving transformations and effects.

The skill handles file format conversion across PSD, TIFF, PNG, JPEG, and WebP with per-format quality and compression settings. Metadata preservation ensures EXIF, IPTC, and XMP data survives processing. Progress tracking provides per-file status updates with error recovery that skips corrupt files and logs failures for manual review. Output organization sorts processed files into configurable directory structures based on dimensions, color space, or custom naming templates.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill photoshop-batch-action-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill photoshop-batch-action-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill photoshop-batch-action-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill photoshop-batch-action-automator -a codex
```

### OpenClaw

```bash
clawhub install photoshop-batch-action-automator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/photoshop-batch-action-automator/
