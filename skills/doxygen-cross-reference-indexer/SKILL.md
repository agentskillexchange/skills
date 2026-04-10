---
name: "Doxygen Cross-Reference Indexer"
description: "Builds searchable cross-reference indexes from Doxygen XML output using doxyparse and doxygen-awesome-css themes. Maps function call graphs, inheritance hierarchies, and include dependency chains across C/C++ codebases."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/doxygen-cross-reference-indexer/"
category:
  - "Library &amp; API Reference"
framework:
  - "ChatGPT Agents"
---

# Doxygen Cross-Reference Indexer

The Doxygen Cross-Reference Indexer processes Doxygen XML output to build rich, searchable cross-reference indexes for C and C++ codebases. Using doxyparse for structural analysis, it maps complete function call graphs showing caller-callee relationships across translation units. Inheritance hierarchies are visualized with virtual method override tracking and diamond inheritance detection. Include dependency chains reveal header file relationships and potential circular include issues. The indexer applies doxygen-awesome-css themes for modern, responsive documentation rendering with dark mode support. It generates interactive diagrams using Graphviz dot language with clickable nodes linking to source code. The tool supports incremental indexing where only changed files trigger reprocessing, dramatically reducing build times for large codebases. Custom tag files enable cross-project references where documentation from dependent libraries is linked seamlessly. Search functionality uses a pre-built lunr.js index for instant client-side full-text search across all documented symbols.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/doxygen-cross-reference-indexer/)
