---
title: "Anthropic SDK Token Usage Logger"
description: "Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient."
verification: "security_reviewed"
source: "https://github.com/anthropics/anthropic-sdk-typescript"
category:
  - "Library & API Reference"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "anthropics/anthropic-sdk-typescript"
  github_stars: 1883
  npm_package: "@anthropic-ai/sdk"
  npm_weekly_downloads: 14518427
---

# Anthropic SDK Token Usage Logger

Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/anthropic-sdk-token-usage-logger
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/anthropic-sdk-token-usage-logger`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
