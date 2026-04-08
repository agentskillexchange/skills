---
title: Adobe Firefly API Batch Image Generator
description: The Adobe Firefly API Batch Image Generator streamlines large-scale creative
  asset production using Adobe’s Firefly Services REST API. It handles the complete
  OAuth 2.0 flow with Adobe IMS including service account JWT authentication and automatic
  token refresh. The skill supports text-to-image generation, generative fill for
  extending or modifying existing assets, and style reference matching via reference
  images. Each API call includes Content Credentials (C2PA) metadata embedding to
  ensure AI-generated content is properly attributed per Adobe’s transparency guidelines.
  Batch mode processes CSV manifests containing prompts, style references, aspect
  ratios, and output paths. Rate limiting respects Adobe’s per-minute quotas with
  exponential backoff. Results are validated against dimension and file-size constraints
  before delivery. The tool integrates with Adobe Creative Cloud Libraries for direct
  asset upload and supports webhook callbacks for completion notification. Error handling
  covers quota exhaustion, content policy rejections, and network timeouts with detailed
  logging.
verification: security_reviewed
source: https://agentskillexchange.com/skills/adobe-firefly-api-batch-image-generator/
category:
- Image &amp; Creative Automation
framework:
- Cursor
---

# Adobe Firefly API Batch Image Generator

The Adobe Firefly API Batch Image Generator streamlines large-scale creative asset production using Adobe’s Firefly Services REST API. It handles the complete OAuth 2.0 flow with Adobe IMS including service account JWT authentication and automatic token refresh. The skill supports text-to-image generation, generative fill for extending or modifying existing assets, and style reference matching via reference images. Each API call includes Content Credentials (C2PA) metadata embedding to ensure AI-generated content is properly attributed per Adobe’s transparency guidelines. Batch mode processes CSV manifests containing prompts, style references, aspect ratios, and output paths. Rate limiting respects Adobe’s per-minute quotas with exponential backoff. Results are validated against dimension and file-size constraints before delivery. The tool integrates with Adobe Creative Cloud Libraries for direct asset upload and supports webhook callbacks for completion notification. Error handling covers quota exhaustion, content policy rejections, and network timeouts with detailed logging.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/adobe-firefly-api-batch-image-generator/)
