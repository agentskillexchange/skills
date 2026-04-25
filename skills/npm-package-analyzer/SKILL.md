---
title: "NPM Package Analyzer"
description: "Deep analysis of npm packages using npm-registry-fetch and pacote. Evaluates bundle size via bundlephobia API, checks security advisories from npm audit, and maps dependency trees with arborist."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-analyzer/"
category:
  - "Library & API Reference"
framework:
  - "ChatGPT Agents"
---

# NPM Package Analyzer

The NPM Package Analyzer provides comprehensive evaluation of npm packages for informed dependency decisions. Using npm-registry-fetch for registry data and pacote for package content inspection, it delivers detailed reports on package health, maintainability, and security posture. Core analysis includes bundle size estimation via the Bundlephobia API, dependency tree mapping with @npmcli/arborist, download trend analysis from npm stats endpoints, and license compatibility checking across the dependency graph. The agent evaluates package maintenance signals including release frequency, open issue count, and contributor diversity. Advanced capabilities include security vulnerability scanning through npm audit advisories, duplicate dependency detection across projects, and alternative package suggestions based on functionality overlap. The agent generates migration guides when switching between packages, estimates upgrade effort for major version bumps, and creates lockfile analysis reports. It also supports monorepo workspace analysis and peerDependency conflict resolution.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/npm-package-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-package-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/npm-package-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-analyzer/)
