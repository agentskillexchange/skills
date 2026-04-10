---
title: "Doxygen Cross-Reference Indexer"
description: "Builds searchable cross-reference indexes from Doxygen XML output using doxyparse and doxygen-awesome-css themes. Maps function call graphs, inheritance hierarchies, and include dependency chains across C/C++ codebases."
slug: "doxygen-cross-reference-indexer"
category:
  - "Library &amp; API Reference"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/doxygen-cross-reference-indexer/"
listed: true
---

# Doxygen Cross-Reference Indexer

Builds searchable cross-reference indexes from Doxygen XML output using doxyparse and doxygen-awesome-css themes. Maps function call graphs, inheritance hierarchies, and include dependency chains across C/C++ codebases.

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
clawhub install doxygen-cross-reference-indexer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Doxygen Cross-Reference Indexer processes Doxygen XML output to build rich, searchable cross-reference indexes for C and C++ codebases. Using doxyparse for structural analysis, it maps complete function call graphs showing caller-callee relationships across translation units. Inheritance hierarchies are visualized with virtual method override tracking and diamond inheritance detection. Include dependency chains reveal header file relationships and potential circular include issues. The indexer applies doxygen-awesome-css themes for modern, responsive documentation rendering with dark mode support. It generates interactive diagrams using Graphviz dot language with clickable nodes linking to source code. The tool supports incremental indexing where only changed files trigger reprocessing, dramatically reducing build times for large codebases. Custom tag files enable cross-project references where documentation from dependent libraries is linked seamlessly. Search functionality uses a pre-built lunr.js index for instant client-side full-text search across all documented symbols.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/doxygen-cross-reference-indexer/)
