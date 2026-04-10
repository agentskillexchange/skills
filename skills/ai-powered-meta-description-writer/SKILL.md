---
name: "AI-Powered Meta Description Writer"
description: "Generates optimized meta descriptions using OpenAI Chat Completions API with token-aware truncation. Integrates with Yoast SEO REST API fields and Google SERP Preview validation for CTR optimization."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ai-powered-meta-description-writer/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Claude Code"
---

# AI-Powered Meta Description Writer

This skill automates meta description generation for large-scale websites using the OpenAI Chat Completions API with gpt-4o-mini for cost efficiency. It fetches existing page content through the WordPress REST API, extracts key themes using TF-IDF scoring, and generates compelling meta descriptions within the 155-character SERP display limit. The agent integrates directly with Yoast SEO plugin REST fields (yoast_head_json.description) for seamless WordPress updates. Each generated description includes the primary target keyword within the first 70 characters, a clear value proposition, and a call-to-action phrase. Google SERP Preview validation checks pixel width rendering using a canvas measureText approximation to ensure descriptions display without truncation on desktop and mobile. The skill processes pages in batches of 50, using wp_remote_post() for OpenAI API calls with configurable temperature settings. A/B testing support generates multiple variants per page with confidence interval tracking. Performance tracking integrates with Google Search Console API to measure CTR changes post-update.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ai-powered-meta-description-writer/)
