---
title: "TypeDoc Symbol Resolver"
description: "The TypeDoc Symbol Resolver skill leverages the TypeDoc compiler API and ts-morph library to produce comprehensive TypeScript API reference documentation. It processes tsconfig.json project configurations to resolve all exported symbols, type aliases, interfaces, and class hierarchies.\nThis skill handles complex TypeScript patterns including declaration merging across multiple files, module augmentation tracking, conditional types, mapped types, and template literal types. It uses TypeDoc’s reflection system to build a complete symbol graph with cross-reference links between related types.\nFor output generation, the skill creates markdown pages compatible with Docusaurus, VitePress, and Astro Starlight documentation frameworks. Each symbol page includes the full type signature, JSDoc tags, parameter descriptions, return types, and usage examples extracted from @example tags.\nAdvanced capabilities include re-export chain resolution, barrel file analysis for public API surface detection, generic type parameter documentation, overload signature grouping, and automatic categorization of symbols by module path. The skill also generates a searchable JSON index for integration with Algolia DocSearch."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/typedoc-symbol-resolver/"
framework:
  - "Claude Agents"
---

# TypeDoc Symbol Resolver

The TypeDoc Symbol Resolver skill leverages the TypeDoc compiler API and ts-morph library to produce comprehensive TypeScript API reference documentation. It processes tsconfig.json project configurations to resolve all exported symbols, type aliases, interfaces, and class hierarchies.
This skill handles complex TypeScript patterns including declaration merging across multiple files, module augmentation tracking, conditional types, mapped types, and template literal types. It uses TypeDoc’s reflection system to build a complete symbol graph with cross-reference links between related types.
For output generation, the skill creates markdown pages compatible with Docusaurus, VitePress, and Astro Starlight documentation frameworks. Each symbol page includes the full type signature, JSDoc tags, parameter descriptions, return types, and usage examples extracted from @example tags.
Advanced capabilities include re-export chain resolution, barrel file analysis for public API surface detection, generic type parameter documentation, overload signature grouping, and automatic categorization of symbols by module path. The skill also generates a searchable JSON index for integration with Algolia DocSearch.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/typedoc-symbol-resolver
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/typedoc-symbol-resolver` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typedoc-symbol-resolver/)
