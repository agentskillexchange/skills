---
title: "Twitter/X Trend Monitor &amp; Thread Publisher"
slug: "twitter-x-trend-monitor-thread-publisher"
description: "Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/"
category: "Templates &amp; Workflows"
framework: "OpenClaw"
---
# Twitter/X Trend Monitor &amp; Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

1. Clone this skill repository.
2. Open this skill folder.
3. Review prerequisites and setup needs.
4. Install required dependencies.
5. Run and test in your environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/)
