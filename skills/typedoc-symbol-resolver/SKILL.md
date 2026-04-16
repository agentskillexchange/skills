---
title: "TypeDoc Symbol Resolver"
description: "Resolves TypeScript symbols and generates API documentation using the TypeDoc compiler API and ts-morph for AST manipulation. Creates interlinked reference pages with declaration merging support and module augmentation tracking."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/typedoc-symbol-resolver/"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
---

# TypeDoc Symbol Resolver

The TypeDoc Symbol Resolver skill leverages the TypeDoc compiler API and ts-morph library to produce comprehensive TypeScript API reference documentation. It processes tsconfig.json project configurations to resolve all exported symbols, type aliases, interfaces, and class hierarchies.

This skill handles complex TypeScript patterns including declaration merging across multiple files, module augmentation tracking, conditional types, mapped types, and template literal types. It uses TypeDoc’s reflection system to build a complete symbol graph with cross-reference links between related types.

For output generation, the skill creates markdown pages compatible with Docusaurus, VitePress, and Astro Starlight documentation frameworks. Each symbol page includes the full type signature, JSDoc tags, parameter descriptions, return types, and usage examples extracted from @example tags.

Advanced capabilities include re-export chain resolution, barrel file analysis for public API surface detection, generic type parameter documentation, overload signature grouping, and automatic categorization of symbols by module path. The skill also generates a searchable JSON index for integration with Algolia DocSearch.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typedoc-symbol-resolver/)
