---
name: Orama Embeddable Search Engine and RAG Pipeline for JavaScript
description: Orama is a full-text, vector, and hybrid search engine that runs in the
  browser, on a server, or at the edge in under 2KB. It provides built-in RAG pipeline
  support, typo tolerance, faceted search, and language-agnostic stemming — all without
  external dependencies.
verification: security_reviewed
source: https://github.com/oramasearch/orama
category:
- Data Extraction &amp; Transformation
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: oramasearch/orama
  github_stars: 10286
---
# Orama Embeddable Search Engine and RAG Pipeline for JavaScript

Orama is a dependency-free, open-source search engine built in TypeScript that delivers full-text search, vector search, and hybrid search capabilities in a package smaller than 2 kilobytes. Developed by OramaSearch, it runs natively in the browser via WebAssembly, on Node.js servers, and on edge platforms like Cloudflare Workers and Deno Deploy.
Core Capabilities
Orama supports schema-based document indexing with automatic type inference for string, number, boolean, enum, and vector fields. Its search engine provides BM25 ranking, typo tolerance with configurable edit distance, exact match boosting, faceted filtering, geosearch, group-by queries, and custom sorting. The vector search module handles cosine similarity, dot product, and Euclidean distance calculations, enabling semantic search and RAG workflows directly within the same engine.
Agent Integration Points
For AI agents, Orama's primary value lies in its ability to create lightweight, embeddable search indexes that persist across sessions. An agent can build a search index from documentation, codebase files, or structured data, then query it with hybrid search to combine keyword precision with semantic relevance. The built-in RAG pipeline chains retrieval with generation, accepting a custom inference function that can call any LLM provider.
Installation and Usage
Install via npm: npm install @orama/orama. Create a database with create({ schema: { title: 'string', embedding: 'vector[384]' } }), insert documents with insert(db, doc), and search with search(db, { term: 'query', mode: 'hybrid' }). The SDK also ships plugin packages for Astro, Docusaurus, and Vitepress integration.
Platform and Runtime Support
Orama works in all modern browsers, Node.js 16+, Deno, Bun, and Cloudflare Workers. It supports persistence via custom storage adapters, and OramaSearch offers a cloud-hosted version with automatic index synchronization and analytics. The open-source core is licensed under Apache 2.0.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orama-embeddable-search-engine-rag-pipeline/)
