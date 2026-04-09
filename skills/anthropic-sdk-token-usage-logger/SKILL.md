---
title: "Anthropic SDK Token Usage Logger"
description: "Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient."
slug: "anthropic-sdk-token-usage-logger"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/"
category:
  - "Library & API Reference"
framework:
  - "Claude Code"
---
# Anthropic SDK Token Usage Logger

Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Add as a local skill folder
3. Install from a Git repository
4. Install via package manager if supported
5. Copy the skill into your OpenClaw skills directory

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
