---
name: "GraphQL Schema Stitching & Federation Agent"
description: "Manages Apollo Federation v2 supergraph composition from subgraph schemas, validating composition rules and generating rover CLI deployment manifests. Handles @key, @shareable, and @override directives."
category: "Library &amp; API Reference"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
tool_ecosystem:
  tool: graphql
  github_repo: graphql/graphql-js
  github_stars: 20329
  license: MIT
  maintained: true
---
# GraphQL Schema Stitching & Federation Agent

Manages Apollo Federation v2 supergraph composition from subgraph schemas, validating composition rules and generating rover CLI deployment manifests. Handles @key, @shareable, and @override directives.

## Overview

This skill orchestrates Apollo Federation v2 supergraph composition across distributed GraphQL subgraph services. It uses the Rover CLI to validate subgraph schemas against federation composition rules, checking @key directive definitions, entity resolution compatibility, and @shareable field declarations. The agent generates supergraph SDL through rover supergraph compose, detecting breaking changes against the previous schema version using rover graph check against Apollo Studio. Subgraph introspection discovers schemas from running services when SDL files are unavailable. The skill handles @override directives for progressive entity migration between subgraphs, generating migration plans with rollback steps. Contract schema variants filter the supergraph for partner-specific API surfaces using @tag directives. Performance analysis identifies N+1 query patterns in entity resolution and recommends @requires directive optimizations. The agent produces deployment manifests for Apollo Router with configuration for query planning cache sizes, subscription support via WebSocket, and rate limiting per operation complexity scores.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-stitching-federation-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-stitching-federation-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-stitching-federation-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-stitching-federation-agent -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-stitching-federation-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-stitching-federation-agent/)
