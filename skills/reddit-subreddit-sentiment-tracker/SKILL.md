---
title: "Reddit Subreddit Sentiment Tracker"
slug: "reddit-subreddit-sentiment-tracker"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Codex"
---
# Reddit Subreddit Sentiment Tracker

Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/)
