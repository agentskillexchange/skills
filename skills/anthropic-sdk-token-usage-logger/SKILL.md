---
title: "Anthropic SDK Token Usage Logger"
description: "Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient."
slug: "anthropic-sdk-token-usage-logger"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/"
---

# Anthropic SDK Token Usage Logger

Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install anthropic-sdk-token-usage-logger
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill wraps the Anthropic TypeScript SDK to provide comprehensive token usage logging and cost tracking for production deployments. It intercepts calls to anthropic.messages.create and anthropic.messages.stream, capturing usage.input_tokens, usage.output_tokens, and cache_creation_input_tokens from the API response object. Request latency is measured with performance.now() and combined with model name, request ID from the x-request-id response header, and estimated cost (calculated from Anthropic’s published per-token pricing) into a structured log record. Logs are written to AWS CloudWatch Logs using the AWS SDK v3 CloudWatchLogsClient and PutLogEventsCommand with automatic log stream management. The skill also exports metrics to Datadog via DogStatsD: token counts as gauges, latency as a histogram, and cost as a counter tagged by model and environment. Includes a budget alarm that triggers an SNS notification when daily cost exceeds a configurable threshold.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
