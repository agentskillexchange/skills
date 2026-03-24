---
name: "Bannerbear Dynamic Image API"
description: "Generates social media graphics and OG images dynamically via Bannerbear REST API. Manages template modifications, font layers, and signed URL generation for on-the-fly image personalization."
category: "Image & Creative Automation"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/bannerbear-dynamic-image-api/"
---

# Bannerbear Dynamic Image API

Generates social media graphics and OG images dynamically via Bannerbear REST API. Manages template modifications, font layers, and signed URL generation for on-the-fly image personalization.

## Overview

This skill automates dynamic image generation for social media posts, email headers, and Open Graph preview images using the Bannerbear REST API. It manages the full lifecycle from template selection to final image delivery. Templates are configured with modifiable text layers, image containers, and shape elements that accept dynamic data via API parameters. The skill handles Bannerbear’s asynchronous generation model: submitting image creation requests, polling for completion via webhook or status endpoint, and downloading rendered outputs. Batch generation processes data from CSV or JSON arrays, producing personalized images at scale for campaigns. Signed URL generation enables on-the-fly image personalization without API calls by encoding parameters in the URL path. The skill supports multi-format output (PNG, JPEG, PDF, GIF, MP4 for animated templates), template duplication for A/B testing variations, and font management including custom font uploads. Integration with social media posting APIs enables end-to-end content creation pipelines. Error handling covers template validation, layer bounds checking, and generation timeout recovery.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill bannerbear-dynamic-image-api
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill bannerbear-dynamic-image-api -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill bannerbear-dynamic-image-api -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill bannerbear-dynamic-image-api -a codex
```

### OpenClaw

```bash
clawhub install bannerbear-dynamic-image-api
```

## Source

- Marketplace: https://agentskillexchange.com/skills/bannerbear-dynamic-image-api/
