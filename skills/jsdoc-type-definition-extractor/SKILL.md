---
title: "JSDoc Type Definition Extractor"
description: "Extracts and indexes JSDoc type annotations from JavaScript codebases using the jsdoc-api parser. Generates TypeScript declaration files (.d.ts) and searchable type catalogs from @typedef and @param tags."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jsdoc-type-definition-extractor/"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
---

# JSDoc Type Definition Extractor

The JSDoc Type Definition Extractor parses JavaScript source files using jsdoc-api to extract type information from JSDoc annotations. It processes @typedef, @param, @returns, @type, @callback, and @template tags to build a comprehensive type catalog. The extractor generates TypeScript declaration files (.d.ts) that provide type safety for JavaScript libraries without requiring a TypeScript migration. It creates searchable HTML documentation using jsdoc-to-markdown templates and supports custom tag definitions for domain-specific annotations. The tool handles complex type expressions including union types, generic type parameters, imported types via @import, and recursive type definitions. It integrates with the TypeScript compiler API to validate extracted types against actual runtime behavior. Incremental parsing tracks file changes and only reprocesses modified sources. The extractor also generates JSON schema representations of extracted types for use in API validation, form generation, and configuration file validation. Cross-reference linking connects related types across files and packages.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jsdoc-type-definition-extractor/)
