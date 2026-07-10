---
title: "Generate and evaluate retrieval embeddings with FlagEmbedding"
description: "Use FlagEmbedding to choose BGE embedding or reranking models, encode documents and queries, evaluate retrieval quality, and feed stronger context into RAG workflows."
verification: "security_reviewed"
source: "https://github.com/FlagOpen/FlagEmbedding"
author: "FlagOpen"
publisher_type: "open_source"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "FlagOpen/FlagEmbedding"
  github_stars: 11807
---

# Generate and evaluate retrieval embeddings with FlagEmbedding

Use FlagEmbedding to choose BGE embedding or reranking models, encode documents and queries, evaluate retrieval quality, and feed stronger context into RAG workflows.

## Prerequisites

Python environment, FlagEmbedding package, selected BGE embedding or reranker model, local corpus, query set, and a downstream vector or RAG pipeline.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the FlagEmbedding Python package from the upstream instructions, select the required BGE model, run encoding or reranking on representative documents and queries, then connect the output to the retrieval store or evaluation harness.
```

## Documentation

- https://github.com/FlagOpen/FlagEmbedding

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-and-evaluate-retrieval-embeddings-with-flagembedding/)
