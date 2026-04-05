---
name: "NPM Package Supply Chain Auditor"
description: "Audits npm dependencies for supply chain risks using npm audit, Socket.dev API, and Snyk vulnerability database. Detects typosquatting, install scripts, and maintainer account takeovers."
category: "Security &amp; Verification"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-supply-chain-auditor/"
---
# NPM Package Supply Chain Auditor

Audits npm dependencies for supply chain risks using npm audit, Socket.dev API, and Snyk vulnerability database. Detects typosquatting, install scripts, and maintainer account takeovers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-package-supply-chain-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-package-supply-chain-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-package-supply-chain-auditor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-package-supply-chain-auditor -a codex
```

### OpenClaw

```bash
clawhub install npm-package-supply-chain-auditor
```

## Details

This skill performs deep supply chain security analysis on npm packages beyond standard vulnerability scanning. It runs npm audit for known CVEs, then queries the Socket.dev API for behavioral analysis including install script detection, network access patterns, and filesystem operations. The auditor checks for typosquatting by comparing package names against popular packages using Levenshtein distance, flags packages with recent maintainer changes via the npm registry API, and identifies packages that were recently unpublished and re-published (potential takeover indicators). It integrates with the Snyk vulnerability database for comprehensive CVE coverage and checks package provenance using npm attestations. The skill analyzes package-lock.json for dependency confusion risks, verifies that packages resolve to expected registries, and scans for protestware patterns. Reports include risk scores per dependency, SBOM generation in CycloneDX format, and actionable recommendations for pinning, replacing, or removing risky packages.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-supply-chain-auditor/)
