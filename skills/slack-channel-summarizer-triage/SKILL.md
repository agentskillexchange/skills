---
title: "Slack Channel Summarizer & Triage Bot"
description: "Connects to the Slack Web API to fetch unread messages across specified channels and surfaces a prioritized digest of action items, decisions, and blockers. Uses conversation.history and users.info endpoints to attribute messages correctly. Supports scheduled digests and posts summaries directly to a designated DM or channel."
verification: security_reviewed
source: "https://github.com/slackapi/bolt-js"
category:
  - "Integrations & Connectors"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
---

# Slack Channel Summarizer & Triage Bot

Connects to the Slack Web API to fetch unread messages across specified channels and surfaces a prioritized digest of action items, decisions, and blockers. Uses conversation.history and users.info endpoints to attribute messages correctly. Supports scheduled digests and posts summaries directly to a designated DM or channel.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/slack-channel-summarizer-triage/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/slack-channel-summarizer-triage
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/slack-channel-summarizer-triage`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-channel-summarizer-triage/)
