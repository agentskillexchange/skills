---
name: "NPM Package Dependency Analyzer"
description: "Analyzes npm package dependency trees using npm-registry-fetch, pacote, and arborist APIs. Detects circular dependencies, license conflicts, and bundle size impacts via bundlephobia API."
category: "Library &amp; API Reference"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-dependency-analyzer/"
---
# NPM Package Dependency Analyzer

Analyzes npm package dependency trees using npm-registry-fetch, pacote, and arborist APIs. Detects circular dependencies, license conflicts, and bundle size impacts via bundlephobia API.

The NPM Package Dependency Analyzer performs deep analysis of Node.js project dependencies using the @npmcli/arborist API for accurate dependency tree resolution and conflict detection. It leverages npm-registry-fetch for querying package metadata, version histories, and download statistics directly from the npm registry. The skill uses pacote for extracting and inspecting package contents without full installation, enabling pre-install security audits. It integrates with the Bundlephobia API to calculate the bundle size impact of each dependency, identifying bloated packages and suggesting lighter alternatives. The analyzer checks all dependencies against the SPDX license database using license-checker to detect incompatible license combinations that could affect distribution. It generates dependency graphs using graphlib, visualizing circular dependencies and identifying opportunities for deduplication. The tool also monitors for deprecated packages and suggests migration paths using npm-check-updates for version range optimization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-package-dependency-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-package-dependency-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-package-dependency-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-package-dependency-analyzer -a codex
```

### OpenClaw

```bash
clawhub install npm-package-dependency-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-dependency-analyzer/)
