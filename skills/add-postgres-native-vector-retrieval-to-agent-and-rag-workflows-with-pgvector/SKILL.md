---
title: "Add Postgres-native vector retrieval to agent and RAG workflows with pgvector"
description: "Store embeddings beside application data in Postgres, create vector indexes, and query nearest neighbors for semantic search, RAG, recommendations, or agent memory retrieval."
verification: "security_reviewed"
source: "https://github.com/pgvector/pgvector"
author: "pgvector"
publisher_type: "organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pgvector/pgvector"
  github_stars: 21709
---

# Add Postgres-native vector retrieval to agent and RAG workflows with pgvector

Store embeddings beside application data in Postgres, create vector indexes, and query nearest neighbors for semantic search, RAG, recommendations, or agent memory retrieval.

## Prerequisites

Postgres 13+, pgvector extension, SQL access to the target database, embeddings from the agent or RAG pipeline, and application code that can query Postgres

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install pgvector using the upstream package, source, Docker, Homebrew, PGXN, APT, Yum, or provider-specific path, run `CREATE EXTENSION vector;`, add vector columns and indexes, then query embeddings with the documented distance operators from the agent or RAG application.
```

## Documentation

- https://github.com/pgvector/pgvector#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-postgres-native-vector-retrieval-to-agent-and-rag-workflows-with-pgvector/)
