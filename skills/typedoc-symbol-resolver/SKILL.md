---
title: TypeDoc Symbol Resolver
description: The TypeDoc Symbol Resolver skill leverages the TypeDoc compiler API
  and ts-morph library to produce comprehensive TypeScript API reference documentation.
  It processes tsconfig.json project configurations to resolve all exported symbols,
  type aliases, interfaces, and class hierarchies. This skill handles complex TypeScript
  patterns including declaration merging across multiple files, module augmentation
  tracking, conditional types, mapped types, and template literal types. It uses TypeDoc’s
  reflection system to build a complete symbol graph with cross-reference links between
  related types. For output generation, the skill creates markdown pages compatible
  with Docusaurus, VitePress, and Astro Starlight documentation frameworks. Each symbol
  page includes the full type signature, JSDoc tags, parameter descriptions, return
  types, and usage examples extracted from @example tags. Advanced capabilities include
  re-export chain resolution, barrel file analysis for public API surface detection,
  generic type parameter documentation, overload signature grouping, and automatic
  categorization of symbols by module path. The skill also generates a searchable
  JSON index for integration with Algolia DocSearch.
verification: security_reviewed
source: https://agentskillexchange.com/skills/typedoc-symbol-resolver/
category:
- Library &amp; API Reference
framework:
- Claude Agents
---

# TypeDoc Symbol Resolver

The TypeDoc Symbol Resolver skill leverages the TypeDoc compiler API and ts-morph library to produce comprehensive TypeScript API reference documentation. It processes tsconfig.json project configurations to resolve all exported symbols, type aliases, interfaces, and class hierarchies. This skill handles complex TypeScript patterns including declaration merging across multiple files, module augmentation tracking, conditional types, mapped types, and template literal types. It uses TypeDoc’s reflection system to build a complete symbol graph with cross-reference links between related types. For output generation, the skill creates markdown pages compatible with Docusaurus, VitePress, and Astro Starlight documentation frameworks. Each symbol page includes the full type signature, JSDoc tags, parameter descriptions, return types, and usage examples extracted from @example tags. Advanced capabilities include re-export chain resolution, barrel file analysis for public API surface detection, generic type parameter documentation, overload signature grouping, and automatic categorization of symbols by module path. The skill also generates a searchable JSON index for integration with Algolia DocSearch.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typedoc-symbol-resolver/)
