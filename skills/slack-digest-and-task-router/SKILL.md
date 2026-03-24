---
name: "Slack Digest and Task Router"
description: "Reads unread Slack messages from specified channels using the conversations.history API, extracts action items and questions, routes tasks to the right person based on mention patterns, and posts a daily digest summary to a designated summary channel via the Slack Web API."
category: "Calendar, Email & Productivity"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/slack-digest-and-task-router/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2900  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/slack-digest-and-task-router/
