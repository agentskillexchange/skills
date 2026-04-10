---
title: "Slack Workflow Bot"
description: "Builds interactive Slack workflows using the Bolt SDK for JavaScript and Block Kit Builder API. Handles modal forms, scheduled messages, and webhook integrations."
slug: "slack-workflow-bot-bolt-sdk"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/slack-workflow-bot-bolt-sdk/"
---

# Slack Workflow Bot

Builds interactive Slack workflows using the Bolt SDK for JavaScript and Block Kit Builder API. Handles modal forms, scheduled messages, and webhook integrations.

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
clawhub install slack-workflow-bot-bolt-sdk
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Slack Workflow Bot uses the Bolt SDK for JavaScript to create interactive workflow automations within Slack workspaces. It constructs rich Block Kit interfaces for approval flows, form submissions, and interactive polls using the Block Kit Builder API. The bot handles OAuth 2.0 installation flows for multi-workspace distribution, manages Socket Mode connections for development environments, and supports Slack Event API subscriptions for real-time message processing. Scheduled message delivery uses the chat.scheduleMessage API with timezone-aware scheduling. Integration with Slack Workflow Builder enables custom steps that connect to external APIs. The tool implements conversation store patterns for multi-turn interactions, handles rate limiting with exponential backoff, and supports Slack Enterprise Grid organization-level deployments. Audit logging tracks all workflow executions for compliance.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-bot-bolt-sdk/)
