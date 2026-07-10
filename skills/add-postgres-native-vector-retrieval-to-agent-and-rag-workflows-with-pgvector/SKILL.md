---
name: "Add Postgres-native vector retrieval to agent and RAG workflows with pgvector"
slug: "add-postgres-native-vector-retrieval-to-agent-and-rag-workflows-with-pgvector"
description: "Store embeddings beside application data in Postgres, create vector indexes, and query nearest neighbors for semantic search, RAG, recommendations, or agent memory retrieval."
github_stars: 21709
verification: "security_reviewed"
source: "https://github.com/pgvector/pgvector"
author: "pgvector"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "pgvector/pgvector"
  github_stars: 21709
---

# Add Postgres-native vector retrieval to agent and RAG workflows with pgvector

Store embeddings beside application data in Postgres, create vector indexes, and query nearest neighbors for semantic search, RAG, recommendations, or agent memory retrieval.

## Prerequisites

Postgres 13+, pgvector extension, SQL access to the target database, embeddings from the agent or RAG pipeline, and application code that can query Postgres

## Installation

Use the upstream install or setup path that matches your environment:
- git clone --branch v0.8.2 https://github.com/pgvector/pgvector.git
- make
- make install # may need sudo
- Then re-run the installation instructions (run make clean before make if needed). If sudo is needed for make install, use:

Requirements and caveats from upstream:
- You can also install it with [Docker](#docker), [Homebrew](#homebrew), [PGXN](#pgxn), [APT](#apt), [Yum](#yum), [pkg](#pkg), [APK](#apk), or [conda-forge](#conda-forge), and it comes preinstalled with [Postgres.app](#...
- You can also install it with [Docker](#docker) or [conda-forge](#conda-forge).
- Or load vectors in bulk using COPY ([example](https://github.com/pgvector/pgvector-python/blob/master/examples/loading/example.py))

Basic usage or getting-started notes:
- Compile and install the extension (supports Postgres 13+)
- cd /tmp
- cd pgvector

- Source: https://github.com/pgvector/pgvector
- Extracted from upstream docs: https://raw.githubusercontent.com/pgvector/pgvector/HEAD/README.md

## Documentation

- https://github.com/pgvector/pgvector#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-postgres-native-vector-retrieval-to-agent-and-rag-workflows-with-pgvector/)
