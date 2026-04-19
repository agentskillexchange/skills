---
title: "Metrics Dashboard Builder"
description: "Metrics Dashboard Builder is built around Datadog observability platform. The underlying ecosystem is represented by DataDog/dd-trace-js (787+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like metrics API, monitors, logs, dashboards, traces, incidents and preserving the operational context that matters for real tasks. In practice, the skill gives an agent a stable interface to datadog so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on metrics API, monitors, logs, dashboards, traces, incidents, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform. Accesses metrics API, monitors, logs, dashboards, traces, incidents instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as incident response, APM, alerting, and operational dashboards. For generator-style use cases, the skill turns a vague request into repeatable scaffolding with defaults that match the upstream toolchain rather than inventing ad hoc files. Key integration points include incident response, APM, alerting, and operational dashboards. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations."
source: "https://github.com/DataDog/datadog-api-client-typescript"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Agents"
tool_ecosystem:
  npm_package: "@datadog/datadog-api-client"
---

# Metrics Dashboard Builder

Metrics Dashboard Builder is built around Datadog observability platform. The underlying ecosystem is represented by DataDog/dd-trace-js (787+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like metrics API, monitors, logs, dashboards, traces, incidents and preserving the operational context that matters for real tasks. In practice, the skill gives an agent a stable interface to datadog so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on metrics API, monitors, logs, dashboards, traces, incidents, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform. Accesses metrics API, monitors, logs, dashboards, traces, incidents instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as incident response, APM, alerting, and operational dashboards. For generator-style use cases, the skill turns a vague request into repeatable scaffolding with defaults that match the upstream toolchain rather than inventing ad hoc files. Key integration points include incident response, APM, alerting, and operational dashboards. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/metrics-dashboard-builder/)
