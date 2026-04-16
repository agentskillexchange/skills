---
title: "NPM Package Supply Chain Auditor"
description: "Audits npm dependencies for supply chain risks using npm audit, Socket.dev API, and Snyk vulnerability database. Detects typosquatting, install scripts, and maintainer account takeovers."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-supply-chain-auditor/"
category:
  - "Security & Verification"
framework:
  - "OpenClaw"
---

# NPM Package Supply Chain Auditor

This skill performs deep supply chain security analysis on npm packages beyond standard vulnerability scanning. It runs npm audit for known CVEs, then queries the Socket.dev API for behavioral analysis including install script detection, network access patterns, and filesystem operations. The auditor checks for typosquatting by comparing package names against popular packages using Levenshtein distance, flags packages with recent maintainer changes via the npm registry API, and identifies packages that were recently unpublished and re-published (potential takeover indicators). It integrates with the Snyk vulnerability database for comprehensive CVE coverage and checks package provenance using npm attestations. The skill analyzes package-lock.json for dependency confusion risks, verifies that packages resolve to expected registries, and scans for protestware patterns. Reports include risk scores per dependency, SBOM generation in CycloneDX format, and actionable recommendations for pinning, replacing, or removing risky packages.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-supply-chain-auditor/)
