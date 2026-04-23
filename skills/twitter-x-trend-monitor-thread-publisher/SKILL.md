---
title: "Twitter/X Trend Monitor & Thread Publisher"
description: "Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/"
category:
  - "Templates & Workflows"
framework:
  - "OpenClaw"
---

# Twitter/X Trend Monitor & Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/twitter-x-trend-monitor-thread-publisher
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/twitter-x-trend-monitor-thread-publisher`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/)
