---
name: "AI Meta Description Generator"
description: "Bulk-generates SEO meta descriptions from page content using OpenAI's GPT-4o API with custom system prompts tuned for SERP CTR optimization. Validates character limits, checks for duplicate descriptions via Screaming Frog CSV exports, and outputs Yoast SEO-compatible import files."
verification: security_reviewed
source: "https://platform.openai.com/docs/api-reference"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Claude Agents"
---

# AI Meta Description Generator

AI Meta Description Generator processes page content at scale to produce compelling meta descriptions optimized for search engine result page click-through rates. It feeds page title, H1, first 500 words, and target keyword into OpenAI's GPT-4o chat completions API with a system prompt engineered for SERP snippet optimization.
The generator enforces a 150-160 character limit on output, includes the primary keyword naturally within the first 80 characters, and adds a clear call-to-action or value proposition. Each generated description is checked against existing descriptions loaded from Screaming Frog CSV crawl exports to prevent duplicates. Similarity scoring via SequenceMatcher flags descriptions that are too close to existing ones.
Output formats include a CSV with URL, current description, and proposed description columns for editorial review, plus a Yoast SEO-compatible import file using the wpseo_metadesc post meta key. For WordPress sites, the tool can directly update meta descriptions through the REST API by patching yoast_head_json metadata. Batch processing uses asyncio with rate-limited concurrent API calls to handle sites with thousands of pages efficiently, respecting OpenAI's tokens-per-minute limits.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ai-meta-description-generator/)
