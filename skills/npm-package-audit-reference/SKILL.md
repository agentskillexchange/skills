---
title: "NPM Package Audit Reference"
description: "Provides deep dependency analysis using npm audit, socket.dev API for supply chain risk scoring, and bundlephobia API for bundle size impact assessment. Generates license compliance reports via license-checker."
slug: "npm-package-audit-reference"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-audit-reference/"
listed: true
---

# NPM Package Audit Reference

Provides deep dependency analysis using npm audit, socket.dev API for supply chain risk scoring, and bundlephobia API for bundle size impact assessment. Generates license compliance reports via license-checker.

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
clawhub install npm-package-audit-reference
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The NPM Package Audit Reference skill provides comprehensive Node.js dependency analysis combining security auditing, supply chain risk assessment, and bundle optimization. It runs npm audit with –json output and enriches vulnerability data with CVE details from the National Vulnerability Database API.
The skill integrates with the socket.dev API to assess supply chain risks including typosquatting detection, maintainer account compromise indicators, obfuscated code detection, and install script analysis. Each dependency receives a risk score combining these factors with download velocity anomaly detection.
For frontend projects, the skill queries the bundlephobia API to assess the bundle size impact of each dependency, identifying heavy packages that could be replaced with lighter alternatives. It generates treemap visualizations showing the proportional size contribution of each dependency.
License compliance is handled via license-checker, which scans all transitive dependencies and flags packages with copyleft licenses (GPL, AGPL) that may conflict with proprietary codebases. It generates SBOM (Software Bill of Materials) documents in CycloneDX and SPDX formats.
The skill can also detect duplicate dependencies across the dependency tree using npm dedupe analysis, identify outdated packages with available updates via npm-check-updates, and generate Renovate or Dependabot configuration files for automated dependency management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-audit-reference/)
