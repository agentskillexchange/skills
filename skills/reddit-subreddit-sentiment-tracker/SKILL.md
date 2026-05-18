---
name: "Reddit Subreddit Sentiment Tracker"
slug: "reddit-subreddit-sentiment-tracker"
description: "Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week."
verification: "security_reviewed"
source: "https://www.reddit.com/dev/api/"
author: "Reddit"
category: "Data Extraction & Transformation"
framework: "Codex"
---

# Reddit Subreddit Sentiment Tracker

Uses the Reddit OAuth2 API via PRAW to collect top posts and comments from subreddits on a rolling 24-hour window, then runs batch sentiment scoring via HuggingFace Inference API using twitter-roberta-base-sentiment. Aggregates scores into a daily time-series written to Google Sheets for Looker Studio visualization. Fires Slack alerts when sentiment drops more than 20 points week-over-week.

## Installation

Requirements and caveats from upstream:
- A modhash is a token that the reddit API requires to help prevent
- with new images. If only the permissions on an emoji require updating
- Requires a string 'flair_csv' which has up to 100 lines of the form

Basic usage or getting-started notes:
- example, t3_15bfi0 .
- for posts. For example, casual conversation may be better sorted by new
- example by creating a text field in their app that does not allow

- Source: https://www.reddit.com/dev/api/

## Documentation

- https://www.reddit.com/dev/api/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reddit-subreddit-sentiment-tracker/)
