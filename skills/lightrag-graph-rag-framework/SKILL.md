---
name: "LightRAG Graph-Based Retrieval-Augmented Generation Framework"
slug: "lightrag-graph-rag-framework"
description: "LightRAG is a Python-based retrieval-augmented generation framework that builds knowledge graphs from documents for more connected, contextual retrieval. Published at EMNLP 2025, it enables graph-powered RAG with support for multiple storage backends and LLM providers."
github_stars: 33160
verification: "security_reviewed"
source: "https://github.com/HKUDS/LightRAG"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "hkuds/lightrag"
  github_stars: 33160
---

# LightRAG Graph-Based Retrieval-Augmented Generation Framework

LightRAG is a Python-based retrieval-augmented generation framework that builds knowledge graphs from documents for more connected, contextual retrieval. Published at EMNLP 2025, it enables graph-powered RAG with support for multiple storage backends and LLM providers.

## Installation

Use the upstream install or setup path that matches your environment:
- **Note**: You can also use pip if you prefer, but uv is recommended for better performance and more reliable dependency management.
- uv tool install "lightrag-hku[api]"
- git clone https://github.com/HKUDS/LightRAG.git
- make dev

Requirements and caveats from upstream:
- <img src="https://img.shields.io/badge/🐍Python-3.10-4ecdc4?style=for-the-badge&logo=python&logoColor=white&labelColor=1a1a2e">
- [2026.03]🎯[New Feature]: Introduced a setup wizard. Support for local deployment of embedding, reranking, and storage backends via Docker.
- # python -m venv .venv

Basic usage or getting-started notes:
- **📦 Offline Deployment**: For offline or air-gapped environments, see the [Offline Deployment Guide](./docs/OfflineDeployment.md) for instructions on pre-installing all dependencies and cache files.
- The LightRAG Server is designed to provide Web UI and API support. The Web UI facilitates document indexing, knowledge graph exploration, and a simple RAG query interface. LightRAG Server also provide an Ollama compat...
- Install from PyPI

- Source: https://github.com/HKUDS/LightRAG
- Extracted from upstream docs: https://raw.githubusercontent.com/HKUDS/LightRAG/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lightrag-graph-rag-framework/)
