---
name: "DALL-E 3 Batch Asset Generator"
description: "Generates multiple image variations from a single brief using the OpenAI Images API (POST /v1/images/generations) with DALL-E 3, applying brand guidelines via structured prompt templates. Handles concurrent generation requests with retry logic for rate limit compliance."
category: "Image &amp; Creative Automation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dalle-3-batch-asset-generator/"
---
# DALL-E 3 Batch Asset Generator

Generates multiple image variations from a single brief using the OpenAI Images API (POST /v1/images/generations) with DALL-E 3, applying brand guidelines via structured prompt templates. Handles concurrent generation requests with retry logic for rate limit compliance.

Generates multiple image variations from a single brief using the OpenAI Images API (POST /v1/images/generations) with DALL-E 3, applying brand guidelines via structured prompt templates. Handles concurrent generation requests with retry logic for rate limit compliance.

This skill takes a creative brief and brand style guide, constructs optimized DALL-E 3 prompts with style directives, and generates multiple image sizes (1024×1024, 1792×1024, 1024×1792) in parallel. Implements exponential backoff for 429 rate limit responses, saves images to a local directory, and produces a manifest JSON with prompt metadata for each asset.

Use for social media content batches, blog illustration sets, marketing campaign assets, and UI mockup visuals. Not for photorealistic portraits of real people or trademarked brand recreations. Requires OPENAI_API_KEY with Images API access. DALL-E 3 generates one image per API call — batch throughput is 50-60 images/minute on Tier 2+.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dalle-3-batch-asset-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dalle-3-batch-asset-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dalle-3-batch-asset-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dalle-3-batch-asset-generator -a codex
```

### OpenClaw

```bash
clawhub install dalle-3-batch-asset-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-3-batch-asset-generator/)
