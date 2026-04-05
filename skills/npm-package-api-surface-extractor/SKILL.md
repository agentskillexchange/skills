---
name: "NPM Package API Surface Extractor"
description: "Extracts and documents public API surfaces from NPM packages using TypeScript Compiler API (ts.createProgram) and API Extractor from @microsoft/api-extractor. Generates .api.md report files and .d.ts rollups."
category: "Library &amp; API Reference"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-api-surface-extractor/"
---
# NPM Package API Surface Extractor

Extracts and documents public API surfaces from NPM packages using TypeScript Compiler API (ts.createProgram) and API Extractor from @microsoft/api-extractor. Generates .api.md report files and .d.ts rollups.

The NPM Package API Surface Extractor skill automates the extraction and documentation of public API surfaces from TypeScript and JavaScript NPM packages. It leverages the TypeScript Compiler API (ts.createProgram, ts.createSourceFile) for AST analysis and Microsoft API Extractor (@microsoft/api-extractor) for generating standardized API reports.

The skill parses package entry points defined in package.json exports, main, module, and types fields to identify all public API surfaces. Using the TypeScript type checker (ts.TypeChecker), it resolves exported types, interfaces, classes, functions, and constants with their full type signatures, JSDoc comments, and deprecation notices.

API Extractor integration produces three key outputs: .api.md files for human-readable API documentation, .d.ts rollup files that bundle all public type declarations, and .api.json files for programmatic API analysis. The skill detects breaking changes by comparing API reports across versions, categorizing changes as major (removed exports, changed signatures), minor (new exports), or patch (documentation updates). It also generates compatibility matrices showing which API features are available across package version ranges.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-package-api-surface-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-package-api-surface-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-package-api-surface-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-package-api-surface-extractor -a codex
```

### OpenClaw

```bash
clawhub install npm-package-api-surface-extractor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-api-surface-extractor/)
