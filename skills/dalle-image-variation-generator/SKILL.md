---
title: "DALL-E Image Variation Generator"
description: "Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024×1024/1792×1024 aspect ratios, and implements content policy pre-screening with the Moderation API."
slug: "dalle-image-variation-generator"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dalle-image-variation-generator/"
listed: true
---

# DALL-E Image Variation Generator

Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024×1024/1792×1024 aspect ratios, and implements content policy pre-screening with the Moderation API.

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
clawhub install dalle-image-variation-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-image-variation-generator/)
