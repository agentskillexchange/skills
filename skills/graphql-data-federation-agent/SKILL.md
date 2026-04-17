---
title: "GraphQL Data Federation Agent"
description: "Data federation agent that unifies multiple data sources through a GraphQL gateway. Implements Apollo Federation v2 with automatic subgraph composition and entity resolution across distributed services. Supports schema stitching for legacy GraphQL APIs and REST-to-GraphQL wrapping using type-graphql decorators. Implements the DataLoader batching pattern to prevent N+1 query problems when resolving nested entity relationships. Generates unified schemas from OpenAPI specifications using graphql-mesh transforms. Supports real-time data subscriptions via WebSocket transport with automatic reconnection. Implements query complexity analysis and depth limiting to prevent abusive queries. Includes response caching at the field level using cache-control directives. Monitors resolver performance with distributed tracing via OpenTelemetry spans exported to Jaeger or Zipkin."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  ase_npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Data Federation Agent

Data federation agent that unifies multiple data sources through a GraphQL gateway. Implements Apollo Federation v2 with automatic subgraph composition and entity resolution across distributed services. Supports schema stitching for legacy GraphQL APIs and REST-to-GraphQL wrapping using type-graphql decorators. Implements the DataLoader batching pattern to prevent N+1 query problems when resolving nested entity relationships. Generates unified schemas from OpenAPI specifications using graphql-mesh transforms. Supports real-time data subscriptions via WebSocket transport with automatic reconnection. Implements query complexity analysis and depth limiting to prevent abusive queries. Includes response caching at the field level using cache-control directives. Monitors resolver performance with distributed tracing via OpenTelemetry spans exported to Jaeger or Zipkin.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/graphql-data-federation-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/graphql-data-federation-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-data-federation-agent/)
