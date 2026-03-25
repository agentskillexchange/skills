---
name: "Jaeger Trace Explorer"
description: "Jaeger Trace Explorer is built around Jaeger distributed tracing platform. The underlying ecosystem is represented by jaegertracing/jaeger (22,608+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like trace search, spans, service graph, latency timelines, baggage, sampling and preserving […]"
category: "Monitoring & Alerts"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jaeger-trace-explorer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jaeger"  # from ase_tool_match
  github_stars: 22608  # from ase_github_stars (integer, not string)
  github_repo: "jaegertracing/jaeger"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Jaeger Trace Explorer

Jaeger Trace Explorer is built around Jaeger distributed tracing platform. The underlying ecosystem is represented by jaegertracing/jaeger (22,608+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like trace search, spans, service graph, latency timelines, baggage, sampling and preserving […]

## Overview

**Jaeger Trace Explorer** is built around Jaeger distributed tracing platform. The underlying ecosystem is represented by `jaegertracing/jaeger` (22,608+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like trace search, spans, service graph, latency timelines, baggage, sampling and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to jaeger so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on trace search, spans, service graph, latency timelines, baggage, sampling, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses trace search, spans, service graph, latency timelines, baggage, sampling instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as APM investigations, request tracing, and microservice diagnostics.

Key integration points include APM investigations, request tracing, and microservice diagnostics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jaeger-trace-explorer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jaeger-trace-explorer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jaeger-trace-explorer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jaeger-trace-explorer -a codex
```

### OpenClaw

```bash
clawhub install jaeger-trace-explorer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jaeger-trace-explorer/
