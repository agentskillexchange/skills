---
title: "Slack Standup Automator"
description: "The Slack Standup Automator skill manages daily standup ceremonies for distributed teams using the Slack Web API. It posts standup prompts via chat.postMessage with Block Kit interactive elements including input blocks for yesterday/today/blockers fields. Responses are collected through the conversations.history endpoint filtered by thread_ts for organized threaded discussions. The skill uses chat.scheduleMessage to send prompts at team-configured times across multiple timezones, respecting users.info timezone data from each participant&#8217;s profile. Summary reports are generated using rich Block Kit layouts with section, divider, and context blocks. The skill tracks participation rates using conversations.members to identify who hasn&#8217;t responded and sends reminder DMs via chat.postMessage to the user&#8217;s DM channel obtained from conversations.open. Historical standup data is aggregated for weekly and sprint-level reports with trend analysis on blocker frequency. Integration with the Slack Events API enables real-time response processing without polling overhead."
source: "https://github.com/slackapi/bolt-js"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
---

# Slack Standup Automator

The Slack Standup Automator skill manages daily standup ceremonies for distributed teams using the Slack Web API. It posts standup prompts via chat.postMessage with Block Kit interactive elements including input blocks for yesterday/today/blockers fields. Responses are collected through the conversations.history endpoint filtered by thread_ts for organized threaded discussions. The skill uses chat.scheduleMessage to send prompts at team-configured times across multiple timezones, respecting users.info timezone data from each participant&#8217;s profile. Summary reports are generated using rich Block Kit layouts with section, divider, and context blocks. The skill tracks participation rates using conversations.members to identify who hasn&#8217;t responded and sends reminder DMs via chat.postMessage to the user&#8217;s DM channel obtained from conversations.open. Historical standup data is aggregated for weekly and sprint-level reports with trend analysis on blocker frequency. Integration with the Slack Events API enables real-time response processing without polling overhead.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-standup-automator/)
