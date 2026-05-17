---
name: "Anthropic SDK Token Usage Logger"
slug: "anthropic-sdk-token-usage-logger"
description: "Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient."
github_stars: 1883
verification: "security_reviewed"
source: "https://github.com/anthropics/anthropic-sdk-typescript"
author: "Anthropic"
category: "Library & API Reference"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "anthropics/anthropic-sdk-typescript"
  github_stars: 1883
  npm_package: "@anthropic-ai/sdk"
  npm_weekly_downloads: 14518427
---

# Anthropic SDK Token Usage Logger

Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install @anthropic-ai/sdk
```

## Documentation

- https://platform.claude.com/docs/en/api/sdks/typescript

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
