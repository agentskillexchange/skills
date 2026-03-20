---
name: Twitter/X Trend Monitor & Thread Publisher
description: Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.
category: Templates &amp; Workflows
framework: Any Agent
verification: verified_metadata
rating: 4.1
reviews: 46
source: https://agentskillexchange.com/skill/twitter-x-trend-monitor-thread-publisher/
---

# Twitter/X Trend Monitor & Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Overview

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill twitter-x-trend-monitor-thread-publisher
```

### OpenClaw

```bash
clawhub install twitter-x-trend-monitor-thread-publisher
```

### Claude Code

```bash
claude mcp add twitter-x-trend-monitor-thread-publisher
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/twitter-x-trend-monitor-thread-publisher/) for detailed installation instructions.

## Verification

- **Status**: verified_metadata
- **Category**: Templates &amp; Workflows
- **Framework**: Any Agent
- **Rating**: 4.1/5 (46 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/twitter-x-trend-monitor-thread-publisher/)
