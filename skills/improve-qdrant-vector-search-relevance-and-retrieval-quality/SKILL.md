---
name: "Improve Qdrant vector search relevance and retrieval quality"
slug: "improve-qdrant-vector-search-relevance-and-retrieval-quality"
description: "Use Qdrant's official qdrant-search-quality skill when an agent needs to diagnose weak recall, irrelevant matches, or embedding and chunking mistakes in a live retrieval pipeline. It is a bounded search-quality tuning workflow, not a generic database listing."
verification: "listed"
source: "https://github.com/qdrant/skills/tree/main/skills/qdrant-search-quality"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
---

# Improve Qdrant vector search relevance and retrieval quality

Use Qdrant's official qdrant-search-quality skill when an agent needs to diagnose weak recall, irrelevant matches, or embedding and chunking mistakes in a live retrieval pipeline. It is a bounded search-quality tuning workflow, not a generic database listing.

## Installation

Use the upstream install or setup path that matches your environment:
- npx skills add qdrant/skills

Requirements and caveats from upstream:
- "I have 50M vectors on a single node and search is slow, should I add more nodes?"
- | qdrant-clients-sdk | SDK setup, code examples, snippet search across Python, TypeScript, Rust, Go, .NET, Java |

Basic usage or getting-started notes:
- ### npx skills
- bash
- ### Claude Code

- Source: https://github.com/qdrant/skills/tree/main/skills/qdrant-search-quality
- Extracted from upstream docs: https://raw.githubusercontent.com/qdrant/skills/HEAD/README.md

## Documentation

- https://github.com/qdrant/skills/tree/main/skills/qdrant-search-quality

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/improve-qdrant-vector-search-relevance-and-retrieval-quality/)
