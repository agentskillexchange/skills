---
title: "JSDoc Type Definition Extractor"
description: "The JSDoc Type Definition Extractor parses JavaScript source files using jsdoc-api to extract type information from JSDoc annotations. It processes @typedef, @param, @returns, @type, @callback, and @template tags to build a comprehensive type catalog. The extractor generates TypeScript declaration files (.d.ts) that provide type safety for JavaScript libraries without requiring a TypeScript migration. It creates searchable HTML documentation using jsdoc-to-markdown templates and supports custom tag definitions for domain-specific annotations. The tool handles complex type expressions including union types, generic type parameters, imported types via @import, and recursive type definitions. It integrates with the TypeScript compiler API to validate extracted types against actual runtime behavior. Incremental parsing tracks file changes and only reprocesses modified sources. The extractor also generates JSON schema representations of extracted types for use in API validation, form generation, and configuration file validation. Cross-reference linking connects related types across files and packages."
source: "https://agentskillexchange.com/skills/jsdoc-type-definition-extractor/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
---

# JSDoc Type Definition Extractor

The JSDoc Type Definition Extractor parses JavaScript source files using jsdoc-api to extract type information from JSDoc annotations. It processes @typedef, @param, @returns, @type, @callback, and @template tags to build a comprehensive type catalog. The extractor generates TypeScript declaration files (.d.ts) that provide type safety for JavaScript libraries without requiring a TypeScript migration. It creates searchable HTML documentation using jsdoc-to-markdown templates and supports custom tag definitions for domain-specific annotations. The tool handles complex type expressions including union types, generic type parameters, imported types via @import, and recursive type definitions. It integrates with the TypeScript compiler API to validate extracted types against actual runtime behavior. Incremental parsing tracks file changes and only reprocesses modified sources. The extractor also generates JSON schema representations of extracted types for use in API validation, form generation, and configuration file validation. Cross-reference linking connects related types across files and packages.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jsdoc-type-definition-extractor/)
