---
name: "DALL-E Image Variation Generator"
description: "Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024×1024/1792×1024 aspect ratios, and implements content policy pre-screening with the Moderation API."
category: "Image & Creative Automation"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dalle-image-variation-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "openai"  # from ase_tool_match
  github_stars: 10765  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/openai-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# DALL-E Image Variation Generator

Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024×1024/1792×1024 aspect ratios, and implements content policy pre-screening with the Moderation API.

## Overview

Generates image variations and edits using the OpenAI Images API v1 with DALL-E 3 model selection. Supports inpainting via base64-encoded mask uploads, handles 1024×1024/1792×1024 aspect ratios, and implements content policy pre-screening with the Moderation API.

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

- Marketplace: https://agentskillexchange.com/skills/dalle-image-variation-generator/
