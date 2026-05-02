---
title: "Doxygen Cross-Reference Indexer"
description: "Builds searchable cross-reference indexes from Doxygen XML output using doxyparse and doxygen-awesome-css themes. Maps function call graphs, inheritance hierarchies, and include dependency chains across C/C++ codebases."
verification: "security_reviewed"
source: "https://github.com/doxygen/doxygen"
category:
  - "Library & API Reference"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "doxygen/doxygen"
  github_stars: 6435
---

# Doxygen Cross-Reference Indexer

The Doxygen Cross-Reference Indexer processes Doxygen XML output to build rich, searchable cross-reference indexes for C and C++ codebases. Using doxyparse for structural analysis, it maps complete function call graphs showing caller-callee relationships across translation units. Inheritance hierarchies are visualized with virtual method override tracking and diamond inheritance detection. Include dependency chains reveal header file relationships and potential circular include issues. The indexer applies doxygen-awesome-css themes for modern, responsive documentation rendering with dark mode support. It generates interactive diagrams using Graphviz dot language with clickable nodes linking to source code. The tool supports incremental indexing where only changed files trigger reprocessing, dramatically reducing build times for large codebases. Custom tag files enable cross-project references where documentation from dependent libraries is linked seamlessly. Search functionality uses a pre-built lunr.js index for instant client-side full-text search across all documented symbols.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/doxygen-cross-reference-indexer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/doxygen-cross-reference-indexer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/doxygen-cross-reference-indexer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/doxygen-cross-reference-indexer/)
