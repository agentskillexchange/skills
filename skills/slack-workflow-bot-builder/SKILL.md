---
title: "Slack Workflow Bot Builder"
description: "Creates interactive Slack workflows using Block Kit UI components and the Bolt.js framework. Implements slash commands, modal views via views.open(), and message shortcuts with action listeners."
slug: "slack-workflow-bot-builder"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/slack-workflow-bot-builder/"
---

# Slack Workflow Bot Builder

Creates interactive Slack workflows using Block Kit UI components and the Bolt.js framework. Implements slash commands, modal views via views.open(), and message shortcuts with action listeners.

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
clawhub install slack-workflow-bot-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Slack Workflow Bot Builder constructs interactive automation workflows within Slack using the Bolt.js framework and Block Kit UI components. It registers slash commands through app.command(), creates rich modal interfaces via views.open() with input blocks, and handles user interactions through app.action() listeners.
The skill builds multi-step workflows using Block Kit’s section, input, and actions blocks with interactive elements like static_select, multi_external_select, and datepicker components. It chains workflow steps through view_submission handlers that trigger subsequent views or post formatted messages via chat.postMessage with Block Kit attachments.
Key features include conversation-scoped data persistence using Bolt’s built-in context store, scheduled message delivery through chat.scheduleMessage, and threaded conversation management via reply_broadcast. The builder supports Slack Connect for cross-organization workflows, implements app home tabs through app.event(“app_home_opened”) with dynamic content, and uses conversations.history for context-aware response generation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-bot-builder/)
