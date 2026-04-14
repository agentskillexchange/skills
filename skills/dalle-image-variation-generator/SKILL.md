---
title: "DALL-E Image Variation Generator"
description: "Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024×1024/1792×1024 aspect ratios, and implements content policy pre-screening with the Moderation API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dalle-image-variation-generator/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
---

# DALL-E Image Variation Generator

Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024×1024/1792×1024 aspect ratios, and implements content policy pre-screening with the Moderation API.

This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-image-variation-generator/)
