---
title: "Jaeger Trace Explorer"
description: "Jaeger Trace Explorer is built around Jaeger distributed tracing platform. The underlying ecosystem is represented by jaegertracing/jaeger (22,608+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like trace search, spans, service graph, latency timelines, baggage, sampling and preserving the operational context that matters for real tasks. In practice, the skill gives an agent a stable interface to jaeger so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on trace search, spans, service graph, latency timelines, baggage, sampling, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform. Accesses trace search, spans, service graph, latency timelines, baggage, sampling instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as APM investigations, request tracing, and microservice diagnostics. Key integration points include APM investigations, request tracing, and microservice diagnostics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations."
source: "https://github.com/jaegertracing/jaeger"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jaegertracing/jaeger"
  github_stars: 22671
---

# Jaeger Trace Explorer

Jaeger Trace Explorer is built around Jaeger distributed tracing platform. The underlying ecosystem is represented by jaegertracing/jaeger (22,608+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like trace search, spans, service graph, latency timelines, baggage, sampling and preserving the operational context that matters for real tasks. In practice, the skill gives an agent a stable interface to jaeger so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on trace search, spans, service graph, latency timelines, baggage, sampling, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform. Accesses trace search, spans, service graph, latency timelines, baggage, sampling instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as APM investigations, request tracing, and microservice diagnostics. Key integration points include APM investigations, request tracing, and microservice diagnostics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jaeger-trace-explorer/)
