---
title: NPM Package API Surface Extractor
description: 'The NPM Package API Surface Extractor skill automates the extraction
  and documentation of public API surfaces from TypeScript and JavaScript NPM packages.
  It leverages the TypeScript Compiler API (ts.createProgram, ts.createSourceFile)
  for AST analysis and Microsoft API Extractor (@microsoft/api-extractor) for generating
  standardized API reports. The skill parses package entry points defined in package.json
  exports, main, module, and types fields to identify all public API surfaces. Using
  the TypeScript type checker (ts.TypeChecker), it resolves exported types, interfaces,
  classes, functions, and constants with their full type signatures, JSDoc comments,
  and deprecation notices. API Extractor integration produces three key outputs: .api.md
  files for human-readable API documentation, .d.ts rollup files that bundle all public
  type declarations, and .api.json files for programmatic API analysis. The skill
  detects breaking changes by comparing API reports across versions, categorizing
  changes as major (removed exports, changed signatures), minor (new exports), or
  patch (documentation updates). It also generates compatibility matrices showing
  which API features are available across package version ranges.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/npm-package-api-surface-extractor/
category:
- Library &amp; API Reference
framework:
- Claude Code
---

# NPM Package API Surface Extractor

The NPM Package API Surface Extractor skill automates the extraction and documentation of public API surfaces from TypeScript and JavaScript NPM packages. It leverages the TypeScript Compiler API (ts.createProgram, ts.createSourceFile) for AST analysis and Microsoft API Extractor (@microsoft/api-extractor) for generating standardized API reports. The skill parses package entry points defined in package.json exports, main, module, and types fields to identify all public API surfaces. Using the TypeScript type checker (ts.TypeChecker), it resolves exported types, interfaces, classes, functions, and constants with their full type signatures, JSDoc comments, and deprecation notices. API Extractor integration produces three key outputs: .api.md files for human-readable API documentation, .d.ts rollup files that bundle all public type declarations, and .api.json files for programmatic API analysis. The skill detects breaking changes by comparing API reports across versions, categorizing changes as major (removed exports, changed signatures), minor (new exports), or patch (documentation updates). It also generates compatibility matrices showing which API features are available across package version ranges.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-api-surface-extractor/)
