---
title: "Reddit Subreddit Sentiment Tracker"
description: "Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/"
category: ["Data Extraction &amp; Transformation"]
framework: ["Codex"]
---

# Reddit Subreddit Sentiment Tracker

Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI.
2. Add it through your agent or assistant skill manager.
3. Clone or copy this skill into your local skills directory.
4. Install with a package manager if the upstream project provides one.
5. Follow the upstream project documentation for manual setup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/)
