---
name: "Bannerbear Dynamic Image API"
description: "Generates social media graphics and OG images dynamically via Bannerbear REST API. Manages template modifications, font layers, and signed URL generation for on-the-fly image personalization."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/bannerbear-dynamic-image-api/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
---

# Bannerbear Dynamic Image API

This skill automates dynamic image generation for social media posts, email headers, and Open Graph preview images using the Bannerbear REST API. It manages the full lifecycle from template selection to final image delivery. Templates are configured with modifiable text layers, image containers, and shape elements that accept dynamic data via API parameters. The skill handles Bannerbear's asynchronous generation model: submitting image creation requests, polling for completion via webhook or status endpoint, and downloading rendered outputs. Batch generation processes data from CSV or JSON arrays, producing personalized images at scale for campaigns. Signed URL generation enables on-the-fly image personalization without API calls by encoding parameters in the URL path. The skill supports multi-format output (PNG, JPEG, PDF, GIF, MP4 for animated templates), template duplication for A/B testing variations, and font management including custom font uploads. Integration with social media posting APIs enables end-to-end content creation pipelines. Error handling covers template validation, layer bounds checking, and generation timeout recovery.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bannerbear-dynamic-image-api/)
