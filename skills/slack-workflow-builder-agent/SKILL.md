---
name: "Slack Workflow Builder Agent"
description: "Creates and manages Slack workflows using @slack/bolt and @slack/web-api. Builds interactive modals with Block Kit, handles slash commands, and orchestrates multi-step approval flows via Slack Events API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/slack-workflow-builder-agent/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Cursor"
---

# Slack Workflow Builder Agent

The Slack Workflow Builder Agent automates complex team workflows using @slack/bolt for event handling and @slack/web-api for programmatic Slack interaction. It creates rich interactive experiences using Block Kit components including modals, message attachments, and action buttons.
The agent handles slash command registration and processing, building multi-step approval workflows where each step triggers the next based on user interaction. It manages channel creation, archival, and topic updates programmatically, and supports threaded conversation management for organized team discussions.
Advanced features include scheduled message delivery using chat.scheduleMessage, user group management via usergroups API methods, and file sharing automation through files.upload v2. The agent implements Slack Events API subscriptions for real-time message monitoring, reaction tracking, and channel membership changes. It also builds custom Home Tab experiences using the views.publish endpoint for personalized dashboards.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-builder-agent/)
