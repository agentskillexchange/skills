---
name: Adobe Firefly API Batch Image Generator
description: Calls Adobe Firefly&#8217;s text-to-image and generative fill APIs for
  batch asset creation. Manages Adobe IMS OAuth tokens and enforces Content Credentials
  (C2PA) metadata on all outputs.
verification: security_reviewed
source: https://agentskillexchange.com/skills/adobe-firefly-api-batch-image-generator/
category:
- Image &amp; Creative Automation
framework:
- Cursor
---
# Adobe Firefly API Batch Image Generator

The Adobe Firefly API Batch Image Generator streamlines large-scale creative asset production using Adobe's Firefly Services REST API. It handles the complete OAuth 2.0 flow with Adobe IMS including service account JWT authentication and automatic token refresh. The skill supports text-to-image generation, generative fill for extending or modifying existing assets, and style reference matching via reference images. Each API call includes Content Credentials (C2PA) metadata embedding to ensure AI-generated content is properly attributed per Adobe's transparency guidelines. Batch mode processes CSV manifests containing prompts, style references, aspect ratios, and output paths. Rate limiting respects Adobe's per-minute quotas with exponential backoff. Results are validated against dimension and file-size constraints before delivery. The tool integrates with Adobe Creative Cloud Libraries for direct asset upload and supports webhook callbacks for completion notification. Error handling covers quota exhaustion, content policy rejections, and network timeouts with detailed logging.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/adobe-firefly-api-batch-image-generator/)
