---
title: "Adobe Firefly API Batch Image Generator"
description: "Calls Adobe Firefly’s text-to-image and generative fill APIs for batch asset creation. Manages Adobe IMS OAuth tokens and enforces Content Credentials (C2PA) metadata on all outputs."
slug: "adobe-firefly-api-batch-image-generator"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/adobe-firefly-api-batch-image-generator/"
---

# Adobe Firefly API Batch Image Generator

Calls Adobe Firefly’s text-to-image and generative fill APIs for batch asset creation. Manages Adobe IMS OAuth tokens and enforces Content Credentials (C2PA) metadata on all outputs.

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
clawhub install adobe-firefly-api-batch-image-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Adobe Firefly API Batch Image Generator streamlines large-scale creative asset production using Adobe’s Firefly Services REST API. It handles the complete OAuth 2.0 flow with Adobe IMS including service account JWT authentication and automatic token refresh. The skill supports text-to-image generation, generative fill for extending or modifying existing assets, and style reference matching via reference images. Each API call includes Content Credentials (C2PA) metadata embedding to ensure AI-generated content is properly attributed per Adobe’s transparency guidelines. Batch mode processes CSV manifests containing prompts, style references, aspect ratios, and output paths. Rate limiting respects Adobe’s per-minute quotas with exponential backoff. Results are validated against dimension and file-size constraints before delivery. The tool integrates with Adobe Creative Cloud Libraries for direct asset upload and supports webhook callbacks for completion notification. Error handling covers quota exhaustion, content policy rejections, and network timeouts with detailed logging.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/adobe-firefly-api-batch-image-generator/)
