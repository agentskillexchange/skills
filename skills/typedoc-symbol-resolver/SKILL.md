---
title: "TypeDoc Symbol Resolver"
description: "Resolves TypeScript symbols and generates API documentation using the TypeDoc compiler API and ts-morph for AST manipulation. Creates interlinked reference pages with declaration merging support and module augmentation tracking."
verification: "security_reviewed"
source: "https://github.com/TypeStrong/typedoc"
category:
  - "Library & API Reference"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "TypeStrong/typedoc"
  github_stars: 8391
  npm_package: "typedoc"
  npm_weekly_downloads: 4062205
---

# TypeDoc Symbol Resolver

The TypeDoc Symbol Resolver skill leverages the TypeDoc compiler API and ts-morph library to produce comprehensive TypeScript API reference documentation. It processes tsconfig.json project configurations to resolve all exported symbols, type aliases, interfaces, and class hierarchies.

This skill handles complex TypeScript patterns including declaration merging across multiple files, module augmentation tracking, conditional types, mapped types, and template literal types. It uses TypeDoc’s reflection system to build a complete symbol graph with cross-reference links between related types.

For output generation, the skill creates markdown pages compatible with Docusaurus, VitePress, and Astro Starlight documentation frameworks. Each symbol page includes the full type signature, JSDoc tags, parameter descriptions, return types, and usage examples extracted from @example tags.

Advanced capabilities include re-export chain resolution, barrel file analysis for public API surface detection, generic type parameter documentation, overload signature grouping, and automatic categorization of symbols by module path. The skill also generates a searchable JSON index for integration with Algolia DocSearch.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/typedoc-symbol-resolver/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/typedoc-symbol-resolver
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/typedoc-symbol-resolver`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typedoc-symbol-resolver/)
