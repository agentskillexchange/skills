---
name: Anthropic SDK Token Usage Logger
description: Instruments Anthropic API calls to log token usage, latency, and cost
  per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create
  method to capture usage.input_tokens, usage.output_tokens, and timing from the API
  response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.
category: Library & API Reference
framework: Claude Code
verification: security_reviewed
source: https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/
---
# Anthropic SDK Token Usage Logger
Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/anthropic-sdk-token-usage-logger
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/anthropic-sdk-token-usage-logger` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
