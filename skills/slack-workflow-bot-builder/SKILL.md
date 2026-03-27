---
name: "Slack Workflow Bot Builder"
description: "Creates interactive Slack workflows using Block Kit UI components and the Bolt.js framework. Implements slash commands, modal views via views.open(), and message shortcuts with action listeners."
category: "Calendar, Email & Productivity"
framework: "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/slack-workflow-bot-builder/"
tool_ecosystem:
  tool: slack
  github_stars: 2899
  npm_weekly_downloads: 2433529
  github_repo: slackapi/bolt-js
  license: MIT
  maintained: true
---

# Slack Workflow Bot Builder

Creates interactive Slack workflows using Block Kit UI components and the Bolt.js framework. Implements slash commands, modal views via views.open(), and message shortcuts with action listeners.

## Overview

The Slack Workflow Bot Builder constructs interactive automation workflows within Slack using the Bolt.js framework and Block Kit UI components. It registers slash commands through app.command(), creates rich modal interfaces via views.open() with input blocks, and handles user interactions through app.action() listeners.

The skill builds multi-step workflows using Block Kit’s section, input, and actions blocks with interactive elements like static_select, multi_external_select, and datepicker components. It chains workflow steps through view_submission handlers that trigger subsequent views or post formatted messages via chat.postMessage with Block Kit attachments.

Key features include conversation-scoped data persistence using Bolt’s built-in context store, scheduled message delivery through chat.scheduleMessage, and threaded conversation management via reply_broadcast. The builder supports Slack Connect for cross-organization workflows, implements app home tabs through app.event(“app_home_opened”) with dynamic content, and uses conversations.history for context-aware response generation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-bot-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-bot-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-bot-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-bot-builder -a codex
```

### OpenClaw

```bash
clawhub install slack-workflow-bot-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/slack-workflow-bot-builder/
