---
name: "Run graph and vector memory backends for agents with NornicDB"
slug: "run-graph-and-vector-memory-backends-for-agents-with-nornicdb"
description: "Use NornicDB when an agent workflow needs a local or self-hosted graph, vector, and temporal database for GraphRAG, memory decay, historical reads, and Neo4j/Qdrant-compatible retrieval."
github_stars: 878
verification: "security_reviewed"
source: "https://github.com/orneryd/NornicDB"
author: "orneryd"
publisher_type: "individual"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "orneryd/NornicDB"
  github_stars: 878
---

# Run graph and vector memory backends for agents with NornicDB

Use NornicDB when an agent workflow needs a local or self-hosted graph, vector, and temporal database for GraphRAG, memory decay, historical reads, and Neo4j/Qdrant-compatible retrieval.

## Prerequisites

NornicDB server, Docker or Homebrew, Neo4j/Cypher-compatible client or GraphRAG application code

## Installation

Install or set up from the source-backed instructions:

Install with Homebrew (`brew tap --trust orneryd/nornicdb && brew install nornicdb && brew services start nornicdb`) or run Docker with the upstream CPU or Apple Silicon images, exposing ports 7474 and 7687 and mounting persistent storage.

- Source: https://github.com/orneryd/NornicDB

## Documentation

- https://github.com/orneryd/NornicDB

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-graph-and-vector-memory-backends-for-agents-with-nornicdb/)
