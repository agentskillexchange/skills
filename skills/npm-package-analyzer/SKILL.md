---
title: "NPM Package Analyzer"
description: "Deep analysis of npm packages using npm-registry-fetch and pacote. Evaluates bundle size via bundlephobia API, checks security advisories from npm audit, and maps dependency trees with arborist."
slug: "npm-package-analyzer"
category:
  - "Library &amp; API Reference"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-analyzer/"
---

# NPM Package Analyzer

Deep analysis of npm packages using npm-registry-fetch and pacote. Evaluates bundle size via bundlephobia API, checks security advisories from npm audit, and maps dependency trees with arborist.

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
clawhub install npm-package-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The NPM Package Analyzer provides comprehensive evaluation of npm packages for informed dependency decisions. Using npm-registry-fetch for registry data and pacote for package content inspection, it delivers detailed reports on package health, maintainability, and security posture.
Core analysis includes bundle size estimation via the Bundlephobia API, dependency tree mapping with @npmcli/arborist, download trend analysis from npm stats endpoints, and license compatibility checking across the dependency graph. The agent evaluates package maintenance signals including release frequency, open issue count, and contributor diversity.
Advanced capabilities include security vulnerability scanning through npm audit advisories, duplicate dependency detection across projects, and alternative package suggestions based on functionality overlap. The agent generates migration guides when switching between packages, estimates upgrade effort for major version bumps, and creates lockfile analysis reports. It also supports monorepo workspace analysis and peerDependency conflict resolution.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-analyzer/)
