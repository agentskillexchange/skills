---
title: "NPM Package Supply Chain Auditor"
description: "This skill performs deep supply chain security analysis on npm packages beyond standard vulnerability scanning. It runs npm audit for known CVEs, then queries the Socket.dev API for behavioral analysis including install script detection, network access patterns, and filesystem operations. The auditor checks for typosquatting by comparing package names against popular packages using Levenshtein distance, flags packages with recent maintainer changes via the npm registry API, and identifies packages that were recently unpublished and re-published (potential takeover indicators). It integrates with the Snyk vulnerability database for comprehensive CVE coverage and checks package provenance using npm attestations. The skill analyzes package-lock.json for dependency confusion risks, verifies that packages resolve to expected registries, and scans for protestware patterns. Reports include risk scores per dependency, SBOM generation in CycloneDX format, and actionable recommendations for pinning, replacing, or removing risky packages."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-supply-chain-auditor/"
framework:
  - "OpenClaw"
---

# NPM Package Supply Chain Auditor

This skill performs deep supply chain security analysis on npm packages beyond standard vulnerability scanning. It runs npm audit for known CVEs, then queries the Socket.dev API for behavioral analysis including install script detection, network access patterns, and filesystem operations. The auditor checks for typosquatting by comparing package names against popular packages using Levenshtein distance, flags packages with recent maintainer changes via the npm registry API, and identifies packages that were recently unpublished and re-published (potential takeover indicators). It integrates with the Snyk vulnerability database for comprehensive CVE coverage and checks package provenance using npm attestations. The skill analyzes package-lock.json for dependency confusion risks, verifies that packages resolve to expected registries, and scans for protestware patterns. Reports include risk scores per dependency, SBOM generation in CycloneDX format, and actionable recommendations for pinning, replacing, or removing risky packages.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-package-supply-chain-auditor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/npm-package-supply-chain-auditor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-supply-chain-auditor/)
