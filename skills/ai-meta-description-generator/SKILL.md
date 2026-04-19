---
title: "AI Meta Description Generator"
description: "AI Meta Description Generator processes page content at scale to produce compelling meta descriptions optimized for search engine result page click-through rates. It feeds page title, H1, first 500 words, and target keyword into OpenAI&#8217;s GPT-4o chat completions API with a system prompt engineered for SERP snippet optimization. The generator enforces a 150-160 character limit on output, includes the primary keyword naturally within the first 80 characters, and adds a clear call-to-action or value proposition. Each generated description is checked against existing descriptions loaded from Screaming Frog CSV crawl exports to prevent duplicates. Similarity scoring via SequenceMatcher flags descriptions that are too close to existing ones. Output formats include a CSV with URL, current description, and proposed description columns for editorial review, plus a Yoast SEO-compatible import file using the wpseo_metadesc post meta key. For WordPress sites, the tool can directly update meta descriptions through the REST API by patching yoast_head_json metadata. Batch processing uses asyncio with rate-limited concurrent API calls to handle sites with thousands of pages efficiently, respecting OpenAI&#8217;s tokens-per-minute limits."
source: "https://platform.openai.com/docs/api-reference"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Claude Agents"
---

# AI Meta Description Generator

AI Meta Description Generator processes page content at scale to produce compelling meta descriptions optimized for search engine result page click-through rates. It feeds page title, H1, first 500 words, and target keyword into OpenAI&#8217;s GPT-4o chat completions API with a system prompt engineered for SERP snippet optimization. The generator enforces a 150-160 character limit on output, includes the primary keyword naturally within the first 80 characters, and adds a clear call-to-action or value proposition. Each generated description is checked against existing descriptions loaded from Screaming Frog CSV crawl exports to prevent duplicates. Similarity scoring via SequenceMatcher flags descriptions that are too close to existing ones. Output formats include a CSV with URL, current description, and proposed description columns for editorial review, plus a Yoast SEO-compatible import file using the wpseo_metadesc post meta key. For WordPress sites, the tool can directly update meta descriptions through the REST API by patching yoast_head_json metadata. Batch processing uses asyncio with rate-limited concurrent API calls to handle sites with thousands of pages efficiently, respecting OpenAI&#8217;s tokens-per-minute limits.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ai-meta-description-generator/)
