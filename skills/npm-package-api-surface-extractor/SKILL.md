---
title: "NPM Package API Surface Extractor"
description: "Extracts and documents public API surfaces from NPM packages using TypeScript Compiler API (ts.createProgram) and API Extractor from @microsoft/api-extractor. Generates .api.md report files and .d.ts rollups."
slug: "npm-package-api-surface-extractor"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-api-surface-extractor/"
---

# NPM Package API Surface Extractor

Extracts and documents public API surfaces from NPM packages using TypeScript Compiler API (ts.createProgram) and API Extractor from @microsoft/api-extractor. Generates .api.md report files and .d.ts rollups.

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
clawhub install npm-package-api-surface-extractor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The NPM Package API Surface Extractor skill automates the extraction and documentation of public API surfaces from TypeScript and JavaScript NPM packages. It leverages the TypeScript Compiler API (ts.createProgram, ts.createSourceFile) for AST analysis and Microsoft API Extractor (@microsoft/api-extractor) for generating standardized API reports.
The skill parses package entry points defined in package.json exports, main, module, and types fields to identify all public API surfaces. Using the TypeScript type checker (ts.TypeChecker), it resolves exported types, interfaces, classes, functions, and constants with their full type signatures, JSDoc comments, and deprecation notices.
API Extractor integration produces three key outputs: .api.md files for human-readable API documentation, .d.ts rollup files that bundle all public type declarations, and .api.json files for programmatic API analysis. The skill detects breaking changes by comparing API reports across versions, categorizing changes as major (removed exports, changed signatures), minor (new exports), or patch (documentation updates). It also generates compatibility matrices showing which API features are available across package version ranges.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-api-surface-extractor/)
