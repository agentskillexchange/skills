---
name: "Slack Digest and Task Router"
description: "Reads unread Slack messages from specified channels using the conversations.history API, extracts action items and questions, routes tasks to the right person based on mention patterns, and posts a daily digest summary to a designated summary channel via the Slack Web API."
category: "Calendar, Email & Productivity"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/slack-digest-and-task-router/"
---
# Slack Digest and Task Router

Reads unread Slack messages from specified channels using the conversations.history API, extracts action items and questions, routes tasks to the right person based on mention patterns, and posts a daily digest summary to a designated summary channel via the Slack Web API.

## Overview

Reads unread Slack messages from specified channels using the conversations.history API, extracts action items and questions, routes tasks to the right person based on mention patterns, and posts a daily digest summary to a designated summary channel via the Slack Web API.

This skill authenticates with the Slack API using a Bot OAuth token, fetches message history from configured channels within a time window, applies NLP-style extraction to identify action items (messages with ‘please’, ‘can you’, ‘need you to’ patterns plus @mentions), groups by mentioned user, and posts a formatted summary block using Block Kit. Supports DM fallback for high-priority items.

Use for async team communication management, daily standup preparation, and reducing message overload in busy engineering or ops channels. Not for real-time message processing — use Slack Events API with a webhook server for that. Not for private DMs or channels where the bot lacks membership. Requires a Slack Bot token with channels:history, chat:write, and users:read scopes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-digest-and-task-router
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-digest-and-task-router -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-digest-and-task-router -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-digest-and-task-router -a codex
```

### OpenClaw

```bash
clawhub install slack-digest-and-task-router
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-digest-and-task-router/)
