---
title: "Reddit Subreddit Sentiment Tracker"
slug: "reddit-subreddit-sentiment-tracker"
description: "Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week."
verification: security_reviewed
source: "https://www.reddit.com/dev/api/"
framework:
  - "Codex"
---

# Reddit Subreddit Sentiment Tracker

Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/)
