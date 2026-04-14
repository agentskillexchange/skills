---
title: "GraphQL Data Federation Agent"
description: "Federates data from multiple GraphQL and REST APIs using Apollo Federation gateway. Implements schema stitching with automatic type merging and the DataLoader pattern for N+1 prevention."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Data Federation Agent

Data federation agent that unifies multiple data sources through a GraphQL gateway. Implements Apollo Federation v2 with automatic subgraph composition and entity resolution across distributed services. Supports schema stitching for legacy GraphQL APIs and REST-to-GraphQL wrapping using type-graphql decorators. Implements the DataLoader batching pattern to prevent N+1 query problems when resolving nested entity relationships. Generates unified schemas from OpenAPI specifications using graphql-mesh transforms. Supports real-time data subscriptions via WebSocket transport with automatic reconnection. Implements query complexity analysis and depth limiting to prevent abusive queries. Includes response caching at the field level using cache-control directives. Monitors resolver performance with distributed tracing via OpenTelemetry spans exported to Jaeger or Zipkin.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-data-federation-agent/)
