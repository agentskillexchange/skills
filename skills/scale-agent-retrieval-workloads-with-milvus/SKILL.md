---
name: "Scale agent retrieval workloads with Milvus"
slug: "scale-agent-retrieval-workloads-with-milvus"
description: "Use Milvus to create vector collections, ingest embeddings, and serve filtered similarity search for RAG and agent retrieval workloads."
github_stars: 44675
verification: "security_reviewed"
source: "https://github.com/milvus-io/milvus"
author: "Milvus"
publisher_type: "open_source_project"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "milvus-io/milvus"
  github_stars: 44675
---

# Scale agent retrieval workloads with Milvus

Use Milvus to create vector collections, ingest embeddings, and serve filtered similarity search for RAG and agent retrieval workloads.

## Prerequisites

Milvus, embedding model, agent or RAG application

## Installation

Use the upstream install or setup path that matches your environment:
- $ pip install -U pymilvus
- CMake: >= 3.26.4 && CMake < 4
- $ git clone https://github.com/milvus-io/milvus.git
- $ make

Requirements and caveats from upstream:
- <a href="https://milvus.io/docs/install_standalone-docker.md"><img src="https://img.shields.io/docker/pulls/milvusdb/milvus" alt="docker-pull-count"/></a>
- python
- This installs pymilvus, the Python SDK for Milvus. Use MilvusClient to create a client:

Basic usage or getting-started notes:
- 🧑‍💻 Written in Go and C++, Milvus implements hardware acceleration for CPU/GPU to achieve best-in-class vector search performance. Thanks to its [fully-distributed and K8s-native architecture](https://milvus.io/docs/o...
- from pymilvus import MilvusClient
- You can also try Milvus Lite for quickstart by installing pymilvus[milvus-lite]. To create a local vector database, simply instantiate a client with a local file name for persisting data:

- Source: https://github.com/milvus-io/milvus
- Extracted from upstream docs: https://raw.githubusercontent.com/milvus-io/milvus/HEAD/README.md

## Documentation

- https://github.com/milvus-io/milvus

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scale-agent-retrieval-workloads-with-milvus/)
