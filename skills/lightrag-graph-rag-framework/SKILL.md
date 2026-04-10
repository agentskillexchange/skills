---
title: "LightRAG Graph-Based Retrieval-Augmented Generation Framework"
description: "LightRAG is a Python-based retrieval-augmented generation framework that builds knowledge graphs from documents for more connected, contextual retrieval. Published at EMNLP 2025, it enables graph-powered RAG with support for multiple storage backends and LLM providers."
slug: "lightrag-graph-rag-framework"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/HKUDS/LightRAG"
listed: true
---

# LightRAG Graph-Based Retrieval-Augmented Generation Framework

LightRAG is a Python-based retrieval-augmented generation framework that builds knowledge graphs from documents for more connected, contextual retrieval. Published at EMNLP 2025, it enables graph-powered RAG with support for multiple storage backends and LLM providers.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install lightrag-graph-rag-framework
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

LightRAG is an open-source Python framework for retrieval-augmented generation (RAG) that uses knowledge graphs to enable more connected and contextual information retrieval. Developed by the HKUDS research group at the University of Hong Kong, it was published at EMNLP 2025 and has rapidly gained adoption with over 32,000 GitHub stars.
How It Works
Unlike traditional RAG systems that chunk documents and retrieve by vector similarity alone, LightRAG extracts entities and relationships from your documents to build a knowledge graph. When you query, it uses both vector similarity and graph traversal to find relevant information, producing more coherent and connected answers that span multiple documents.
Key Features
- Graph-based RAG: Builds knowledge graphs from documents using entity recognition and relation extraction for fine-grained, domain-specific retrieval.
- Multiple query modes: Supports naive, local, global, hybrid, and mixed query modes with reranker support for optimal results.
- Flexible storage backends: Works with Neo4J, PostgreSQL, MongoDB, OpenSearch, and built-in storage for both vector and graph data.
- LLM provider agnostic: Compatible with OpenAI, Anthropic, local models via Ollama, and other providers.
- REST API server: Includes a built-in API server for document insertion and querying, plus a WebUI for visualization.
- Multimodal support: Handles text, images, tables, and equations through RAG-Anything integration.
- Citation support: Enables proper source attribution and document traceability.
- Evaluation and tracing: Integrated RAGAS for evaluation and Langfuse for observability tracing.
Installation
pip install lightrag-hku
Integration with AI Agents
LightRAG can serve as the knowledge retrieval backbone for AI coding agents and assistants. Its REST API makes it straightforward to integrate into agent workflows — insert documents during setup, then query during task execution. The knowledge graph approach is particularly valuable for codebases and technical documentation where entities (functions, classes, APIs) have rich relationships that flat vector search misses.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lightrag-graph-rag-framework/)
