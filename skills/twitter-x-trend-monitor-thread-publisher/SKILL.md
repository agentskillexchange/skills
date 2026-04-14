---
title: "Twitter/X Trend Monitor & Thread Publisher"
slug: "twitter-x-trend-monitor-thread-publisher"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/"
category:
  - "Templates &amp; Workflows"
framework:
  - "OpenClaw"
---
# Twitter/X Trend Monitor & Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/)
