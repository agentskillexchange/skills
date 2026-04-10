---
title: "AI Meta Description Generator"
description: "Bulk-generates SEO meta descriptions from page content using OpenAI’s GPT-4o API with custom system prompts tuned for SERP CTR optimization. Validates character limits, checks for duplicate descriptions via Screaming Frog CSV exports, and outputs Yoast SEO-compatible import files."
slug: "ai-meta-description-generator"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://platform.openai.com/docs/api-reference"
listed: true
---

# AI Meta Description Generator

Bulk-generates SEO meta descriptions from page content using OpenAI’s GPT-4o API with custom system prompts tuned for SERP CTR optimization. Validates character limits, checks for duplicate descriptions via Screaming Frog CSV exports, and outputs Yoast SEO-compatible import files.

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
clawhub install ai-meta-description-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

AI Meta Description Generator processes page content at scale to produce compelling meta descriptions optimized for search engine result page click-through rates. It feeds page title, H1, first 500 words, and target keyword into OpenAI’s GPT-4o chat completions API with a system prompt engineered for SERP snippet optimization.
The generator enforces a 150-160 character limit on output, includes the primary keyword naturally within the first 80 characters, and adds a clear call-to-action or value proposition. Each generated description is checked against existing descriptions loaded from Screaming Frog CSV crawl exports to prevent duplicates. Similarity scoring via SequenceMatcher flags descriptions that are too close to existing ones.
Output formats include a CSV with URL, current description, and proposed description columns for editorial review, plus a Yoast SEO-compatible import file using the wpseo_metadesc post meta key. For WordPress sites, the tool can directly update meta descriptions through the REST API by patching yoast_head_json metadata. Batch processing uses asyncio with rate-limited concurrent API calls to handle sites with thousands of pages efficiently, respecting OpenAI’s tokens-per-minute limits.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ai-meta-description-generator/)
