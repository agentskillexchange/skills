---
name: Reddit Subreddit Sentiment Tracker
description: Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.
category: Data Extraction &amp; Transformation
framework: Any Agent
verification: security_reviewed
rating: 4.1
reviews: 52
source: https://agentskillexchange.com/skill/reddit-subreddit-sentiment-tracker/
---

# Reddit Subreddit Sentiment Tracker

Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.

## Overview

Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill reddit-subreddit-sentiment-tracker
```

### OpenClaw

```bash
clawhub install reddit-subreddit-sentiment-tracker
```

### Claude Code

```bash
claude mcp add reddit-subreddit-sentiment-tracker
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/reddit-subreddit-sentiment-tracker/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Data Extraction &amp; Transformation
- **Framework**: Any Agent
- **Rating**: 4.1/5 (52 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/reddit-subreddit-sentiment-tracker/)
