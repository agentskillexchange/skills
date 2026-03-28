---
name: "GraphQL Data Federation Agent"
description: "Federates data from multiple GraphQL and REST APIs using Apollo Federation gateway. Implements schema stitching with automatic type merging and the DataLoader pattern for N+1 prevention."
category: "Data Extraction & Transformation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
tool_ecosystem:
  tool: graphql
  github_stars: 20332
  npm_weekly_downloads: 32010306
  github_repo: graphql/graphql-js
  license: MIT
  maintained: true
---

# GraphQL Data Federation Agent

Federates data from multiple GraphQL and REST APIs using Apollo Federation gateway. Implements schema stitching with automatic type merging and the DataLoader pattern for N+1 prevention.

## Overview

Data federation agent that unifies multiple data sources through a GraphQL gateway. Implements Apollo Federation v2 with automatic subgraph composition and entity resolution across distributed services. Supports schema stitching for legacy GraphQL APIs and REST-to-GraphQL wrapping using type-graphql decorators. Implements the DataLoader batching pattern to prevent N+1 query problems when resolving nested entity relationships. Generates unified schemas from OpenAPI specifications using graphql-mesh transforms. Supports real-time data subscriptions via WebSocket transport with automatic reconnection. Implements query complexity analysis and depth limiting to prevent abusive queries. Includes response caching at the field level using cache-control directives. Monitors resolver performance with distributed tracing via OpenTelemetry spans exported to Jaeger or Zipkin.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-data-federation-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-data-federation-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-data-federation-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-data-federation-agent -a codex
```

### OpenClaw

```bash
clawhub install graphql-data-federation-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/graphql-data-federation-agent/
