---
title: "DALL-E Image Variation Generator"
description: "Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024&#215;1024/1792&#215;1024 aspect ratios, and implements content policy pre-screening with the Moderation API. This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development."
source: "https://github.com/openai/openai-node"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "openai/openai-node"
  github_stars: 10813
  npm_package: "openai"
  npm_weekly_downloads: 18107622
---

# DALL-E Image Variation Generator

Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024&#215;1024/1792&#215;1024 aspect ratios, and implements content policy pre-screening with the Moderation API. This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-image-variation-generator/)
