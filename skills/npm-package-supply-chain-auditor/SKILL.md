---
title: "NPM Package Supply Chain Auditor"
description: "Audits npm dependencies for supply chain risks using npm audit, Socket.dev API, and Snyk vulnerability database. Detects typosquatting, install scripts, and maintainer account takeovers."
slug: "npm-package-supply-chain-auditor"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-supply-chain-auditor/"
listed: true
---

# NPM Package Supply Chain Auditor

Audits npm dependencies for supply chain risks using npm audit, Socket.dev API, and Snyk vulnerability database. Detects typosquatting, install scripts, and maintainer account takeovers.

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
clawhub install npm-package-supply-chain-auditor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill performs deep supply chain security analysis on npm packages beyond standard vulnerability scanning. It runs npm audit for known CVEs, then queries the Socket.dev API for behavioral analysis including install script detection, network access patterns, and filesystem operations. The auditor checks for typosquatting by comparing package names against popular packages using Levenshtein distance, flags packages with recent maintainer changes via the npm registry API, and identifies packages that were recently unpublished and re-published (potential takeover indicators). It integrates with the Snyk vulnerability database for comprehensive CVE coverage and checks package provenance using npm attestations. The skill analyzes package-lock.json for dependency confusion risks, verifies that packages resolve to expected registries, and scans for protestware patterns. Reports include risk scores per dependency, SBOM generation in CycloneDX format, and actionable recommendations for pinning, replacing, or removing risky packages.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-supply-chain-auditor/)
