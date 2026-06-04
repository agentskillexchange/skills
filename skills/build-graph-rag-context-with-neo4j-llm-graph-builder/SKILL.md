---
name: "Build graph RAG context with Neo4j LLM Graph Builder"
slug: "build-graph-rag-context-with-neo4j-llm-graph-builder"
description: "Convert a bounded document set into a Neo4j knowledge graph, inspect extracted nodes and relationships, and use it for graph-backed RAG."
github_stars: 4733
verification: "security_reviewed"
source: "https://github.com/neo4j-labs/llm-graph-builder"
author: "Neo4j Labs"
publisher_type: "open-source organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "neo4j-labs/llm-graph-builder"
  github_stars: 4733
---

# Build graph RAG context with Neo4j LLM Graph Builder

Convert a bounded document set into a Neo4j knowledge graph, inspect extracted nodes and relationships, and use it for graph-backed RAG.

## Prerequisites

Neo4j Database 5.23 or later with APOC, Python 3.12 backend, configured LLM provider credentials, optional front-end and Docker deployment paths from the upstream README.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install -r requirements.txt -c constraints.txt

Requirements and caveats from upstream:
- ![Python](https://img.shields.io/badge/Python-yellow)
- **Python 3.12 or higher** (for local/separate backend deployment)
- If using **Neo4j Desktop**, you will need to deploy the backend and frontend separately (docker-compose is not supported).

Basic usage or getting-started notes:
- Neo4j Database **5.23 or later** with APOC installed.
- **Neo4j Aura** databases (including the free tier) are supported.
- Create a .env file in the backend folder by copying backend/example.env.

- Source: https://github.com/neo4j-labs/llm-graph-builder
- Extracted from upstream docs: https://raw.githubusercontent.com/neo4j-labs/llm-graph-builder/HEAD/README.md

## Documentation

- https://github.com/neo4j-labs/llm-graph-builder

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-graph-rag-context-with-neo4j-llm-graph-builder/)
