---
title: "Slack Workflow Builder Agent"
description: "Creates and manages Slack workflows using @slack/bolt and @slack/web-api. Builds interactive modals with Block Kit, handles slash commands, and orchestrates multi-step approval flows via Slack Events API."
verification: "security_reviewed"
source: "https://github.com/slackapi/bolt-js"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  ase_npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
  license: "MIT"
---

# Slack Workflow Builder Agent

The Slack Workflow Builder Agent automates complex team workflows using @slack/bolt for event handling and @slack/web-api for programmatic Slack interaction. It creates rich interactive experiences using Block Kit components including modals, message attachments, and action buttons.


The agent handles slash command registration and processing, building multi-step approval workflows where each step triggers the next based on user interaction. It manages channel creation, archival, and topic updates programmatically, and supports threaded conversation management for organized team discussions.


Advanced features include scheduled message delivery using chat.scheduleMessage, user group management via usergroups API methods, and file sharing automation through files.upload v2. The agent implements Slack Events API subscriptions for real-time message monitoring, reaction tracking, and channel membership changes. It also builds custom Home Tab experiences using the views.publish endpoint for personalized dashboards.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-builder-agent/)
