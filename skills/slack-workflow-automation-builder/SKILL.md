---
title: "Slack Workflow Automation Builder"
description: "Creates Slack Workflow Builder automations using the Slack Web API and Block Kit. Builds approval flows, standup collectors, and incident response channels with interactive message components."
slug: "slack-workflow-automation-builder"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/slack-workflow-automation-builder/"
---

# Slack Workflow Automation Builder

Creates Slack Workflow Builder automations using the Slack Web API and Block Kit. Builds approval flows, standup collectors, and incident response channels with interactive message components.

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
clawhub install slack-workflow-automation-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Slack Workflow Automation Builder programmatically creates and deploys Slack workflows using the Slack Web API and Bolt SDK framework. It constructs interactive workflows using Block Kit components—modal dialogs with input fields, multi-select menus, date pickers, and overflow menus for complex data collection. The skill builds approval workflows that route requests through configurable chains using Slack message actions and button callbacks, tracking approval state in a Redis-backed store. For standup automation, it deploys scheduled messages via chat.scheduleMessage that collect team updates through threaded responses, then aggregates and formats summaries into designated channels. Incident response workflows automatically create dedicated channels with conversations.create, invite on-call responders using usergroups.users.list integration with PagerDuty, pin runbook links, and set channel topics with incident metadata. The skill manages OAuth scopes and bot token permissions, handles rate limiting with the Slack retry headers (Retry-After), and implements event subscription verification for the Events API challenge handshake. Interactive component payloads are processed through the Bolt middleware chain with proper acknowledgment within the 3-second Slack timeout requirement.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-automation-builder/)
