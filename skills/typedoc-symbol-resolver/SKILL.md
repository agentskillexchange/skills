---
title: "TypeDoc Symbol Resolver"
description: "The TypeDoc Symbol Resolver skill leverages the TypeDoc compiler API and ts-morph library to produce comprehensive TypeScript API reference documentation. It processes tsconfig.json project configurations to resolve all exported symbols, type aliases, interfaces, and class hierarchies. This skill handles complex TypeScript patterns including declaration merging across multiple files, module augmentation tracking, conditional types, mapped types, and template literal types. It uses TypeDoc&#8217;s reflection system to build a complete symbol graph with cross-reference links between related types. For output generation, the skill creates markdown pages compatible with Docusaurus, VitePress, and Astro Starlight documentation frameworks. Each symbol page includes the full type signature, JSDoc tags, parameter descriptions, return types, and usage examples extracted from @example tags. Advanced capabilities include re-export chain resolution, barrel file analysis for public API surface detection, generic type parameter documentation, overload signature grouping, and automatic categorization of symbols by module path. The skill also generates a searchable JSON index for integration with Algolia DocSearch."
source: "https://agentskillexchange.com/skills/typedoc-symbol-resolver/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
---

# TypeDoc Symbol Resolver

The TypeDoc Symbol Resolver skill leverages the TypeDoc compiler API and ts-morph library to produce comprehensive TypeScript API reference documentation. It processes tsconfig.json project configurations to resolve all exported symbols, type aliases, interfaces, and class hierarchies. This skill handles complex TypeScript patterns including declaration merging across multiple files, module augmentation tracking, conditional types, mapped types, and template literal types. It uses TypeDoc&#8217;s reflection system to build a complete symbol graph with cross-reference links between related types. For output generation, the skill creates markdown pages compatible with Docusaurus, VitePress, and Astro Starlight documentation frameworks. Each symbol page includes the full type signature, JSDoc tags, parameter descriptions, return types, and usage examples extracted from @example tags. Advanced capabilities include re-export chain resolution, barrel file analysis for public API surface detection, generic type parameter documentation, overload signature grouping, and automatic categorization of symbols by module path. The skill also generates a searchable JSON index for integration with Algolia DocSearch.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typedoc-symbol-resolver/)
