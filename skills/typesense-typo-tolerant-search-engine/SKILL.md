---
name: "Typesense Typo-Tolerant Search Engine"
description: "Typesense is an open-source, typo-tolerant search engine built in C++ for building fast, relevant search experiences. It serves as a self-hostable alternative to Algolia with support for vector search, geo-search, and faceted filtering."
category: "Data Extraction &amp; Transformation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/typesense/typesense"
tool_ecosystem:
  github_repo: "https://github.com/typesense/typesense"
  github_stars: 25500
---
# Typesense Typo-Tolerant Search Engine

Typesense is an open-source, typo-tolerant search engine built in C++ for building fast, relevant search experiences. It serves as a self-hostable alternative to Algolia with support for vector search, geo-search, and faceted filtering.

Typesense is a high-performance, open-source search engine designed from the ground up for speed and developer ergonomics. Written in C++ and distributed as a single binary and Docker image, Typesense delivers sub-50ms search latency even on datasets with tens of millions of documents. With over 25,000 GitHub stars and a GPL-3.0 license, it has become the leading open-source alternative to Algolia and a simpler alternative to Elasticsearch for teams that need fast, typo-tolerant search without operational complexity.

The engine handles typographical errors gracefully out of the box — users can misspell words and still get relevant results without any special configuration. Beyond basic full-text search, Typesense supports faceted navigation with counts, geo-search with distance-based filtering and sorting, vector search for semantic and hybrid retrieval, synonyms, curation and pinning of results, and dynamic sorting. The query language supports filtering, grouping, and multi-field weighted search with fine-grained relevance tuning.

Typesense exposes a RESTful JSON API with official client libraries for JavaScript/TypeScript, Python, Ruby, PHP, Java, Go, C#, Rust, Dart, and Swift. The InstantSearch.js adapter lets you use Algolia’s popular InstantSearch UI components directly with a Typesense backend, making migration from Algolia straightforward. For high availability, Typesense supports Raft-based clustering with automatic leader election and data replication across nodes.

For agent and automation workflows, Typesense provides a powerful indexing and retrieval layer. Agents can use the API to create collections with defined schemas, index documents in real time, and execute complex search queries programmatically. The vector search capability makes Typesense suitable as a lightweight vector store for RAG pipelines, combining keyword and semantic search in a single query. The Docker-based deployment and zero-configuration approach means agents can spin up search infrastructure as part of automated workflows without managing Elasticsearch clusters or paying for hosted search services.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill typesense-typo-tolerant-search-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill typesense-typo-tolerant-search-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill typesense-typo-tolerant-search-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill typesense-typo-tolerant-search-engine -a codex
```

### OpenClaw

```bash
clawhub install typesense-typo-tolerant-search-engine
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typesense-typo-tolerant-search-engine/)
