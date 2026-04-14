---
title: "Slack Standup Automator"
description: "Automates daily standup collection and reporting in Slack using the Slack Web API chat.postMessage and conversations.history methods. Supports threaded responses and scheduled summaries via chat.scheduleMessage."
verification: security_reviewed
source: "https://github.com/slackapi/bolt-js"
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

The Slack Standup Automator skill manages daily standup ceremonies for distributed teams using the Slack Web API. It posts standup prompts via chat.postMessage with Block Kit interactive elements including input blocks for yesterday/today/blockers fields. Responses are collected through the conversations.history endpoint filtered by thread_ts for organized threaded discussions. The skill uses chat.scheduleMessage to send prompts at team-configured times across multiple timezones, respecting users.info timezone data from each participant’s profile. Summary reports are generated using rich Block Kit layouts with section, divider, and context blocks. The skill tracks participation rates using conversations.members to identify who hasn’t responded and sends reminder DMs via chat.postMessage to the user’s DM channel obtained from conversations.open. Historical standup data is aggregated for weekly and sprint-level reports with trend analysis on blocker frequency. Integration with the Slack Events API enables real-time response processing without polling overhead.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-standup-automator/)
