---
name: "Prepare local retrieval embeddings with FastEmbed"
slug: "prepare-local-retrieval-embeddings-with-fastembed"
description: "Generate dense, sparse, image, and reranking embeddings locally before writing vectors into Qdrant or another retrieval stack for agent memory and RAG workflows."
github_stars: 3011
verification: "security_reviewed"
source: "https://github.com/qdrant/fastembed"
author: "Qdrant"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "qdrant/fastembed"
  github_stars: 3011
---

# Prepare local retrieval embeddings with FastEmbed

Generate dense, sparse, image, and reranking embeddings locally before writing vectors into Qdrant or another retrieval stack for agent memory and RAG workflows.

## Prerequisites

Python, FastEmbed, optional qdrant-client and Qdrant vector database

## Installation

Use the upstream install or setup path that matches your environment:
- pip install fastembed
- pip install fastembed-gpu
- pip install qdrant-client[fastembed]
- pip install qdrant-client[fastembed-gpu]

Requirements and caveats from upstream:
- FastEmbed is a lightweight, fast, Python library built for embedding generation. We [support popular text models](https://qdrant.github.io/fastembed/examples/Supported_Models/). Please [open a GitHub issue](https://gi...
- Light: FastEmbed is a lightweight library with few external dependencies. We don't require a GPU and don't download GBs of PyTorch dependencies, and instead use the ONNX Runtime. This makes it a great candidate for se...
- python

Basic usage or getting-started notes:
- The default text embedding (TextEmbedding) model is Flag Embedding, presented in the [MTEB](https://huggingface.co/spaces/mteb/leaderboard) leaderboard. It supports "query" and "passage" prefixes for the input text. H...
- Check our [example](https://qdrant.github.io/fastembed/examples/FastEmbed_GPU/) for detailed instructions, CUDA 12.x support and troubleshooting of the common issues.
- or

- Source: https://github.com/qdrant/fastembed
- Extracted from upstream docs: https://raw.githubusercontent.com/qdrant/fastembed/HEAD/README.md

## Documentation

- https://qdrant.github.io/fastembed/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prepare-local-retrieval-embeddings-with-fastembed/)
