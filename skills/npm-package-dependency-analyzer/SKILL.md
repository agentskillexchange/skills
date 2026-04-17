---
title: "NPM Package Dependency Analyzer"
description: "The NPM Package Dependency Analyzer performs deep analysis of Node.js project dependencies using the @npmcli/arborist API for accurate dependency tree resolution and conflict detection. It leverages npm-registry-fetch for querying package metadata, version histories, and download statistics directly from the npm registry. The skill uses pacote for extracting and inspecting package contents without full installation, enabling pre-install security audits. It integrates with the Bundlephobia API to calculate the bundle size impact of each dependency, identifying bloated packages and suggesting lighter alternatives. The analyzer checks all dependencies against the SPDX license database using license-checker to detect incompatible license combinations that could affect distribution. It generates dependency graphs using graphlib, visualizing circular dependencies and identifying opportunities for deduplication. The tool also monitors for deprecated packages and suggests migration paths using npm-check-updates for version range optimization."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-dependency-analyzer/"
framework:
  - "Gemini"
---

# NPM Package Dependency Analyzer

The NPM Package Dependency Analyzer performs deep analysis of Node.js project dependencies using the @npmcli/arborist API for accurate dependency tree resolution and conflict detection. It leverages npm-registry-fetch for querying package metadata, version histories, and download statistics directly from the npm registry. The skill uses pacote for extracting and inspecting package contents without full installation, enabling pre-install security audits. It integrates with the Bundlephobia API to calculate the bundle size impact of each dependency, identifying bloated packages and suggesting lighter alternatives. The analyzer checks all dependencies against the SPDX license database using license-checker to detect incompatible license combinations that could affect distribution. It generates dependency graphs using graphlib, visualizing circular dependencies and identifying opportunities for deduplication. The tool also monitors for deprecated packages and suggests migration paths using npm-check-updates for version range optimization.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-package-dependency-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/npm-package-dependency-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-dependency-analyzer/)
