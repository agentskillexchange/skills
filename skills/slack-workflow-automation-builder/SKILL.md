---
title: "Slack Workflow Automation Builder"
description: "Creates Slack Workflow Builder automations using the Slack Web API and Block Kit. Builds approval flows, standup collectors, and incident response channels with interactive message components."
verification: "security_reviewed"
source: "https://github.com/slackapi/bolt-js"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  ase_npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
  license: "MIT"
---

# Slack Workflow Automation Builder

The Slack Workflow Automation Builder programmatically creates and deploys Slack workflows using the Slack Web API and Bolt SDK framework. It constructs interactive workflows using Block Kit components—modal dialogs with input fields, multi-select menus, date pickers, and overflow menus for complex data collection. The skill builds approval workflows that route requests through configurable chains using Slack message actions and button callbacks, tracking approval state in a Redis-backed store. For standup automation, it deploys scheduled messages via chat.scheduleMessage that collect team updates through threaded responses, then aggregates and formats summaries into designated channels. Incident response workflows automatically create dedicated channels with conversations.create, invite on-call responders using usergroups.users.list integration with PagerDuty, pin runbook links, and set channel topics with incident metadata. The skill manages OAuth scopes and bot token permissions, handles rate limiting with the Slack retry headers (Retry-After), and implements event subscription verification for the Events API challenge handshake. Interactive component payloads are processed through the Bolt middleware chain with proper acknowledgment within the 3-second Slack timeout requirement.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-automation-builder/)
