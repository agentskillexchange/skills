---
title: "Anthropic SDK Token Usage Logger"
description: "Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient."
slug: "anthropic-sdk-token-usage-logger"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---
# Anthropic SDK Token Usage Logger

Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.

## Installation

Choose the method that fits your setup:
1. Install from the Agent Skill Exchange website
2. Clone or download the upstream source repository
3. Install via npm if the project is published there
4. Use the tool's package manager or release binaries
5. Copy the skill files into your local skills directory manually

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
