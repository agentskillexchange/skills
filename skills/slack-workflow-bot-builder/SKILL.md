---
title: "Slack Workflow Bot Builder"
description: "Creates interactive Slack workflows using Block Kit UI components and the Bolt.js framework. Implements slash commands, modal views via views.open(), and message shortcuts with action listeners."
verification: "security_reviewed"
source: "https://github.com/slackapi/bolt-js"
category:
  - "Calendar, Email & Productivity"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
---

# Slack Workflow Bot Builder

The Slack Workflow Bot Builder constructs interactive automation workflows within Slack using the Bolt.js framework and Block Kit UI components. It registers slash commands through app.command(), creates rich modal interfaces via views.open() with input blocks, and handles user interactions through app.action() listeners. The skill builds multi-step workflows using Block Kit’s section, input, and actions blocks with interactive elements like static_select, multi_external_select, and datepicker components. It chains workflow steps through view_submission handlers that trigger subsequent views or post formatted messages via chat.postMessage with Block Kit attachments. Key features include conversation-scoped data persistence using Bolt’s built-in context store, scheduled message delivery through chat.scheduleMessage, and threaded conversation management via reply_broadcast. The builder supports Slack Connect for cross-organization workflows, implements app home tabs through app.event(“app_home_opened”) with dynamic content, and uses conversations.history for context-aware response generation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/slack-workflow-bot-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/slack-workflow-bot-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/slack-workflow-bot-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-bot-builder/)
