---
title: "JSDoc Type Definition Extractor"
description: "Extracts and indexes JSDoc type annotations from JavaScript codebases using the jsdoc-api parser. Generates TypeScript declaration files (.d.ts) and searchable type catalogs from @typedef and @param tags."
slug: "jsdoc-type-definition-extractor"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jsdoc-type-definition-extractor/"
---

# JSDoc Type Definition Extractor

Extracts and indexes JSDoc type annotations from JavaScript codebases using the jsdoc-api parser. Generates TypeScript declaration files (.d.ts) and searchable type catalogs from @typedef and @param tags.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install jsdoc-type-definition-extractor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The JSDoc Type Definition Extractor parses JavaScript source files using jsdoc-api to extract type information from JSDoc annotations. It processes @typedef, @param, @returns, @type, @callback, and @template tags to build a comprehensive type catalog. The extractor generates TypeScript declaration files (.d.ts) that provide type safety for JavaScript libraries without requiring a TypeScript migration. It creates searchable HTML documentation using jsdoc-to-markdown templates and supports custom tag definitions for domain-specific annotations. The tool handles complex type expressions including union types, generic type parameters, imported types via @import, and recursive type definitions. It integrates with the TypeScript compiler API to validate extracted types against actual runtime behavior. Incremental parsing tracks file changes and only reprocesses modified sources. The extractor also generates JSON schema representations of extracted types for use in API validation, form generation, and configuration file validation. Cross-reference linking connects related types across files and packages.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jsdoc-type-definition-extractor/)
