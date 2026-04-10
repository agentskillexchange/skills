---
title: "NPM Package Dependency Analyzer"
description: "Analyzes npm package dependency trees using npm-registry-fetch, pacote, and arborist APIs. Detects circular dependencies, license conflicts, and bundle size impacts via bundlephobia API."
slug: "npm-package-dependency-analyzer"
category:
  - "Library &amp; API Reference"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-dependency-analyzer/"
---

# NPM Package Dependency Analyzer

Analyzes npm package dependency trees using npm-registry-fetch, pacote, and arborist APIs. Detects circular dependencies, license conflicts, and bundle size impacts via bundlephobia API.

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
clawhub install npm-package-dependency-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The NPM Package Dependency Analyzer performs deep analysis of Node.js project dependencies using the @npmcli/arborist API for accurate dependency tree resolution and conflict detection. It leverages npm-registry-fetch for querying package metadata, version histories, and download statistics directly from the npm registry. The skill uses pacote for extracting and inspecting package contents without full installation, enabling pre-install security audits. It integrates with the Bundlephobia API to calculate the bundle size impact of each dependency, identifying bloated packages and suggesting lighter alternatives. The analyzer checks all dependencies against the SPDX license database using license-checker to detect incompatible license combinations that could affect distribution. It generates dependency graphs using graphlib, visualizing circular dependencies and identifying opportunities for deduplication. The tool also monitors for deprecated packages and suggests migration paths using npm-check-updates for version range optimization.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-dependency-analyzer/)
