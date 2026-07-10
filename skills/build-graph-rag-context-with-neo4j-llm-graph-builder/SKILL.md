---
title: "Build graph RAG context with Neo4j LLM Graph Builder"
description: "Convert a bounded document set into a Neo4j knowledge graph, inspect extracted nodes and relationships, and use it for graph-backed RAG."
verification: "security_reviewed"
source: "https://github.com/neo4j-labs/llm-graph-builder"
author: "Neo4j Labs"
publisher_type: "open-source organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "neo4j-labs/llm-graph-builder"
  github_stars: 4733
---

# Build graph RAG context with Neo4j LLM Graph Builder

Convert a bounded document set into a Neo4j knowledge graph, inspect extracted nodes and relationships, and use it for graph-backed RAG.

## Prerequisites

Neo4j Database 5.23 or later with APOC, Python 3.12 backend, configured LLM provider credentials, optional front-end and Docker deployment paths from the upstream README.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Create backend/.env from backend/example.env and set NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD, and NEO4J_DATABASE. From backend, create a Python 3.12 virtual environment, install requirements with pip install -r requirements.txt -c constraints.txt, then run uvicorn score:app --reload. Follow the README for front-end and Docker-specific deployment paths.
```

## Documentation

- https://github.com/neo4j-labs/llm-graph-builder

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-graph-rag-context-with-neo4j-llm-graph-builder/)
