---
name: Slack Workflow Bot
description: Builds interactive Slack workflows using the Bolt SDK for JavaScript
  and Block Kit Builder API. Handles modal forms, scheduled messages, and webhook
  integrations.
category: "Calendar, Email &amp; Productivity"
framework: MCP
verification: security_reviewed
source: "https://agentskillexchange.com/skills/slack-workflow-bot-bolt-sdk/"
---
# Slack Workflow Bot

Builds interactive Slack workflows using the Bolt SDK for JavaScript and Block Kit Builder API. Handles modal forms, scheduled messages, and webhook integrations.

Slack Workflow Bot uses the Bolt SDK for JavaScript to create interactive workflow automations within Slack workspaces. It constructs rich Block Kit interfaces for approval flows, form submissions, and interactive polls using the Block Kit Builder API. The bot handles OAuth 2.0 installation flows for multi-workspace distribution, manages Socket Mode connections for development environments, and supports Slack Event API subscriptions for real-time message processing. Scheduled message delivery uses the chat.scheduleMessage API with timezone-aware scheduling. Integration with Slack Workflow Builder enables custom steps that connect to external APIs. The tool implements conversation store patterns for multi-turn interactions, handles rate limiting with exponential backoff, and supports Slack Enterprise Grid organization-level deployments. Audit logging tracks all workflow executions for compliance.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-bot-bolt-sdk
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-bot-bolt-sdk -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-bot-bolt-sdk -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-workflow-bot-bolt-sdk -a codex
```

### OpenClaw

```bash
clawhub install slack-workflow-bot-bolt-sdk
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-workflow-bot-bolt-sdk/)
