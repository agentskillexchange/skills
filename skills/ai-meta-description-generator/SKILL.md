---
title: "AI Meta Description Generator"
description: "Bulk-generates SEO meta descriptions from page content using OpenAI’s GPT-4o API with custom system prompts tuned for SERP CTR optimization. Validates character limits, checks for duplicate descriptions via Screaming Frog CSV exports, and outputs Yoast SEO-compatible import files."
verification: "security_reviewed"
source: "https://platform.openai.com/docs/api-reference"
category:
  - "Content Writing & SEO"
framework:
  - "Claude Agents"
---

# AI Meta Description Generator

AI Meta Description Generator processes page content at scale to produce compelling meta descriptions optimized for search engine result page click-through rates. It feeds page title, H1, first 500 words, and target keyword into OpenAI’s GPT-4o chat completions API with a system prompt engineered for SERP snippet optimization. The generator enforces a 150-160 character limit on output, includes the primary keyword naturally within the first 80 characters, and adds a clear call-to-action or value proposition. Each generated description is checked against existing descriptions loaded from Screaming Frog CSV crawl exports to prevent duplicates. Similarity scoring via SequenceMatcher flags descriptions that are too close to existing ones. Output formats include a CSV with URL, current description, and proposed description columns for editorial review, plus a Yoast SEO-compatible import file using the wpseo_metadesc post meta key. For WordPress sites, the tool can directly update meta descriptions through the REST API by patching yoast_head_json metadata. Batch processing uses asyncio with rate-limited concurrent API calls to handle sites with thousands of pages efficiently, respecting OpenAI’s tokens-per-minute limits.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/ai-meta-description-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ai-meta-description-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/ai-meta-description-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ai-meta-description-generator/)
