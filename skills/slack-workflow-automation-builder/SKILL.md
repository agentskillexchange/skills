---
title: "Slack Workflow Automation Builder"
description: "The Slack Workflow Automation Builder programmatically creates and deploys Slack workflows using the Slack Web API and Bolt SDK framework. It constructs interactive workflows using Block Kit components—modal dialogs with input fields, multi-select menus, date pickers, and overflow menus for complex data collection. The skill builds approval workflows that route requests through configurable chains using Slack message actions and button callbacks, tracking approval state in a Redis-backed store. For standup automation, it deploys scheduled messages via chat.scheduleMessage that collect team updates through threaded responses, then aggregates and formats summaries into designated channels. Incident response workflows automatically create dedicated channels with conversations.create, invite on-call responders using usergroups.users.list integration with PagerDuty, pin runbook links, and set channel topics with incident metadata. The skill manages OAuth scopes and bot token permissions, handles rate limiting with the Slack retry headers (Retry-After), and implements event subscription verification for the Events API challenge handshake. Interactive component payloads are processed through the Bolt middleware chain with proper acknowledgment within the 3-second Slack timeout requirement."
source: "https://github.com/slackapi/bolt-js"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
---

# Slack Workflow Automation Builder

The Slack Workflow Automation Builder programmatically creates and deploys Slack workflows using the Slack Web API and Bolt SDK framework. It constructs interactive workflows using Block Kit components—modal dialogs with input fields, multi-select menus, date pickers, and overflow menus for complex data collection. The skill builds approval workflows that route requests through configurable chains using Slack message actions and button callbacks, tracking approval state in a Redis-backed store. For standup automation, it deploys scheduled messages via chat.scheduleMessage that collect team updates through threaded responses, then aggregates and formats summaries into designated channels. Incident response workflows automatically create dedicated channels with conversations.create, invite on-call responders using usergroups.users.list integration with PagerDuty, pin runbook links, and set channel topics with incident metadata. The skill manages OAuth scopes and bot token permissions, handles rate limiting with the Slack retry headers (Retry-After), and implements event subscription verification for the Events API challenge handshake. Interactive component payloads are processed through the Bolt middleware chain with proper acknowledgment within the 3-second Slack timeout requirement.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-automation-builder/)
