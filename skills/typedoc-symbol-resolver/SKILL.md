---
name: TypeDoc Symbol Resolver
description: Resolves TypeScript symbols and generates API documentation using the
  TypeDoc compiler API and ts-morph for AST manipulation. Creates interlinked reference
  pages with declaration merging support and module augmentation tracking.
verification: security_reviewed
source: https://agentskillexchange.com/skills/typedoc-symbol-resolver/
category:
- Library &amp; API Reference
framework:
- Claude Agents
---
# TypeDoc Symbol Resolver

The TypeDoc Symbol Resolver skill leverages the TypeDoc compiler API and ts-morph library to produce comprehensive TypeScript API reference documentation. It processes tsconfig.json project configurations to resolve all exported symbols, type aliases, interfaces, and class hierarchies.
This skill handles complex TypeScript patterns including declaration merging across multiple files, module augmentation tracking, conditional types, mapped types, and template literal types. It uses TypeDoc's reflection system to build a complete symbol graph with cross-reference links between related types.
For output generation, the skill creates markdown pages compatible with Docusaurus, VitePress, and Astro Starlight documentation frameworks. Each symbol page includes the full type signature, JSDoc tags, parameter descriptions, return types, and usage examples extracted from @example tags.
Advanced capabilities include re-export chain resolution, barrel file analysis for public API surface detection, generic type parameter documentation, overload signature grouping, and automatic categorization of symbols by module path. The skill also generates a searchable JSON index for integration with Algolia DocSearch.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typedoc-symbol-resolver/)
