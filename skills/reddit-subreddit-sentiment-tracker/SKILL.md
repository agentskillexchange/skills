---
title: "Reddit Subreddit Sentiment Tracker"
description: "Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week."
slug: "reddit-subreddit-sentiment-tracker"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/"
category:
  - "Data Extraction & Transformation"
framework:
  - "Codex"
---
# Reddit Subreddit Sentiment Tracker

Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Add as a local skill folder
3. Install from a Git repository
4. Install via package manager if supported
5. Copy the skill into your OpenClaw skills directory

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/)
