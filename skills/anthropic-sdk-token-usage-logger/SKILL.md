---
name: "Anthropic SDK Token Usage Logger"
slug: "anthropic-sdk-token-usage-logger"
description: "Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient."
github_stars: 1883
verification: "listed"
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

Use the upstream install or setup path that matches your environment:
- npm install @anthropic-ai/sdk

Requirements and caveats from upstream:
- Node.js 18+

Basic usage or getting-started notes:
- sh
- js
- import Anthropic from '@anthropic-ai/sdk';

- Source: https://github.com/anthropics/anthropic-sdk-typescript
- Extracted from upstream docs: https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/HEAD/README.md

## Documentation

- https://platform.claude.com/docs/en/api/sdks/typescript

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
