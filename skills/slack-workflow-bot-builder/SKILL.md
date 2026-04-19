---
title: "Slack Workflow Bot Builder"
description: "The Slack Workflow Bot Builder constructs interactive automation workflows within Slack using the Bolt.js framework and Block Kit UI components. It registers slash commands through app.command(), creates rich modal interfaces via views.open() with input blocks, and handles user interactions through app.action() listeners. The skill builds multi-step workflows using Block Kit&#8217;s section, input, and actions blocks with interactive elements like static_select, multi_external_select, and datepicker components. It chains workflow steps through view_submission handlers that trigger subsequent views or post formatted messages via chat.postMessage with Block Kit attachments. Key features include conversation-scoped data persistence using Bolt&#8217;s built-in context store, scheduled message delivery through chat.scheduleMessage, and threaded conversation management via reply_broadcast. The builder supports Slack Connect for cross-organization workflows, implements app home tabs through app.event(&#8220;app_home_opened&#8221;) with dynamic content, and uses conversations.history for context-aware response generation."
source: "https://github.com/slackapi/bolt-js"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
---

# Slack Workflow Bot Builder

The Slack Workflow Bot Builder constructs interactive automation workflows within Slack using the Bolt.js framework and Block Kit UI components. It registers slash commands through app.command(), creates rich modal interfaces via views.open() with input blocks, and handles user interactions through app.action() listeners. The skill builds multi-step workflows using Block Kit&#8217;s section, input, and actions blocks with interactive elements like static_select, multi_external_select, and datepicker components. It chains workflow steps through view_submission handlers that trigger subsequent views or post formatted messages via chat.postMessage with Block Kit attachments. Key features include conversation-scoped data persistence using Bolt&#8217;s built-in context store, scheduled message delivery through chat.scheduleMessage, and threaded conversation management via reply_broadcast. The builder supports Slack Connect for cross-organization workflows, implements app home tabs through app.event(&#8220;app_home_opened&#8221;) with dynamic content, and uses conversations.history for context-aware response generation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-bot-builder/)
