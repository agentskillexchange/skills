---
title: "Bannerbear Dynamic Image API"
description: "This skill automates dynamic image generation for social media posts, email headers, and Open Graph preview images using the Bannerbear REST API. It manages the full lifecycle from template selection to final image delivery. Templates are configured with modifiable text layers, image containers, and shape elements that accept dynamic data via API parameters. The skill handles Bannerbear’s asynchronous generation model: submitting image creation requests, polling for completion via webhook or status endpoint, and downloading rendered outputs. Batch generation processes data from CSV or JSON arrays, producing personalized images at scale for campaigns. Signed URL generation enables on-the-fly image personalization without API calls by encoding parameters in the URL path. The skill supports multi-format output (PNG, JPEG, PDF, GIF, MP4 for animated templates), template duplication for A/B testing variations, and font management including custom font uploads. Integration with social media posting APIs enables end-to-end content creation pipelines. Error handling covers template validation, layer bounds checking, and generation timeout recovery."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/bannerbear-dynamic-image-api/"
framework:
  - "Custom Agents"
---

# Bannerbear Dynamic Image API

This skill automates dynamic image generation for social media posts, email headers, and Open Graph preview images using the Bannerbear REST API. It manages the full lifecycle from template selection to final image delivery. Templates are configured with modifiable text layers, image containers, and shape elements that accept dynamic data via API parameters. The skill handles Bannerbear’s asynchronous generation model: submitting image creation requests, polling for completion via webhook or status endpoint, and downloading rendered outputs. Batch generation processes data from CSV or JSON arrays, producing personalized images at scale for campaigns. Signed URL generation enables on-the-fly image personalization without API calls by encoding parameters in the URL path. The skill supports multi-format output (PNG, JPEG, PDF, GIF, MP4 for animated templates), template duplication for A/B testing variations, and font management including custom font uploads. Integration with social media posting APIs enables end-to-end content creation pipelines. Error handling covers template validation, layer bounds checking, and generation timeout recovery.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/bannerbear-dynamic-image-api
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/bannerbear-dynamic-image-api` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bannerbear-dynamic-image-api/)
