---
title: "DALL-E 3 Batch Asset Generator"
description: "Generates multiple image variations from a single brief using the OpenAI Images API (POST /v1/images/generations) with DALL-E 3, applying brand guidelines via structured prompt templates. Handles concurrent generation requests with retry logic for rate limit compliance."
verification: security_reviewed
source: "https://github.com/openai/openai-node"
category:
  - "Image & Creative Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "openai/openai-node"
  github_stars: 10813
  npm_package: "openai"
  npm_weekly_downloads: 18107622
  license: "Apache-2.0"
---

# DALL-E 3 Batch Asset Generator

Generates multiple image variations from a single brief using the OpenAI Images API (POST /v1/images/generations) with DALL-E 3, applying brand guidelines via structured prompt templates. Handles concurrent generation requests with retry logic for rate limit compliance.

This skill takes a creative brief and brand style guide, constructs optimized DALL-E 3 prompts with style directives, and generates multiple image sizes (1024×1024, 1792×1024, 1024×1792) in parallel. Implements exponential backoff for 429 rate limit responses, saves images to a local directory, and produces a manifest JSON with prompt metadata for each asset.

Use for social media content batches, blog illustration sets, marketing campaign assets, and UI mockup visuals. Not for photorealistic portraits of real people or trademarked brand recreations. Requires OPENAI_API_KEY with Images API access. DALL-E 3 generates one image per API call — batch throughput is 50-60 images/minute on Tier 2+.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dalle-3-batch-asset-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dalle-3-batch-asset-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-3-batch-asset-generator/)
