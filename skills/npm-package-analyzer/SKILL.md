---
title: "NPM Package Analyzer"
description: "The NPM Package Analyzer provides comprehensive evaluation of npm packages for informed dependency decisions. Using npm-registry-fetch for registry data and pacote for package content inspection, it delivers detailed reports on package health, maintainability, and security posture.\nCore analysis includes bundle size estimation via the Bundlephobia API, dependency tree mapping with @npmcli/arborist, download trend analysis from npm stats endpoints, and license compatibility checking across the dependency graph. The agent evaluates package maintenance signals including release frequency, open issue count, and contributor diversity.\nAdvanced capabilities include security vulnerability scanning through npm audit advisories, duplicate dependency detection across projects, and alternative package suggestions based on functionality overlap. The agent generates migration guides when switching between packages, estimates upgrade effort for major version bumps, and creates lockfile analysis reports. It also supports monorepo workspace analysis and peerDependency conflict resolution."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-analyzer/"
framework:
  - "ChatGPT Agents"
---

# NPM Package Analyzer

The NPM Package Analyzer provides comprehensive evaluation of npm packages for informed dependency decisions. Using npm-registry-fetch for registry data and pacote for package content inspection, it delivers detailed reports on package health, maintainability, and security posture.
Core analysis includes bundle size estimation via the Bundlephobia API, dependency tree mapping with @npmcli/arborist, download trend analysis from npm stats endpoints, and license compatibility checking across the dependency graph. The agent evaluates package maintenance signals including release frequency, open issue count, and contributor diversity.
Advanced capabilities include security vulnerability scanning through npm audit advisories, duplicate dependency detection across projects, and alternative package suggestions based on functionality overlap. The agent generates migration guides when switching between packages, estimates upgrade effort for major version bumps, and creates lockfile analysis reports. It also supports monorepo workspace analysis and peerDependency conflict resolution.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-package-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/npm-package-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-analyzer/)
