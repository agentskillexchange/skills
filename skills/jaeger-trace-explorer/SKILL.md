---
title: "Jaeger Trace Explorer"
description: "Jaeger Trace Explorer is built around Jaeger distributed tracing platform. The underlying ecosystem is represented by jaegertracing/jaeger (22,608+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like trace search, spans, service graph, latency timelines, baggage, sampling and preserving […]"
verification: "security_reviewed"
source: "https://github.com/jaegertracing/jaeger"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jaegertracing/jaeger"
  github_stars: 22671
---

# Jaeger Trace Explorer

Jaeger Trace Explorer is built around Jaeger distributed tracing platform. The underlying ecosystem is represented by jaegertracing/jaeger (22,608+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like trace search, spans, service graph, latency timelines, baggage, sampling and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to jaeger so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on trace search, spans, service graph, latency timelines, baggage, sampling, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses trace search, spans, service graph, latency timelines, baggage, sampling instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as APM investigations, request tracing, and microservice diagnostics.

Key integration points include APM investigations, request tracing, and microservice diagnostics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jaeger-trace-explorer/)
