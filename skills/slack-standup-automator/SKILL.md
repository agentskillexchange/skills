---
title: "Slack Standup Automator"
description: "Automates daily standup collection and reporting in Slack using the Slack Web API chat.postMessage and conversations.history methods. Supports threaded responses and scheduled summaries via chat.scheduleMessage."
slug: "slack-standup-automator"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/slack-standup-automator/"
---

# Slack Standup Automator

Automates daily standup collection and reporting in Slack using the Slack Web API chat.postMessage and conversations.history methods. Supports threaded responses and scheduled summaries via chat.scheduleMessage.

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
clawhub install slack-standup-automator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Slack Standup Automator skill manages daily standup ceremonies for distributed teams using the Slack Web API. It posts standup prompts via chat.postMessage with Block Kit interactive elements including input blocks for yesterday/today/blockers fields. Responses are collected through the conversations.history endpoint filtered by thread_ts for organized threaded discussions. The skill uses chat.scheduleMessage to send prompts at team-configured times across multiple timezones, respecting users.info timezone data from each participant’s profile. Summary reports are generated using rich Block Kit layouts with section, divider, and context blocks. The skill tracks participation rates using conversations.members to identify who hasn’t responded and sends reminder DMs via chat.postMessage to the user’s DM channel obtained from conversations.open. Historical standup data is aggregated for weekly and sprint-level reports with trend analysis on blocker frequency. Integration with the Slack Events API enables real-time response processing without polling overhead.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-standup-automator/)
