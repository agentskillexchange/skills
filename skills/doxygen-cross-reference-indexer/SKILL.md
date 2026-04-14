---
title: "Doxygen Cross-Reference Indexer"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/doxygen-cross-reference-indexer/)
