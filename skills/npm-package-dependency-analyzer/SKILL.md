---
title: "NPM Package Dependency Analyzer"
description: "Analyzes npm package dependency trees using npm-registry-fetch, pacote, and arborist APIs. Detects circular dependencies, license conflicts, and bundle size impacts via bundlephobia API."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-dependency-analyzer/"
category:
  - "Library & API Reference"
framework:
  - "Gemini"
---

# NPM Package Dependency Analyzer

The NPM Package Dependency Analyzer performs deep analysis of Node.js project dependencies using the @npmcli/arborist API for accurate dependency tree resolution and conflict detection. It leverages npm-registry-fetch for querying package metadata, version histories, and download statistics directly from the npm registry. The skill uses pacote for extracting and inspecting package contents without full installation, enabling pre-install security audits. It integrates with the Bundlephobia API to calculate the bundle size impact of each dependency, identifying bloated packages and suggesting lighter alternatives. The analyzer checks all dependencies against the SPDX license database using license-checker to detect incompatible license combinations that could affect distribution. It generates dependency graphs using graphlib, visualizing circular dependencies and identifying opportunities for deduplication. The tool also monitors for deprecated packages and suggests migration paths using npm-check-updates for version range optimization.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/npm-package-dependency-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-package-dependency-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/npm-package-dependency-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-dependency-analyzer/)
