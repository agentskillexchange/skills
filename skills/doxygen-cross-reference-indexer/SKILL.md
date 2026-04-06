---
name: Doxygen Cross-Reference Indexer
description: Builds searchable cross-reference indexes from Doxygen XML output using
  doxyparse and doxygen-awesome-css themes. Maps function call graphs, inheritance
  hierarchies, and include dependency chains across C/C++ codebases.
category: "Library &amp; API Reference"
framework: ChatGPT Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/doxygen-cross-reference-indexer/"
---
# Doxygen Cross-Reference Indexer

Builds searchable cross-reference indexes from Doxygen XML output using doxyparse and doxygen-awesome-css themes. Maps function call graphs, inheritance hierarchies, and include dependency chains across C/C++ codebases.

The Doxygen Cross-Reference Indexer processes Doxygen XML output to build rich, searchable cross-reference indexes for C and C++ codebases. Using doxyparse for structural analysis, it maps complete function call graphs showing caller-callee relationships across translation units. Inheritance hierarchies are visualized with virtual method override tracking and diamond inheritance detection. Include dependency chains reveal header file relationships and potential circular include issues. The indexer applies doxygen-awesome-css themes for modern, responsive documentation rendering with dark mode support. It generates interactive diagrams using Graphviz dot language with clickable nodes linking to source code. The tool supports incremental indexing where only changed files trigger reprocessing, dramatically reducing build times for large codebases. Custom tag files enable cross-project references where documentation from dependent libraries is linked seamlessly. Search functionality uses a pre-built lunr.js index for instant client-side full-text search across all documented symbols.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill doxygen-cross-reference-indexer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill doxygen-cross-reference-indexer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill doxygen-cross-reference-indexer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill doxygen-cross-reference-indexer -a codex
```

### OpenClaw

```bash
clawhub install doxygen-cross-reference-indexer
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/doxygen-cross-reference-indexer/)
