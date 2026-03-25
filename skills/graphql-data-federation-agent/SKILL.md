---
name: "GraphQL Data Federation Agent"
description: "Federates data from multiple GraphQL and REST APIs using Apollo Federation gateway. Implements schema stitching with automatic type merging and the DataLoader pattern for N+1 prevention."
category: "Data Extraction & Transformation"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/graphql-data-federation-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20335  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
