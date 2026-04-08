---
title: Slack Workflow Bot Builder
description: The Slack Workflow Bot Builder constructs interactive automation workflows
  within Slack using the Bolt.js framework and Block Kit UI components. It registers
  slash commands through app.command(), creates rich modal interfaces via views.open()
  with input blocks, and handles user interactions through app.action() listeners.
  The skill builds multi-step workflows using Block Kit’s section, input, and actions
  blocks with interactive elements like static_select, multi_external_select, and
  datepicker components. It chains workflow steps through view_submission handlers
  that trigger subsequent views or post formatted messages via chat.postMessage with
  Block Kit attachments. Key features include conversation-scoped data persistence
  using Bolt’s built-in context store, scheduled message delivery through chat.scheduleMessage,
  and threaded conversation management via reply_broadcast. The builder supports Slack
  Connect for cross-organization workflows, implements app home tabs through app.event(“app_home_opened”)
  with dynamic content, and uses conversations.history for context-aware response
  generation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/slack-workflow-bot-builder/
category:
- Calendar, Email &amp; Productivity
framework:
- MCP
---

# Slack Workflow Bot Builder

The Slack Workflow Bot Builder constructs interactive automation workflows within Slack using the Bolt.js framework and Block Kit UI components. It registers slash commands through app.command(), creates rich modal interfaces via views.open() with input blocks, and handles user interactions through app.action() listeners. The skill builds multi-step workflows using Block Kit’s section, input, and actions blocks with interactive elements like static_select, multi_external_select, and datepicker components. It chains workflow steps through view_submission handlers that trigger subsequent views or post formatted messages via chat.postMessage with Block Kit attachments. Key features include conversation-scoped data persistence using Bolt’s built-in context store, scheduled message delivery through chat.scheduleMessage, and threaded conversation management via reply_broadcast. The builder supports Slack Connect for cross-organization workflows, implements app home tabs through app.event(“app_home_opened”) with dynamic content, and uses conversations.history for context-aware response generation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-bot-builder/)
