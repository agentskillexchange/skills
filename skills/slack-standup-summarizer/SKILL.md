---
title: "Slack Standup Summarizer"
description: "Collects daily standup updates from Slack channels using the Web API and generates team summaries with blockers highlighted. Posts formatted digests via Incoming Webhooks."
verification: "security_reviewed"
source: "https://github.com/slackapi/bolt-js"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
---

# Slack Standup Summarizer

The Slack Standup Summarizer skill monitors designated Slack channels for daily standup messages using the conversations.history Web API endpoint. It identifies standup entries by timestamp windows, thread patterns, or bot-prompted responses and extracts structured data from free-form updates. The summarizer parses standup messages to identify three components: completed work, planned work, and blockers. Natural language processing detects blocker keywords and escalation signals even when not explicitly formatted. Cross-referencing with Jira or Linear ticket numbers provides automatic status linking. Digest generation produces formatted Slack Block Kit messages with sections for each team member, highlighted blockers with suggested owners, and sprint progress indicators. Digests post to configurable channels via Incoming Webhooks with optional threading under a daily parent message. Historical data aggregation tracks individual velocity trends, recurring blockers, and team completion rates over configurable time windows.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/slack-standup-summarizer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/slack-standup-summarizer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/slack-standup-summarizer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-standup-summarizer/)
