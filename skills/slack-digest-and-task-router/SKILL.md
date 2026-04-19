---
title: "Slack Digest and Task Router"
description: "Reads unread Slack messages from specified channels using the conversations.history API, extracts action items and questions, routes tasks to the right person based on mention patterns, and posts a daily digest summary to a designated summary channel via the Slack Web API. This skill authenticates with the Slack API using a Bot OAuth token, fetches message history from configured channels within a time window, applies NLP-style extraction to identify action items (messages with &#8216;please&#8217;, &#8216;can you&#8217;, &#8216;need you to&#8217; patterns plus @mentions), groups by mentioned user, and posts a formatted summary block using Block Kit. Supports DM fallback for high-priority items. Use for async team communication management, daily standup preparation, and reducing message overload in busy engineering or ops channels. Not for real-time message processing — use Slack Events API with a webhook server for that. Not for private DMs or channels where the bot lacks membership. Requires a Slack Bot token with channels:history, chat:write, and users:read scopes."
source: "https://github.com/slackapi/bolt-js"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "slackapi/bolt-js"
  github_stars: 2900
  npm_package: "@slack/bolt"
  npm_weekly_downloads: 2603193
---

# Slack Digest and Task Router

Reads unread Slack messages from specified channels using the conversations.history API, extracts action items and questions, routes tasks to the right person based on mention patterns, and posts a daily digest summary to a designated summary channel via the Slack Web API. This skill authenticates with the Slack API using a Bot OAuth token, fetches message history from configured channels within a time window, applies NLP-style extraction to identify action items (messages with &#8216;please&#8217;, &#8216;can you&#8217;, &#8216;need you to&#8217; patterns plus @mentions), groups by mentioned user, and posts a formatted summary block using Block Kit. Supports DM fallback for high-priority items. Use for async team communication management, daily standup preparation, and reducing message overload in busy engineering or ops channels. Not for real-time message processing — use Slack Events API with a webhook server for that. Not for private DMs or channels where the bot lacks membership. Requires a Slack Bot token with channels:history, chat:write, and users:read scopes.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-digest-and-task-router/)
