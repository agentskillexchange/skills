---
title: "GraphQL Data Federation Agent"
description: "Federates data from multiple GraphQL and REST APIs using Apollo Federation gateway. Implements schema stitching with automatic type merging and the DataLoader pattern for N+1 prevention."
slug: "graphql-data-federation-agent"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/graphql-data-federation-agent/"
---

# GraphQL Data Federation Agent

Federates data from multiple GraphQL and REST APIs using Apollo Federation gateway. Implements schema stitching with automatic type merging and the DataLoader pattern for N+1 prevention.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install graphql-data-federation-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Data federation agent that unifies multiple data sources through a GraphQL gateway. Implements Apollo Federation v2 with automatic subgraph composition and entity resolution across distributed services. Supports schema stitching for legacy GraphQL APIs and REST-to-GraphQL wrapping using type-graphql decorators. Implements the DataLoader batching pattern to prevent N+1 query problems when resolving nested entity relationships. Generates unified schemas from OpenAPI specifications using graphql-mesh transforms. Supports real-time data subscriptions via WebSocket transport with automatic reconnection. Implements query complexity analysis and depth limiting to prevent abusive queries. Includes response caching at the field level using cache-control directives. Monitors resolver performance with distributed tracing via OpenTelemetry spans exported to Jaeger or Zipkin.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-data-federation-agent/)
