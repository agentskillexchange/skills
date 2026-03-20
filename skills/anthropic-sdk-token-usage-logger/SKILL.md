---
name: Anthropic SDK Token Usage Logger
description: Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.ou
category: Library & API Reference
framework: Claude Code
verification: verified_metadata
rating: 4.9
reviews: 83
source: https://agentskillexchange.com/skill/anthropic-sdk-token-usage-logger/
---

# Anthropic SDK Token Usage Logger

Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.

## Overview

This skill wraps the Anthropic TypeScript SDK to provide comprehensive token usage logging and cost tracking for production deployments. It intercepts calls to anthropic.messages.create and anthropic.messages.stream, capturing usage.input_tokens, usage.output_tokens, and cache_creation_input_tokens from the API response object. Request latency is measured with performance.now() and combined with model name, request ID from the x-request-id response header, and estimated cost (calculated from Anthropic’s published per-token pricing) into a structured log record. Logs are written to AWS CloudWatch Logs using the AWS SDK v3 CloudWatchLogsClient and PutLogEventsCommand with automatic log stream management. The skill also exports metrics to Datadog via DogStatsD: token counts as gauges, latency as a histogram, and cost as a counter tagged by model and environment. Includes a budget alarm that triggers an SNS notification when daily cost exceeds a configurable threshold.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill anthropic-sdk-token-usage-logger
```

### OpenClaw

```bash
openclaw install anthropic-sdk-token-usage-logger
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Library & API Reference |
| Framework | Claude Code |
| Verification | Verified Metadata |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (83 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/anthropic-sdk-token-usage-logger/)*
