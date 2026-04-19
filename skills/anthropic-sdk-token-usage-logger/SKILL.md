---
title: "Anthropic SDK Token Usage Logger"
description: "This skill wraps the Anthropic TypeScript SDK to provide comprehensive token usage logging and cost tracking for production deployments. It intercepts calls to anthropic.messages.create and anthropic.messages.stream, capturing usage.input_tokens, usage.output_tokens, and cache_creation_input_tokens from the API response object. Request latency is measured with performance.now() and combined with model name, request ID from the x-request-id response header, and estimated cost (calculated from Anthropic&#8217;s published per-token pricing) into a structured log record. Logs are written to AWS CloudWatch Logs using the AWS SDK v3 CloudWatchLogsClient and PutLogEventsCommand with automatic log stream management. The skill also exports metrics to Datadog via DogStatsD: token counts as gauges, latency as a histogram, and cost as a counter tagged by model and environment. Includes a budget alarm that triggers an SNS notification when daily cost exceeds a configurable threshold."
source: "https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---

# Anthropic SDK Token Usage Logger

This skill wraps the Anthropic TypeScript SDK to provide comprehensive token usage logging and cost tracking for production deployments. It intercepts calls to anthropic.messages.create and anthropic.messages.stream, capturing usage.input_tokens, usage.output_tokens, and cache_creation_input_tokens from the API response object. Request latency is measured with performance.now() and combined with model name, request ID from the x-request-id response header, and estimated cost (calculated from Anthropic&#8217;s published per-token pricing) into a structured log record. Logs are written to AWS CloudWatch Logs using the AWS SDK v3 CloudWatchLogsClient and PutLogEventsCommand with automatic log stream management. The skill also exports metrics to Datadog via DogStatsD: token counts as gauges, latency as a histogram, and cost as a counter tagged by model and environment. Includes a budget alarm that triggers an SNS notification when daily cost exceeds a configurable threshold.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
