---
name: "GraphQL Schema Stitching & Federation Agent"
description: "Manages Apollo Federation v2 supergraph composition from subgraph schemas, validating composition rules and generating rover CLI deployment manifests. Handles @key, @shareable, and @override directives."
category: "Library & API Reference"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/graphql-schema-stitching-federation-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20335  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/graphql-schema-stitching-federation-agent/
