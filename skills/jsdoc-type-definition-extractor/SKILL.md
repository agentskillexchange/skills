---
title: "JSDoc Type Definition Extractor"
description: "Extracts and indexes JSDoc type annotations from JavaScript codebases using the jsdoc-api parser. Generates TypeScript declaration files (.d.ts) and searchable type catalogs from @typedef and @param tags."
verification: "security_reviewed"
source: "https://github.com/jsdoc/jsdoc"
category:
  - "Library & API Reference"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jsdoc/jsdoc"
  github_stars: 15436
---

# JSDoc Type Definition Extractor

The JSDoc Type Definition Extractor parses JavaScript source files using jsdoc-api to extract type information from JSDoc annotations. It processes @typedef, @param, @returns, @type, @callback, and @template tags to build a comprehensive type catalog. The extractor generates TypeScript declaration files (.d.ts) that provide type safety for JavaScript libraries without requiring a TypeScript migration. It creates searchable HTML documentation using jsdoc-to-markdown templates and supports custom tag definitions for domain-specific annotations. The tool handles complex type expressions including union types, generic type parameters, imported types via @import, and recursive type definitions. It integrates with the TypeScript compiler API to validate extracted types against actual runtime behavior. Incremental parsing tracks file changes and only reprocesses modified sources. The extractor also generates JSON schema representations of extracted types for use in API validation, form generation, and configuration file validation. Cross-reference linking connects related types across files and packages.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/jsdoc-type-definition-extractor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jsdoc-type-definition-extractor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/jsdoc-type-definition-extractor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jsdoc-type-definition-extractor/)
