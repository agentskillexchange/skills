---
title: "NPM Package Supply Chain Auditor"
description: "Audits npm dependencies for supply chain risks using npm audit, Socket.dev API, and Snyk vulnerability database. Detects typosquatting, install scripts, and maintainer account takeovers."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-supply-chain-auditor/"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
---

# NPM Package Supply Chain Auditor

This skill performs deep supply chain security analysis on npm packages beyond standard vulnerability scanning. It runs npm audit for known CVEs, then queries the Socket.dev API for behavioral analysis including install script detection, network access patterns, and filesystem operations. The auditor checks for typosquatting by comparing package names against popular packages using Levenshtein distance, flags packages with recent maintainer changes via the npm registry API, and identifies packages that were recently unpublished and re-published (potential takeover indicators). It integrates with the Snyk vulnerability database for comprehensive CVE coverage and checks package provenance using npm attestations. The skill analyzes package-lock.json for dependency confusion risks, verifies that packages resolve to expected registries, and scans for protestware patterns. Reports include risk scores per dependency, SBOM generation in CycloneDX format, and actionable recommendations for pinning, replacing, or removing risky packages.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-supply-chain-auditor/)
