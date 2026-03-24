---
name: "DALL-E 3 Batch Asset Generator"
description: "Generates multiple image variations from a single brief using the OpenAI Images API (POST /v1/images/generations) with DALL-E 3, applying brand guidelines via structured prompt templates. Handles concurrent generation requests with retry logic for rate limit compliance."
category: "Image & Creative Automation"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dalle-3-batch-asset-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "openai"  # from ase_tool_match
  github_stars: 10761  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16275389  # from ase_npm_downloads
  github_repo: "openai/openai-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# DALL-E 3 Batch Asset Generator

Generates multiple image variations from a single brief using the OpenAI Images API (POST /v1/images/generations) with DALL-E 3, applying brand guidelines via structured prompt templates. Handles concurrent generation requests with retry logic for rate limit compliance.

## Overview

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

- Marketplace: https://agentskillexchange.com/skills/dalle-3-batch-asset-generator/
