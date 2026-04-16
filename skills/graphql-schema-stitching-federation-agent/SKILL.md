---
title: "GraphQL Schema Stitching & Federation Agent"
description: "Manages Apollo Federation v2 supergraph composition from subgraph schemas, validating composition rules and generating rover CLI deployment manifests. Handles @key, @shareable, and @override directives."
verification: "security_reviewed"
source: "https://github.com/graphql/graphql-js"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  ase_npm_package: "graphql"
  npm_weekly_downloads: 34200861
  license: "MIT"
---

# GraphQL Schema Stitching & Federation Agent

This skill orchestrates Apollo Federation v2 supergraph composition across distributed GraphQL subgraph services. It uses the Rover CLI to validate subgraph schemas against federation composition rules, checking @key directive definitions, entity resolution compatibility, and @shareable field declarations. The agent generates supergraph SDL through rover supergraph compose, detecting breaking changes against the previous schema version using rover graph check against Apollo Studio. Subgraph introspection discovers schemas from running services when SDL files are unavailable. The skill handles @override directives for progressive entity migration between subgraphs, generating migration plans with rollback steps. Contract schema variants filter the supergraph for partner-specific API surfaces using @tag directives. Performance analysis identifies N+1 query patterns in entity resolution and recommends @requires directive optimizations. The agent produces deployment manifests for Apollo Router with configuration for query planning cache sizes, subscription support via WebSocket, and rate limiting per operation complexity scores.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-stitching-federation-agent/)
