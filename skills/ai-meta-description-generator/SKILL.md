---
name: "AI Meta Description Generator"
description: "Bulk-generates SEO meta descriptions from page content using OpenAI’s GPT-4o API with custom system prompts tuned for SERP CTR optimization. Validates character limits, checks for duplicate descriptions via Screaming Frog CSV exports, and outputs Yoast SEO-compatible import files."
category: "Content Writing & SEO"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ai-meta-description-generator/"
tool_ecosystem:
  tool: openai
  github_stars: 10765
  npm_weekly_downloads: 16275389
  github_repo: openai/openai-node
  license: Apache-2.0
  maintained: true
---
# AI Meta Description Generator

Bulk-generates SEO meta descriptions from page content using OpenAI’s GPT-4o API with custom system prompts tuned for SERP CTR optimization. Validates character limits, checks for duplicate descriptions via Screaming Frog CSV exports, and outputs Yoast SEO-compatible import files.

## Overview

AI Meta Description Generator processes page content at scale to produce compelling meta descriptions optimized for search engine result page click-through rates. It feeds page title, H1, first 500 words, and target keyword into OpenAI’s GPT-4o chat completions API with a system prompt engineered for SERP snippet optimization.

The generator enforces a 150-160 character limit on output, includes the primary keyword naturally within the first 80 characters, and adds a clear call-to-action or value proposition. Each generated description is checked against existing descriptions loaded from Screaming Frog CSV crawl exports to prevent duplicates. Similarity scoring via SequenceMatcher flags descriptions that are too close to existing ones.

Output formats include a CSV with URL, current description, and proposed description columns for editorial review, plus a Yoast SEO-compatible import file using the wpseo_metadesc post meta key. For WordPress sites, the tool can directly update meta descriptions through the REST API by patching yoast_head_json metadata. Batch processing uses asyncio with rate-limited concurrent API calls to handle sites with thousands of pages efficiently, respecting OpenAI’s tokens-per-minute limits.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ai-meta-description-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ai-meta-description-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ai-meta-description-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ai-meta-description-generator -a codex
```

### OpenClaw

```bash
clawhub install ai-meta-description-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ai-meta-description-generator/)
