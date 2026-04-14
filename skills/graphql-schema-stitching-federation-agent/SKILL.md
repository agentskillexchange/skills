---
title: "GraphQL Schema Stitching & Federation Agent"
description: "Manages Apollo Federation v2 supergraph composition from subgraph schemas, validating composition rules and generating rover CLI deployment manifests. Handles @key, @shareable, and @override directives."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Stitching & Federation Agent

This skill orchestrates Apollo Federation v2 supergraph composition across distributed GraphQL subgraph services. It uses the Rover CLI to validate subgraph schemas against federation composition rules, checking @key directive definitions, entity resolution compatibility, and @shareable field declarations. The agent generates supergraph SDL through rover supergraph compose, detecting breaking changes against the previous schema version using rover graph check against Apollo Studio. Subgraph introspection discovers schemas from running services when SDL files are unavailable. The skill handles @override directives for progressive entity migration between subgraphs, generating migration plans with rollback steps. Contract schema variants filter the supergraph for partner-specific API surfaces using @tag directives. Performance analysis identifies N+1 query patterns in entity resolution and recommends @requires directive optimizations. The agent produces deployment manifests for Apollo Router with configuration for query planning cache sizes, subscription support via WebSocket, and rate limiting per operation complexity scores.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-stitching-federation-agent/)
