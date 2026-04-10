---
name: Slack Workflow Bot Builder
description: Creates interactive Slack workflows using Block Kit UI components and
  the Bolt.js framework. Implements slash commands, modal views via views.open(),
  and message shortcuts with action listeners.
verification: security_reviewed
source: https://agentskillexchange.com/skills/slack-workflow-bot-builder/
category:
- Calendar, Email &amp; Productivity
framework:
- MCP
---
# Slack Workflow Bot Builder

The Slack Workflow Bot Builder constructs interactive automation workflows within Slack using the Bolt.js framework and Block Kit UI components. It registers slash commands through app.command(), creates rich modal interfaces via views.open() with input blocks, and handles user interactions through app.action() listeners.
The skill builds multi-step workflows using Block Kit's section, input, and actions blocks with interactive elements like static_select, multi_external_select, and datepicker components. It chains workflow steps through view_submission handlers that trigger subsequent views or post formatted messages via chat.postMessage with Block Kit attachments.
Key features include conversation-scoped data persistence using Bolt's built-in context store, scheduled message delivery through chat.scheduleMessage, and threaded conversation management via reply_broadcast. The builder supports Slack Connect for cross-organization workflows, implements app home tabs through app.event(&#8220;app_home_opened&#8221;) with dynamic content, and uses conversations.history for context-aware response generation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-bot-builder/)
