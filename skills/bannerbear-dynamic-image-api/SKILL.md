---
title: "Bannerbear Dynamic Image API"
description: "Generates social media graphics and OG images dynamically via Bannerbear REST API. Manages template modifications, font layers, and signed URL generation for on-the-fly image personalization."
slug: "bannerbear-dynamic-image-api"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/bannerbear-dynamic-image-api/"
---

# Bannerbear Dynamic Image API

Generates social media graphics and OG images dynamically via Bannerbear REST API. Manages template modifications, font layers, and signed URL generation for on-the-fly image personalization.

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
clawhub install bannerbear-dynamic-image-api
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill automates dynamic image generation for social media posts, email headers, and Open Graph preview images using the Bannerbear REST API. It manages the full lifecycle from template selection to final image delivery. Templates are configured with modifiable text layers, image containers, and shape elements that accept dynamic data via API parameters. The skill handles Bannerbear’s asynchronous generation model: submitting image creation requests, polling for completion via webhook or status endpoint, and downloading rendered outputs. Batch generation processes data from CSV or JSON arrays, producing personalized images at scale for campaigns. Signed URL generation enables on-the-fly image personalization without API calls by encoding parameters in the URL path. The skill supports multi-format output (PNG, JPEG, PDF, GIF, MP4 for animated templates), template duplication for A/B testing variations, and font management including custom font uploads. Integration with social media posting APIs enables end-to-end content creation pipelines. Error handling covers template validation, layer bounds checking, and generation timeout recovery.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bannerbear-dynamic-image-api/)
