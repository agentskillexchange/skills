---
title: "Slack Digest and Task Router"
description: "Reads unread Slack messages from specified channels using the conversations.history API, extracts action items and questions, routes tasks to the right person based on mention patterns, and posts a daily digest summary to a designated summary channel via the Slack Web API."
verification: security_reviewed
source: "https://github.com/slackapi/bolt-js"
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

Reads unread Slack messages from specified channels using the conversations.history API, extracts action items and questions, routes tasks to the right person based on mention patterns, and posts a daily digest summary to a designated summary channel via the Slack Web API.

This skill authenticates with the Slack API using a Bot OAuth token, fetches message history from configured channels within a time window, applies NLP-style extraction to identify action items (messages with ‘please’, ‘can you’, ‘need you to’ patterns plus @mentions), groups by mentioned user, and posts a formatted summary block using Block Kit. Supports DM fallback for high-priority items.

Use for async team communication management, daily standup preparation, and reducing message overload in busy engineering or ops channels. Not for real-time message processing — use Slack Events API with a webhook server for that. Not for private DMs or channels where the bot lacks membership. Requires a Slack Bot token with channels:history, chat:write, and users:read scopes.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-digest-and-task-router/)
