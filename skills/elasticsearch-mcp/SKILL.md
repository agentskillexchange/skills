---
name: "Elasticsearch MCP"
description: "Elasticsearch MCP is built around Elasticsearch search and analytics engine. The underlying ecosystem is represented by elastic/elasticsearch (76,387+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like Query DSL, aggregations, indices, shards, mappings, cluster health and preserving the […]"
category: "Data Extraction & Transformation"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/elasticsearch-mcp/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "elasticsearch"  # from ase_tool_match
  github_stars: 76393  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1893773  # from ase_npm_downloads
  github_repo: "elastic/elasticsearch"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Elasticsearch MCP

Elasticsearch MCP is built around Elasticsearch search and analytics engine. The underlying ecosystem is represented by elastic/elasticsearch (76,387+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like Query DSL, aggregations, indices, shards, mappings, cluster health and preserving the […]

## Overview

**Elasticsearch MCP** is built around Elasticsearch search and analytics engine. The underlying ecosystem is represented by `elastic/elasticsearch` (76,387+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like Query DSL, aggregations, indices, shards, mappings, cluster health and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to elasticsearch so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on Query DSL, aggregations, indices, shards, mappings, cluster health, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses Query DSL, aggregations, indices, shards, mappings, cluster health instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as full-text search, log analysis, SIEM, and analytics workloads.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include full-text search, log analysis, SIEM, and analytics workloads. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill elasticsearch-mcp
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill elasticsearch-mcp -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill elasticsearch-mcp -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill elasticsearch-mcp -a codex
```

### OpenClaw

```bash
clawhub install elasticsearch-mcp
```

## Source

- Marketplace: https://agentskillexchange.com/skills/elasticsearch-mcp/
