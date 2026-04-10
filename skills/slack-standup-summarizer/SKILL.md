---
title: "Slack Standup Summarizer"
description: "Collects daily standup updates from Slack channels using the Web API and generates team summaries with blockers highlighted. Posts formatted digests via Incoming Webhooks."
slug: "slack-standup-summarizer"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/slack-standup-summarizer/"
---

# Slack Standup Summarizer

Collects daily standup updates from Slack channels using the Web API and generates team summaries with blockers highlighted. Posts formatted digests via Incoming Webhooks.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install slack-standup-summarizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Slack Standup Summarizer skill monitors designated Slack channels for daily standup messages using the conversations.history Web API endpoint. It identifies standup entries by timestamp windows, thread patterns, or bot-prompted responses and extracts structured data from free-form updates.
The summarizer parses standup messages to identify three components: completed work, planned work, and blockers. Natural language processing detects blocker keywords and escalation signals even when not explicitly formatted. Cross-referencing with Jira or Linear ticket numbers provides automatic status linking.
Digest generation produces formatted Slack Block Kit messages with sections for each team member, highlighted blockers with suggested owners, and sprint progress indicators. Digests post to configurable channels via Incoming Webhooks with optional threading under a daily parent message. Historical data aggregation tracks individual velocity trends, recurring blockers, and team completion rates over configurable time windows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-standup-summarizer/)
