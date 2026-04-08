---
title: GraphQL Schema Stitching & Federation Agent
description: This skill orchestrates Apollo Federation v2 supergraph composition across
  distributed GraphQL subgraph services. It uses the Rover CLI to validate subgraph
  schemas against federation composition rules, checking @key directive definitions,
  entity resolution compatibility, and @shareable field declarations. The agent generates
  supergraph SDL through rover supergraph compose, detecting breaking changes against
  the previous schema version using rover graph check against Apollo Studio. Subgraph
  introspection discovers schemas from running services when SDL files are unavailable.
  The skill handles @override directives for progressive entity migration between
  subgraphs, generating migration plans with rollback steps. Contract schema variants
  filter the supergraph for partner-specific API surfaces using @tag directives. Performance
  analysis identifies N+1 query patterns in entity resolution and recommends @requires
  directive optimizations. The agent produces deployment manifests for Apollo Router
  with configuration for query planning cache sizes, subscription support via WebSocket,
  and rate limiting per operation complexity scores.
verification: security_reviewed
source: https://agentskillexchange.com/skills/graphql-schema-stitching-federation-agent/
category:
- Library &amp; API Reference
framework:
- Claude Code
---

# GraphQL Schema Stitching & Federation Agent

This skill orchestrates Apollo Federation v2 supergraph composition across distributed GraphQL subgraph services. It uses the Rover CLI to validate subgraph schemas against federation composition rules, checking @key directive definitions, entity resolution compatibility, and @shareable field declarations. The agent generates supergraph SDL through rover supergraph compose, detecting breaking changes against the previous schema version using rover graph check against Apollo Studio. Subgraph introspection discovers schemas from running services when SDL files are unavailable. The skill handles @override directives for progressive entity migration between subgraphs, generating migration plans with rollback steps. Contract schema variants filter the supergraph for partner-specific API surfaces using @tag directives. Performance analysis identifies N+1 query patterns in entity resolution and recommends @requires directive optimizations. The agent produces deployment manifests for Apollo Router with configuration for query planning cache sizes, subscription support via WebSocket, and rate limiting per operation complexity scores.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-stitching-federation-agent/)
