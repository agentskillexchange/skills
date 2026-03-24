---
name: "Reddit Subreddit Sentiment Tracker"
description: "Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week."
category: "Data Extraction & Transformation"
framework: "Codex"
verification: security_reviewed
rating: 4.1
reviews: 52
creator: "Sofia Petrov"
creator_handle: "@sofiapetrov"
creator_verified: true
source: "https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/"
---
# Reddit Subreddit Sentiment Tracker

Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Data Extraction & Transformation |
| Framework | Codex |
| Verification | Security Reviewed |
| Rating | 4.1/5 (52 reviews) |

## Creator

**Sofia Petrov** (Verified Creator ✓)
- Profile: [@sofiapetrov](https://agentskillexchange.com/browse-skills/?creator=sofiapetrov)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/reddit-subreddit-sentiment-tracker/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
