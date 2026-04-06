---
title: "Twitter/X Trend Monitor &amp; Thread Publisher"
description: "Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/"
category: ["Templates &amp; Workflows"]
framework: ["OpenClaw"]
---

# Twitter/X Trend Monitor &amp; Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI.
2. Add it through your agent or assistant skill manager.
3. Clone or copy this skill into your local skills directory.
4. Install with a package manager if the upstream project provides one.
5. Follow the upstream project documentation for manual setup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/)
