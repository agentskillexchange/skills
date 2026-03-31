---
name: "DALL-E Image Variation Generator"
description: "Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024&#215;1024/1792&#215;1024 aspect ratios, and implements content policy pre-screening with the Moderation API."
category: "Image &amp; Creative Automation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dalle-image-variation-generator/"
---
# DALL-E Image Variation Generator

Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024&#215;1024/1792&#215;1024 aspect ratios, and implements content policy pre-screening with the Moderation API.

## Overview

Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024&#215;1024/1792&#215;1024 aspect ratios, and implements content policy pre-screening with the Moderation API.

This skill provides comprehensive automation for its target domain with production-ready error handling and logging. It implements retry mechanisms with configurable backoff strategies, validates all inputs against JSON Schema definitions, and produces structured output compatible with downstream processing pipelines. Authentication is handled through OAuth 2.0 flows or API key rotation with secure storage in environment variables or secret managers like HashiCorp Vault. The skill supports dry-run mode for safe testing, emits OpenTelemetry traces for distributed debugging, and includes comprehensive unit test coverage with mock fixtures for offline development.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dalle-image-variation-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dalle-image-variation-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dalle-image-variation-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dalle-image-variation-generator -a codex
```

### OpenClaw

```bash
clawhub install dalle-image-variation-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-image-variation-generator/)
