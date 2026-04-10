---
name: Slack Digest and Task Router
description: Reads unread Slack messages from specified channels using the conversations.history
  API, extracts action items and questions, routes tasks to the right person based
  on mention patterns, and posts a daily digest summary to a designated summary channel
  via the Slack Web API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/slack-digest-and-task-router/
category:
- Calendar, Email &amp; Productivity
framework:
- OpenClaw
---
# Slack Digest and Task Router

Reads unread Slack messages from specified channels using the conversations.history API, extracts action items and questions, routes tasks to the right person based on mention patterns, and posts a daily digest summary to a designated summary channel via the Slack Web API.
This skill authenticates with the Slack API using a Bot OAuth token, fetches message history from configured channels within a time window, applies NLP-style extraction to identify action items (messages with &#8216;please', &#8216;can you', &#8216;need you to' patterns plus @mentions), groups by mentioned user, and posts a formatted summary block using Block Kit. Supports DM fallback for high-priority items.
Use for async team communication management, daily standup preparation, and reducing message overload in busy engineering or ops channels. Not for real-time message processing — use Slack Events API with a webhook server for that. Not for private DMs or channels where the bot lacks membership. Requires a Slack Bot token with channels:history, chat:write, and users:read scopes.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-digest-and-task-router/)
