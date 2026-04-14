---
title: "Anthropic SDK Token Usage Logger"
description: "Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---

# Anthropic SDK Token Usage Logger

This skill wraps the Anthropic TypeScript SDK to provide comprehensive token usage logging and cost tracking for production deployments. It intercepts calls to anthropic.messages.create and anthropic.messages.stream, capturing usage.input_tokens, usage.output_tokens, and cache_creation_input_tokens from the API response object. Request latency is measured with performance.now() and combined with model name, request ID from the x-request-id response header, and estimated cost (calculated from Anthropic’s published per-token pricing) into a structured log record. Logs are written to AWS CloudWatch Logs using the AWS SDK v3 CloudWatchLogsClient and PutLogEventsCommand with automatic log stream management. The skill also exports metrics to Datadog via DogStatsD: token counts as gauges, latency as a histogram, and cost as a counter tagged by model and environment. Includes a budget alarm that triggers an SNS notification when daily cost exceeds a configurable threshold.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
