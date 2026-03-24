---
name: "Hacker News Frontpage Tracker"
description: "Monitors the Hacker News Firebase API for top stories, tracks score velocity, and identifies trending discussions. Uses the /v0/topstories endpoint combined with Algolia HN Search API for comment sentiment analysis and keyword-based alerting."
category: "Research & Scraping"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/hacker-news-frontpage-tracker/"
---

# Hacker News Frontpage Tracker

Monitors the Hacker News Firebase API for top stories, tracks score velocity, and identifies trending discussions. Uses the /v0/topstories endpoint combined with Algolia HN Search API for comment sentiment analysis and keyword-based alerting.

## Overview

Overview

The Hacker News Frontpage Tracker skill provides real-time monitoring of Hacker News stories using the official Firebase API at `https://hacker-news.firebaseio.com/v0/`. It polls `/topstories.json`, `/newstories.json`, and `/beststories.json` endpoints to track which submissions are gaining traction, then fetches individual item details from `/item/<id>.json` to build a complete picture of each story’s trajectory including score, comment count, author, and submission time.

How It Works

The agent maintains a local SQLite database of tracked stories with periodic snapshots of their score and comment count, enabling velocity calculations — stories gaining more than 10 points per minute are flagged as trending. For deeper analysis, the skill queries the Algolia HN Search API at `https://hn.algolia.com/api/v1/search` with filters for date range, story type, and minimum point thresholds. Comment threads are fetched recursively and analyzed for keyword patterns, sentiment polarity (using a simple positive/negative lexicon), and author reputation based on karma scores.

Output and Alerting

Produces a formatted digest with sections for Trending (fast-rising stories), Top Discussion (highest comment-to-score ratio), and New Launches (Show HN / Launch HN posts). Each entry includes the title, URL, current score, comment count, score velocity, and top-3 most-upvoted comments. Supports webhook delivery via HTTP POST to Slack, Discord, or Telegram endpoints. The agent can also filter stories by domain, keyword whitelist, or author to focus monitoring on specific technology topics like Rust, LLMs, or startup fundraising. All API calls respect rate limits with exponential backoff.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hacker-news-frontpage-tracker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hacker-news-frontpage-tracker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hacker-news-frontpage-tracker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hacker-news-frontpage-tracker -a codex
```

### OpenClaw

```bash
clawhub install hacker-news-frontpage-tracker
```

## Source

- Marketplace: https://agentskillexchange.com/skills/hacker-news-frontpage-tracker/
