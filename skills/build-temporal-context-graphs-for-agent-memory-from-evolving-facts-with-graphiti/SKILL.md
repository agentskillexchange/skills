---
title: "Build temporal context graphs for agent memory from evolving facts with Graphiti"
description: "Use Graphiti when an agent needs long-term memory that tracks what changed, when it changed, and which source episode produced each fact, instead of storing flat chunks or chat history alone."
verification: "security_reviewed"
source: "https://github.com/getzep/graphiti"
category:
  - "Library & API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "getzep/graphiti"
  github_stars: 24898
  npm_package: "graphiti-core"
  npm_weekly_downloads: 529336
---

# Build temporal context graphs for agent memory from evolving facts with Graphiti

Tool: Graphiti. This skill is for agents that need memory with time awareness, provenance, and graph structure, not just embeddings or raw conversation logs. Graphiti builds a temporal context graph from structured and unstructured inputs, keeps validity windows on facts, and lets the agent query what is true now versus what was true before. When to use it: invoke this when the agent must maintain evolving user, account, policy, or world-state memory across many interactions, especially when older facts can be superseded and still need to remain auditable. It is useful for personalization, longitudinal case tracking, operational state tracking, and any workflow where remembering the latest fact without losing history matters more than generic document retrieval. Using Graphiti is different from using the product normally because the value here is the repeatable operator workflow: ingest episodes, update graph memory incrementally, and query temporally grounded context for downstream agent decisions. Scope boundary: this is not a generic graph database card, a managed memory platform listing, or a broad RAG framework entry. Its boundary is tighter: build and query temporal context graphs for agent memory with provenance and historical fact tracking. If you need a turnkey hosted memory platform, that is a different listing shape. If you need time-aware memory construction and retrieval inside your own agent stack, this is the job.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti/)
