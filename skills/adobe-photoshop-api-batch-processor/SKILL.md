---
title: "Adobe Photoshop API Batch Processor"
description: "Automates image editing workflows via the Adobe Photoshop API (Firefly Services). Supports smart object replacement, action playback, and PSD layer manipulation at scale."
verification: "security_reviewed"
source: "https://developer.adobe.com/firefly-services/docs/photoshop/"
category:
  - "Image & Creative Automation"
framework:
  - "ChatGPT Agents"
---

# Adobe Photoshop API Batch Processor

The Adobe Photoshop API Batch Processor leverages Adobe Firefly Services (formerly Creative Cloud APIs) to perform enterprise-scale image editing without local Photoshop installations. It communicates with the Photoshop API endpoints for actions like cutout, mask, smart object replacement, and layer composition.

The skill manages Adobe IMS OAuth2 authentication with automatic token refresh and supports both Adobe S3 presigned URLs and Azure Blob storage for input/output asset management. Batch processing queues handle rate limiting and retry logic for large asset libraries.

Smart object replacement enables template-based image generation where text layers, images, and adjustment layers are dynamically swapped via the renditionCreate API. Action playback executes recorded Photoshop actions (.atn files) server-side for consistent filter and effect application.

PSD layer manipulation supports adding, removing, and modifying individual layers including text layers with font substitution, shape layers with path editing, and adjustment layers with parameter tuning. The agent generates renditions in multiple formats (JPEG, PNG, TIFF, PSD) with configurable quality and color space settings. Integration with Adobe Lightroom API extends capabilities to RAW file processing and preset application.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/adobe-photoshop-api-batch-processor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/adobe-photoshop-api-batch-processor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/adobe-photoshop-api-batch-processor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/adobe-photoshop-api-batch-processor/)
