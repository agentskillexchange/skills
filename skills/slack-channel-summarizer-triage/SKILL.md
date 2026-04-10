---
name: Slack Channel Summarizer &amp; Triage Bot
description: Connects to the Slack Web API to fetch unread messages across specified
  channels and surfaces a prioritized digest of action items, decisions, and blockers.
  Uses conversation.history and users.info endpoints to attribute messages correctly.
  Supports scheduled digests and posts summaries directly to a designated DM or channel.
verification: security_reviewed
source: https://agentskillexchange.com/skills/slack-channel-summarizer-triage/
category:
- Integrations &amp; Connectors
framework:
- OpenClaw
---
# Slack Channel Summarizer & Triage Bot

Slack Channel Summarizer & Triage Bot is built around Slack messaging and workspace APIs. The underlying ecosystem is represented by slackapi/bolt-js (2,900+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like conversations.history, chat.postMessage, users.info, block kit, files and preserving the operational context that matters for real tasks.
For content workflows, the skill uses slack primitives as the system of record, so an agent can read structured inputs, apply transformations, and publish or sync output without losing metadata, IDs, or status fields. The original use case is clear: Connects to the Slack Web API to fetch unread messages across specified channels and surfaces a prioritized digest of action items, decisions, and blockers. Uses conversation.history and users.info endpoints to attribute messages correctly. Supports scheduled digests and posts summaries directly to a designated DM or channel. The implementation typically relies on conversations.history, chat.postMessage, users.info, block kit, files, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses conversations.history, chat.postMessage, users.info, block kit, files instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as chat triage, digests, alerts, and collaborative automation.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include chat triage, digests, alerts, and collaborative automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-channel-summarizer-triage/)
