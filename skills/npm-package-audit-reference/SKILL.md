---
title: "NPM Package Audit Reference"
description: "The NPM Package Audit Reference skill provides comprehensive Node.js dependency analysis combining security auditing, supply chain risk assessment, and bundle optimization. It runs npm audit with &#8211;json output and enriches vulnerability data with CVE details from the National Vulnerability Database API. The skill integrates with the socket.dev API to assess supply chain risks including typosquatting detection, maintainer account compromise indicators, obfuscated code detection, and install script analysis. Each dependency receives a risk score combining these factors with download velocity anomaly detection. For frontend projects, the skill queries the bundlephobia API to assess the bundle size impact of each dependency, identifying heavy packages that could be replaced with lighter alternatives. It generates treemap visualizations showing the proportional size contribution of each dependency. License compliance is handled via license-checker, which scans all transitive dependencies and flags packages with copyleft licenses (GPL, AGPL) that may conflict with proprietary codebases. It generates SBOM (Software Bill of Materials) documents in CycloneDX and SPDX formats. The skill can also detect duplicate dependencies across the dependency tree using npm dedupe analysis, identify outdated packages with available updates via npm-check-updates, and generate Renovate or Dependabot configuration files for automated dependency management."
source: "https://agentskillexchange.com/skills/npm-package-audit-reference/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
---

# NPM Package Audit Reference

The NPM Package Audit Reference skill provides comprehensive Node.js dependency analysis combining security auditing, supply chain risk assessment, and bundle optimization. It runs npm audit with &#8211;json output and enriches vulnerability data with CVE details from the National Vulnerability Database API. The skill integrates with the socket.dev API to assess supply chain risks including typosquatting detection, maintainer account compromise indicators, obfuscated code detection, and install script analysis. Each dependency receives a risk score combining these factors with download velocity anomaly detection. For frontend projects, the skill queries the bundlephobia API to assess the bundle size impact of each dependency, identifying heavy packages that could be replaced with lighter alternatives. It generates treemap visualizations showing the proportional size contribution of each dependency. License compliance is handled via license-checker, which scans all transitive dependencies and flags packages with copyleft licenses (GPL, AGPL) that may conflict with proprietary codebases. It generates SBOM (Software Bill of Materials) documents in CycloneDX and SPDX formats. The skill can also detect duplicate dependencies across the dependency tree using npm dedupe analysis, identify outdated packages with available updates via npm-check-updates, and generate Renovate or Dependabot configuration files for automated dependency management.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-audit-reference/)
