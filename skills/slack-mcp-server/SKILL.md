---
name: Slack MCP Server
description: Agent access to Slack conversations and workspace workflows.
verification: security_reviewed
source: https://github.com/modelcontextprotocol/servers
category:
- Calendar, Email &amp; Productivity
framework:
- Claude Code
- Cursor
- MCP
- OpenClaw
tool_ecosystem:
  github_repo: modelcontextprotocol/servers
  github_stars: 83288
---
# Slack MCP Server

Slack MCP Server is built around Slack messaging and workspace APIs. The underlying ecosystem is represented by slackapi/bolt-js (2,900+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like conversations.history, chat.postMessage, users.info, block kit, files and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to slack so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Agent access to Slack conversations and workspace workflows. The implementation typically relies on conversations.history, chat.postMessage, users.info, block kit, files, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses conversations.history, chat.postMessage, users.info, block kit, files instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as chat triage, digests, alerts, and collaborative automation.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include chat triage, digests, alerts, and collaborative automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-mcp-server/)
