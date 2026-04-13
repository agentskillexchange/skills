---
name: "anthropic-sdk-token-usage-logger"
title: "Anthropic SDK Token Usage Logger"
description: "Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient."
category: "Library & API Reference"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/"
---

# Anthropic SDK Token Usage Logger

Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.

## Installation

You can install this skill using any of these methods:

1. OpenClaw skill installer
2. ClawHub CLI
3. Git clone into your skills directory
4. Download and extract the skill folder manually
5. Copy the skill folder from a local checkout

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
