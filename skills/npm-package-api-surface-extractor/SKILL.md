---
title: "NPM Package API Surface Extractor"
description: "The NPM Package API Surface Extractor skill automates the extraction and documentation of public API surfaces from TypeScript and JavaScript NPM packages. It leverages the TypeScript Compiler API (ts.createProgram, ts.createSourceFile) for AST analysis and Microsoft API Extractor (@microsoft/api-extractor) for generating standardized API reports. The skill parses package entry points defined in package.json exports, main, module, and types fields to identify all public API surfaces. Using the TypeScript type checker (ts.TypeChecker), it resolves exported types, interfaces, classes, functions, and constants with their full type signatures, JSDoc comments, and deprecation notices. API Extractor integration produces three key outputs: .api.md files for human-readable API documentation, .d.ts rollup files that bundle all public type declarations, and .api.json files for programmatic API analysis. The skill detects breaking changes by comparing API reports across versions, categorizing changes as major (removed exports, changed signatures), minor (new exports), or patch (documentation updates). It also generates compatibility matrices showing which API features are available across package version ranges."
source: "https://agentskillexchange.com/skills/npm-package-api-surface-extractor/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---

# NPM Package API Surface Extractor

The NPM Package API Surface Extractor skill automates the extraction and documentation of public API surfaces from TypeScript and JavaScript NPM packages. It leverages the TypeScript Compiler API (ts.createProgram, ts.createSourceFile) for AST analysis and Microsoft API Extractor (@microsoft/api-extractor) for generating standardized API reports. The skill parses package entry points defined in package.json exports, main, module, and types fields to identify all public API surfaces. Using the TypeScript type checker (ts.TypeChecker), it resolves exported types, interfaces, classes, functions, and constants with their full type signatures, JSDoc comments, and deprecation notices. API Extractor integration produces three key outputs: .api.md files for human-readable API documentation, .d.ts rollup files that bundle all public type declarations, and .api.json files for programmatic API analysis. The skill detects breaking changes by comparing API reports across versions, categorizing changes as major (removed exports, changed signatures), minor (new exports), or patch (documentation updates). It also generates compatibility matrices showing which API features are available across package version ranges.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-api-surface-extractor/)
