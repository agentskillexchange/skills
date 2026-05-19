---
name: "Build temporal context graphs for agent memory from evolving facts with Graphiti"
slug: "build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti"
description: "Use Graphiti when an agent needs long-term memory that tracks what changed, when it changed, and which source episode produced each fact, instead of storing flat chunks or chat history alone."
github_stars: 24898
verification: "security_reviewed"
source: "https://github.com/getzep/graphiti"
author: "Zep"
publisher_type: "company"
category: "Library & API Reference"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "getzep/graphiti"
  github_stars: 24898
  npm_package: "graphiti-core"
  npm_weekly_downloads: 529336
---

# Build temporal context graphs for agent memory from evolving facts with Graphiti

Use Graphiti when an agent needs long-term memory that tracks what changed, when it changed, and which source episode produced each fact, instead of storing flat chunks or chat history alone.

## Prerequisites

Python environment, Graphiti library, backing graph/database components per Graphiti docs, agent application that can ingest episodes and query memory.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -p 6379:6379 -p 3000:3000 -it --rm falkordb/falkordb:latest
- pip install graphiti-core
- uv add graphiti-core
- pip install graphiti-core[falkordb]

Requirements and caveats from upstream:
- | **Retrieval & performance** | Pre-configured, production-ready retrieval with sub-200ms performance at scale | Custom implementation required; performance depends on your setup |
- | **Developer tools** | Dashboard with graph visualization, debug logs, API logs; SDKs for Python, TypeScript, and Go | Build your own tools |
- Python 3.10 or higher

Basic usage or getting-started notes:
- Neo4j 5.26 / FalkorDB 1.1.2 / Kuzu 0.11.2 / Amazon Neptune Database Cluster or Neptune Analytics Graph + Amazon
- OpenSearch Serverless collection (serves as the full text search backend)
- OpenAI API key (Graphiti defaults to OpenAI for LLM inference and embedding)

- Source: https://github.com/getzep/graphiti
- Extracted from upstream docs: https://raw.githubusercontent.com/getzep/graphiti/HEAD/README.md

## Documentation

- https://help.getzep.com/graphiti

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti/)
