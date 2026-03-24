---
name: "Twitter/X Trend Monitor & Thread Publisher"
description: "Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits."
category: "Templates & Workflows"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "redis"  # from ase_tool_match
  github_stars: 73523  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8224050  # from ase_npm_downloads
  github_repo: "redis/redis"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Twitter/X Trend Monitor & Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Overview

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill twitter-x-trend-monitor-thread-publisher
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill twitter-x-trend-monitor-thread-publisher -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill twitter-x-trend-monitor-thread-publisher -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill twitter-x-trend-monitor-thread-publisher -a codex
```

### OpenClaw

```bash
clawhub install twitter-x-trend-monitor-thread-publisher
```

## Source

- Marketplace: https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/
