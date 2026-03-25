---
name: "Twitter/X Trend Monitor & Thread Publisher"
description: "Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits."
category: "Templates & Workflows"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
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

**Twitter/X Trend Monitor & Thread Publisher** is built around Redis in-memory datastore. The underlying ecosystem is represented by `redis/redis` (73,523+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like keys, hashes, TTLs, streams, pub/sub, sorted sets, locks and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to redis so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits. The implementation typically relies on keys, hashes, TTLs, streams, pub/sub, sorted sets, locks, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses keys, hashes, TTLs, streams, pub/sub, sorted sets, locks instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as caching, queues, rate limiting, and fast shared state.

Key integration points include caching, queues, rate limiting, and fast shared state. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

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
