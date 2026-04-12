---
title: "Reddit Subreddit Sentiment Tracker"
description: "Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/"
categories:
  - "Data Extraction &amp; Transformation"
frameworks:
  - "Codex"
---

# Reddit Subreddit Sentiment Tracker

Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.

## Installation

You can install this skill using one of these methods:

1. Install from Agent Skill Exchange in OpenClaw
2. Install from ClawHub
3. Copy the skill folder into your local skills directory
4. Add it as a git submodule or synced folder in your workspace
5. Use your team or org skill distribution workflow

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/)
