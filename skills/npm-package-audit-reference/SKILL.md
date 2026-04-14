---
title: "NPM Package Audit Reference"
description: "Provides deep dependency analysis using npm audit, socket.dev API for supply chain risk scoring, and bundlephobia API for bundle size impact assessment. Generates license compliance reports via license-checker."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-audit-reference/"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
---

# NPM Package Audit Reference

The NPM Package Audit Reference skill provides comprehensive Node.js dependency analysis combining security auditing, supply chain risk assessment, and bundle optimization. It runs npm audit with –json output and enriches vulnerability data with CVE details from the National Vulnerability Database API.

The skill integrates with the socket.dev API to assess supply chain risks including typosquatting detection, maintainer account compromise indicators, obfuscated code detection, and install script analysis. Each dependency receives a risk score combining these factors with download velocity anomaly detection.

For frontend projects, the skill queries the bundlephobia API to assess the bundle size impact of each dependency, identifying heavy packages that could be replaced with lighter alternatives. It generates treemap visualizations showing the proportional size contribution of each dependency.

License compliance is handled via license-checker, which scans all transitive dependencies and flags packages with copyleft licenses (GPL, AGPL) that may conflict with proprietary codebases. It generates SBOM (Software Bill of Materials) documents in CycloneDX and SPDX formats.

The skill can also detect duplicate dependencies across the dependency tree using npm dedupe analysis, identify outdated packages with available updates via npm-check-updates, and generate Renovate or Dependabot configuration files for automated dependency management.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-audit-reference/)
