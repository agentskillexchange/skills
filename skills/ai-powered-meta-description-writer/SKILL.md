---
title: AI-Powered Meta Description Writer
description: This skill automates meta description generation for large-scale websites
  using the OpenAI Chat Completions API with gpt-4o-mini for cost efficiency. It fetches
  existing page content through the WordPress REST API, extracts key themes using
  TF-IDF scoring, and generates compelling meta descriptions within the 155-character
  SERP display limit. The agent integrates directly with Yoast SEO plugin REST fields
  (yoast_head_json.description) for seamless WordPress updates. Each generated description
  includes the primary target keyword within the first 70 characters, a clear value
  proposition, and a call-to-action phrase. Google SERP Preview validation checks
  pixel width rendering using a canvas measureText approximation to ensure descriptions
  display without truncation on desktop and mobile. The skill processes pages in batches
  of 50, using wp_remote_post() for OpenAI API calls with configurable temperature
  settings. A/B testing support generates multiple variants per page with confidence
  interval tracking. Performance tracking integrates with Google Search Console API
  to measure CTR changes post-update.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ai-powered-meta-description-writer/
category:
- Content Writing &amp; SEO
framework:
- Claude Code
---

# AI-Powered Meta Description Writer

This skill automates meta description generation for large-scale websites using the OpenAI Chat Completions API with gpt-4o-mini for cost efficiency. It fetches existing page content through the WordPress REST API, extracts key themes using TF-IDF scoring, and generates compelling meta descriptions within the 155-character SERP display limit. The agent integrates directly with Yoast SEO plugin REST fields (yoast_head_json.description) for seamless WordPress updates. Each generated description includes the primary target keyword within the first 70 characters, a clear value proposition, and a call-to-action phrase. Google SERP Preview validation checks pixel width rendering using a canvas measureText approximation to ensure descriptions display without truncation on desktop and mobile. The skill processes pages in batches of 50, using wp_remote_post() for OpenAI API calls with configurable temperature settings. A/B testing support generates multiple variants per page with confidence interval tracking. Performance tracking integrates with Google Search Console API to measure CTR changes post-update.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ai-powered-meta-description-writer/)
