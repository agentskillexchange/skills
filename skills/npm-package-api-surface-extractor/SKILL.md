---
title: "NPM Package API Surface Extractor"
description: "Extracts and documents public API surfaces from NPM packages using TypeScript Compiler API (ts.createProgram) and API Extractor from @microsoft/api-extractor. Generates .api.md report files and .d.ts rollups."
verification: "security_reviewed"
source: "https://api-extractor.com/"
category:
  - "Library & API Reference"
framework:
  - "Claude Code"
---

# NPM Package API Surface Extractor

The NPM Package API Surface Extractor skill automates the extraction and documentation of public API surfaces from TypeScript and JavaScript NPM packages. It leverages the TypeScript Compiler API (ts.createProgram, ts.createSourceFile) for AST analysis and Microsoft API Extractor (@microsoft/api-extractor) for generating standardized API reports.

The skill parses package entry points defined in package.json exports, main, module, and types fields to identify all public API surfaces. Using the TypeScript type checker (ts.TypeChecker), it resolves exported types, interfaces, classes, functions, and constants with their full type signatures, JSDoc comments, and deprecation notices.

API Extractor integration produces three key outputs: .api.md files for human-readable API documentation, .d.ts rollup files that bundle all public type declarations, and .api.json files for programmatic API analysis. The skill detects breaking changes by comparing API reports across versions, categorizing changes as major (removed exports, changed signatures), minor (new exports), or patch (documentation updates). It also generates compatibility matrices showing which API features are available across package version ranges.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/npm-package-api-surface-extractor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-package-api-surface-extractor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/npm-package-api-surface-extractor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-api-surface-extractor/)
