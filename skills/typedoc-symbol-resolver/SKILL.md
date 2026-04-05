---
name: "TypeDoc Symbol Resolver"
description: "Resolves TypeScript symbols and generates API documentation using the TypeDoc compiler API and ts-morph for AST manipulation. Creates interlinked reference pages with declaration merging support and module augmentation tracking."
category: "Library & API Reference"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/typedoc-symbol-resolver/"
---
# TypeDoc Symbol Resolver

Resolves TypeScript symbols and generates API documentation using the TypeDoc compiler API and ts-morph for AST manipulation. Creates interlinked reference pages with declaration merging support and module augmentation tracking.

The TypeDoc Symbol Resolver skill leverages the TypeDoc compiler API and ts-morph library to produce comprehensive TypeScript API reference documentation. It processes tsconfig.json project configurations to resolve all exported symbols, type aliases, interfaces, and class hierarchies.



This skill handles complex TypeScript patterns including declaration merging across multiple files, module augmentation tracking, conditional types, mapped types, and template literal types. It uses TypeDoc’s reflection system to build a complete symbol graph with cross-reference links between related types.



For output generation, the skill creates markdown pages compatible with Docusaurus, VitePress, and Astro Starlight documentation frameworks. Each symbol page includes the full type signature, JSDoc tags, parameter descriptions, return types, and usage examples extracted from @example tags.



Advanced capabilities include re-export chain resolution, barrel file analysis for public API surface detection, generic type parameter documentation, overload signature grouping, and automatic categorization of symbols by module path. The skill also generates a searchable JSON index for integration with Algolia DocSearch.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill typedoc-symbol-resolver
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill typedoc-symbol-resolver -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill typedoc-symbol-resolver -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill typedoc-symbol-resolver -a codex
```

### OpenClaw

```bash
clawhub install typedoc-symbol-resolver
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typedoc-symbol-resolver/)
