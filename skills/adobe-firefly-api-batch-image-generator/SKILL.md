---
title: "Adobe Firefly API Batch Image Generator"
description: "Calls Adobe Firefly’s text-to-image and generative fill APIs for batch asset creation. Manages Adobe IMS OAuth tokens and enforces Content Credentials (C2PA) metadata on all outputs."
verification: "security_reviewed"
source: "https://developer.adobe.com/firefly-services/docs/firefly-api/"
category:
  - "Image & Creative Automation"
framework:
  - "Cursor"
---

# Adobe Firefly API Batch Image Generator

The Adobe Firefly API Batch Image Generator streamlines large-scale creative asset production using Adobe’s Firefly Services REST API. It handles the complete OAuth 2.0 flow with Adobe IMS including service account JWT authentication and automatic token refresh. The skill supports text-to-image generation, generative fill for extending or modifying existing assets, and style reference matching via reference images. Each API call includes Content Credentials (C2PA) metadata embedding to ensure AI-generated content is properly attributed per Adobe’s transparency guidelines. Batch mode processes CSV manifests containing prompts, style references, aspect ratios, and output paths. Rate limiting respects Adobe’s per-minute quotas with exponential backoff. Results are validated against dimension and file-size constraints before delivery. The tool integrates with Adobe Creative Cloud Libraries for direct asset upload and supports webhook callbacks for completion notification. Error handling covers quota exhaustion, content policy rejections, and network timeouts with detailed logging.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/adobe-firefly-api-batch-image-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/adobe-firefly-api-batch-image-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/adobe-firefly-api-batch-image-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/adobe-firefly-api-batch-image-generator/)
