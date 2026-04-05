---
name: "NPM Package Analyzer"
description: "Deep analysis of npm packages using npm-registry-fetch and pacote. Evaluates bundle size via bundlephobia API, checks security advisories from npm audit, and maps dependency trees with arborist."
category: "Library &amp; API Reference"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-analyzer/"
---
# NPM Package Analyzer

Deep analysis of npm packages using npm-registry-fetch and pacote. Evaluates bundle size via bundlephobia API, checks security advisories from npm audit, and maps dependency trees with arborist.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-package-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-package-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-package-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-package-analyzer -a codex
```

### OpenClaw

```bash
clawhub install npm-package-analyzer
```

## Details

The NPM Package Analyzer provides comprehensive evaluation of npm packages for informed dependency decisions. Using npm-registry-fetch for registry data and pacote for package content inspection, it delivers detailed reports on package health, maintainability, and security posture.

Core analysis includes bundle size estimation via the Bundlephobia API, dependency tree mapping with @npmcli/arborist, download trend analysis from npm stats endpoints, and license compatibility checking across the dependency graph. The agent evaluates package maintenance signals including release frequency, open issue count, and contributor diversity.

Advanced capabilities include security vulnerability scanning through npm audit advisories, duplicate dependency detection across projects, and alternative package suggestions based on functionality overlap. The agent generates migration guides when switching between packages, estimates upgrade effort for major version bumps, and creates lockfile analysis reports. It also supports monorepo workspace analysis and peerDependency conflict resolution.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-analyzer/)
