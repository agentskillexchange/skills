---
name: "JSDoc Type Definition Extractor"
description: "Extracts and indexes JSDoc type annotations from JavaScript codebases using the jsdoc-api parser. Generates TypeScript declaration files (.d.ts) and searchable type catalogs from @typedef and @param tags."
category: "Library & API Reference"
framework: "MCP-compatible"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jsdoc-type-definition-extractor/"
---

# JSDoc Type Definition Extractor

Extracts and indexes JSDoc type annotations from JavaScript codebases using the jsdoc-api parser. Generates TypeScript declaration files (.d.ts) and searchable type catalogs from @typedef and @param tags.

## Overview

The JSDoc Type Definition Extractor parses JavaScript source files using jsdoc-api to extract type information from JSDoc annotations. It processes @typedef, @param, @returns, @type, @callback, and @template tags to build a comprehensive type catalog. The extractor generates TypeScript declaration files (.d.ts) that provide type safety for JavaScript libraries without requiring a TypeScript migration. It creates searchable HTML documentation using jsdoc-to-markdown templates and supports custom tag definitions for domain-specific annotations. The tool handles complex type expressions including union types, generic type parameters, imported types via @import, and recursive type definitions. It integrates with the TypeScript compiler API to validate extracted types against actual runtime behavior. Incremental parsing tracks file changes and only reprocesses modified sources. The extractor also generates JSON schema representations of extracted types for use in API validation, form generation, and configuration file validation. Cross-reference linking connects related types across files and packages.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jsdoc-type-definition-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jsdoc-type-definition-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jsdoc-type-definition-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jsdoc-type-definition-extractor -a codex
```

### OpenClaw

```bash
clawhub install jsdoc-type-definition-extractor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jsdoc-type-definition-extractor/
