---
name: "Slack Standup Automator"
description: "Automates daily standup collection and reporting in Slack using the Slack Web API chat.postMessage and conversations.history methods. Supports threaded responses and scheduled summaries via chat.scheduleMessage."
category: "Calendar, Email & Productivity"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/slack-standup-automator/"
---
# Slack Standup Automator

Automates daily standup collection and reporting in Slack using the Slack Web API chat.postMessage and conversations.history methods. Supports threaded responses and scheduled summaries via chat.scheduleMessage.

## Overview

The Slack Standup Automator skill manages daily standup ceremonies for distributed teams using the Slack Web API. It posts standup prompts via chat.postMessage with Block Kit interactive elements including input blocks for yesterday/today/blockers fields. Responses are collected through the conversations.history endpoint filtered by thread_ts for organized threaded discussions. The skill uses chat.scheduleMessage to send prompts at team-configured times across multiple timezones, respecting users.info timezone data from each participant’s profile. Summary reports are generated using rich Block Kit layouts with section, divider, and context blocks. The skill tracks participation rates using conversations.members to identify who hasn’t responded and sends reminder DMs via chat.postMessage to the user’s DM channel obtained from conversations.open. Historical standup data is aggregated for weekly and sprint-level reports with trend analysis on blocker frequency. Integration with the Slack Events API enables real-time response processing without polling overhead.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-standup-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-standup-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-standup-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-standup-automator -a codex
```

### OpenClaw

```bash
clawhub install slack-standup-automator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-standup-automator/)
