---
title: "Twitter/X Trend Monitor &amp; Thread Publisher"
slug: "twitter-x-trend-monitor-thread-publisher"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "OpenClaw"
source: "https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/"
---

# Twitter/X Trend Monitor &amp; Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/)
