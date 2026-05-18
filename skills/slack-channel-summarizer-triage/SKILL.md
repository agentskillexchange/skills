---
name: "Slack Channel Summarizer & Triage Bot"
slug: "slack-channel-summarizer-triage"
description: "Connects to the Slack Web API to fetch unread messages across specified channels and surfaces a prioritized digest of action items, decisions, and blockers. Uses conversation.history and users.info endpoints to attribute messages correctly. Supports scheduled digests and posts summaries directly to a designated DM or channel."
github_stars: 2900
verification: "security_reviewed"
source: "https://github.com/slackapi/bolt-js"
category: "Integrations & Connectors"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
---

# Slack Channel Summarizer & Triage Bot

Connects to the Slack Web API to fetch unread messages across specified channels and surfaces a prioritized digest of action items, decisions, and blockers. Uses conversation.history and users.info endpoints to attribute messages correctly. Supports scheduled digests and posts summaries directly to a designated DM or channel.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-channel-summarizer-triage/)
