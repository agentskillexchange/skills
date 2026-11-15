---
name: "Build edge-to-cloud agent memory with NodeDB"
slug: "build-edge-to-cloud-agent-memory-with-nodedb"
description: "Use NodeDB when an agent system needs one durable, queryable memory store for semantic, graph, document, time-series, and key-value context that can run embedded, offline, or behind a PostgreSQL-compatible server."
github_stars: 201
verification: "security_reviewed"
source: "https://github.com/NodeDB-Lab/nodedb"
author: "NodeDB-Lab"
publisher_type: "source_available"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "NodeDB-Lab/nodedb"
  github_stars: 201
---

# Build edge-to-cloud agent memory with NodeDB

Use NodeDB when an agent system needs one durable, queryable memory store for semantic, graph, document, time-series, and key-value context that can run embedded, offline, or behind a PostgreSQL-compatible server.

## Prerequisites

NodeDB server or Docker image, ndb or psql client, and an agent or application that needs durable memory, RAG, GraphRAG, or retrieval context

## Installation

Install or set up from the source-backed instructions:

Run docker run -d -p 6432:6432 -p 6433:6433 -p 6480:6480 -v nodedb-data:/var/lib/nodedb farhansyah/nodedb:latest, or install from source with cargo install nodedb. Then connect with ndb or psql -h localhost -p 6432 and follow the upstream AI pattern guides for agent memory, RAG, GraphRAG, on-device AI, and evaluation tracking.

- Source: https://github.com/NodeDB-Lab/nodedb

## Documentation

- https://nodedb.dev/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-edge-to-cloud-agent-memory-with-nodedb/)
