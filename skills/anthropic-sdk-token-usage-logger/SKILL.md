---
title: Anthropic SDK Token Usage Logger
description: 'This skill wraps the Anthropic TypeScript SDK to provide comprehensive
  token usage logging and cost tracking for production deployments. It intercepts
  calls to anthropic.messages.create and anthropic.messages.stream, capturing usage.input_tokens,
  usage.output_tokens, and cache_creation_input_tokens from the API response object.
  Request latency is measured with performance.now() and combined with model name,
  request ID from the x-request-id response header, and estimated cost (calculated
  from Anthropic’s published per-token pricing) into a structured log record. Logs
  are written to AWS CloudWatch Logs using the AWS SDK v3 CloudWatchLogsClient and
  PutLogEventsCommand with automatic log stream management. The skill also exports
  metrics to Datadog via DogStatsD: token counts as gauges, latency as a histogram,
  and cost as a counter tagged by model and environment. Includes a budget alarm that
  triggers an SNS notification when daily cost exceeds a configurable threshold.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/
category:
- Library &amp; API Reference
framework:
- Claude Code
---

# Anthropic SDK Token Usage Logger

This skill wraps the Anthropic TypeScript SDK to provide comprehensive token usage logging and cost tracking for production deployments. It intercepts calls to anthropic.messages.create and anthropic.messages.stream, capturing usage.input_tokens, usage.output_tokens, and cache_creation_input_tokens from the API response object. Request latency is measured with performance.now() and combined with model name, request ID from the x-request-id response header, and estimated cost (calculated from Anthropic’s published per-token pricing) into a structured log record. Logs are written to AWS CloudWatch Logs using the AWS SDK v3 CloudWatchLogsClient and PutLogEventsCommand with automatic log stream management. The skill also exports metrics to Datadog via DogStatsD: token counts as gauges, latency as a histogram, and cost as a counter tagged by model and environment. Includes a budget alarm that triggers an SNS notification when daily cost exceeds a configurable threshold.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
