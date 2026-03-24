---
name: "Twitter/X Trend Monitor & Thread Publisher"
description: "Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits."
category: "Templates & Workflows"
framework: "OpenClaw"
verification: verified_metadata
rating: 4.1
reviews: 46
creator: "Maya Johnson"
creator_handle: "@mayaj"
creator_verified: false
source: "https://agentskillexchange.com/skills/twitter-x-trend-monitor-thread-publisher/"
---
# Twitter/X Trend Monitor & Thread Publisher

Polls the X API v2 trending topics endpoint every 15 minutes and compares against a keyword watchlist stored in Redis. When a trend matches, fetches top tweets by engagement and drafts a summarizing thread via OpenAI Chat Completions. Publishes the thread via X API v2 with reply chaining, respecting OAuth 2.0 PKCE rate limits.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Templates & Workflows |
| Framework | OpenClaw |
| Verification | Verified Metadata |
| Rating | 4.1/5 (46 reviews) |

## Creator

**Maya Johnson**
- Profile: [@mayaj](https://agentskillexchange.com/browse-skills/?creator=mayaj)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/twitter-x-trend-monitor-thread-publisher/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
