---
title: "Prepare local retrieval embeddings with FastEmbed"
description: "Generate dense, sparse, image, and reranking embeddings locally before writing vectors into Qdrant or another retrieval stack for agent memory and RAG workflows."
verification: "security_reviewed"
source: "https://github.com/qdrant/fastembed"
author: "Qdrant"
publisher_type: "organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "qdrant/fastembed"
  github_stars: 3011
---

# Prepare local retrieval embeddings with FastEmbed

Generate dense, sparse, image, and reranking embeddings locally before writing vectors into Qdrant or another retrieval stack for agent memory and RAG workflows.

## Prerequisites

Python, FastEmbed, optional qdrant-client and Qdrant vector database

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip install fastembed or pip install fastembed-gpu for GPU support. For Qdrant ingestion, install qdrant-client[fastembed], create embeddings with FastEmbed models, then write vectors and payloads into the retrieval collection.
```

## Documentation

- https://qdrant.github.io/fastembed/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prepare-local-retrieval-embeddings-with-fastembed/)
