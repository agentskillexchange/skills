---
title: "Adobe Firefly API Batch Image Generator"
description: "Calls Adobe Firefly’s text-to-image and generative fill APIs for batch asset creation. Manages Adobe IMS OAuth tokens and enforces Content Credentials (C2PA) metadata on all outputs."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/adobe-firefly-api-batch-image-generator/"
category:
  - "Image & Creative Automation"
framework:
  - "Cursor"
---

# Adobe Firefly API Batch Image Generator

The Adobe Firefly API Batch Image Generator streamlines large-scale creative asset production using Adobe’s Firefly Services REST API. It handles the complete OAuth 2.0 flow with Adobe IMS including service account JWT authentication and automatic token refresh. The skill supports text-to-image generation, generative fill for extending or modifying existing assets, and style reference matching via reference images. Each API call includes Content Credentials (C2PA) metadata embedding to ensure AI-generated content is properly attributed per Adobe’s transparency guidelines. Batch mode processes CSV manifests containing prompts, style references, aspect ratios, and output paths. Rate limiting respects Adobe’s per-minute quotas with exponential backoff. Results are validated against dimension and file-size constraints before delivery. The tool integrates with Adobe Creative Cloud Libraries for direct asset upload and supports webhook callbacks for completion notification. Error handling covers quota exhaustion, content policy rejections, and network timeouts with detailed logging.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/adobe-firefly-api-batch-image-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/adobe-firefly-api-batch-image-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/adobe-firefly-api-batch-image-generator/)
