---
title: "Twitter/X Trend Monitor & Thread Publisher"
slug: "twitter-x-trend-monitor-thread-publisher"
description: "Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/"
category: "Templates &amp; Workflows"
framework: "OpenClaw"
---
# Twitter/X Trend Monitor & Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

Choose the installation path that fits your setup:

1. Install from Agent Skill Exchange in the OpenClaw UI.
2. Copy the skill folder into your local skills directory.
3. Add it to your shared workspace skills collection.
4. Install it through a compatible agent skill manager.
5. Clone or download the upstream source and wire it into your agent runtime.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/)
