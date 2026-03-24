---
name: "Jaeger Trace Explorer"
description: "Queries and analyzes distributed traces in Jaeger. Finds slow spans, identifies bottlenecks, compares trace latency distributions, and generates service dependency graphs from trace data."
category: "Monitoring & Alerts"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
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

Queries and analyzes distributed traces in Jaeger. Finds slow spans, identifies bottlenecks, compares trace latency distributions, and generates service dependency graphs from trace data.

## Overview

Queries and analyzes distributed traces in Jaeger. Finds slow spans, identifies bottlenecks, compares trace latency distributions, and generates service dependency graphs from trace data.

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
