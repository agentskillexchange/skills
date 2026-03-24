---
name: "Twitter/X Trend Monitor & Thread Publisher"
description: "Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits."
category: "Templates & Workflows"
framework: "OpenClaw"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/"
tool_ecosystem:
  tool: "redis"
  github_stars: 73523
  npm_weekly_downloads: 8224050
  github_repo: "redis/redis"
  license: "NOASSERTION"
  maintained: true
---

# Twitter/X Trend Monitor & Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

### Any Agent (npx)
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

### OpenClaw
```bash
clawhub install twitter-x-trend-monitor-thread-publisher
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill twitter-x-trend-monitor-thread-publisher -a codex
```

## Details

| | |
|---|---|
| **Category** | Templates & Workflows |
| **Framework** | OpenClaw |
| **Verification** | 📋 Listed |
| **Tool** | [redis](https://github.com/redis/redis) — ⭐ 73.5k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
