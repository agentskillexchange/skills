---
name: "Reddit Subreddit Sentiment Tracker"
description: "Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week."
category: "Data Extraction & Transformation"
framework: "Codex"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/"
tool_ecosystem:
  tool: "slack"
  github_stars: 2900
  npm_weekly_downloads: 2433529
  github_repo: "slackapi/bolt-js"
  license: "MIT"
  maintained: true
---

# Reddit Subreddit Sentiment Tracker

Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill reddit-subreddit-sentiment-tracker
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill reddit-subreddit-sentiment-tracker -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill reddit-subreddit-sentiment-tracker -a cursor
```

### OpenClaw
```bash
clawhub install reddit-subreddit-sentiment-tracker
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill reddit-subreddit-sentiment-tracker -a codex
```

## Details

| | |
|---|---|
| **Category** | Data Extraction & Transformation |
| **Framework** | Codex |
| **Verification** | 📋 Listed |
| **Tool** | [slack](https://github.com/slackapi/bolt-js) — ⭐ 2.9k · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
