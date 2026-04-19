---
title: "Bannerbear Dynamic Image API"
description: "This skill automates dynamic image generation for social media posts, email headers, and Open Graph preview images using the Bannerbear REST API. It manages the full lifecycle from template selection to final image delivery. Templates are configured with modifiable text layers, image containers, and shape elements that accept dynamic data via API parameters. The skill handles Bannerbear&#8217;s asynchronous generation model: submitting image creation requests, polling for completion via webhook or status endpoint, and downloading rendered outputs. Batch generation processes data from CSV or JSON arrays, producing personalized images at scale for campaigns. Signed URL generation enables on-the-fly image personalization without API calls by encoding parameters in the URL path. The skill supports multi-format output (PNG, JPEG, PDF, GIF, MP4 for animated templates), template duplication for A/B testing variations, and font management including custom font uploads. Integration with social media posting APIs enables end-to-end content creation pipelines. Error handling covers template validation, layer bounds checking, and generation timeout recovery."
source: "https://agentskillexchange.com/skills/bannerbear-dynamic-image-api/"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
---

# Bannerbear Dynamic Image API

This skill automates dynamic image generation for social media posts, email headers, and Open Graph preview images using the Bannerbear REST API. It manages the full lifecycle from template selection to final image delivery. Templates are configured with modifiable text layers, image containers, and shape elements that accept dynamic data via API parameters. The skill handles Bannerbear&#8217;s asynchronous generation model: submitting image creation requests, polling for completion via webhook or status endpoint, and downloading rendered outputs. Batch generation processes data from CSV or JSON arrays, producing personalized images at scale for campaigns. Signed URL generation enables on-the-fly image personalization without API calls by encoding parameters in the URL path. The skill supports multi-format output (PNG, JPEG, PDF, GIF, MP4 for animated templates), template duplication for A/B testing variations, and font management including custom font uploads. Integration with social media posting APIs enables end-to-end content creation pipelines. Error handling covers template validation, layer bounds checking, and generation timeout recovery.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bannerbear-dynamic-image-api/)
