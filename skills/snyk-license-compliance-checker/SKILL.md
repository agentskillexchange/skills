---
name: "Snyk License Compliance Checker"
description: "Uses the Snyk CLI and REST API to audit open-source dependencies for license compliance across npm, PyPI, Maven, and Go modules. Generates SPDX license reports and flags copyleft violations."
category: "Security & Verification"
framework: "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/snyk-license-compliance-checker/"
tool_ecosystem:
  tool: snyk
  github_stars: 5458
  npm_weekly_downloads: 601684
  github_repo: snyk/cli
  maintained: true
---

# Snyk License Compliance Checker

Uses the Snyk CLI and REST API to audit open-source dependencies for license compliance across npm, PyPI, Maven, and Go modules. Generates SPDX license reports and flags copyleft violations.

## Overview

The Snyk License Compliance Checker skill integrates with the **Snyk CLI and REST API** to perform comprehensive license auditing across software projects. It analyzes dependency trees for npm, PyPI, Maven, Go modules, and NuGet packages, identifying all transitive dependency licenses.

The skill maintains configurable license allowlists and denylists, flagging copyleft licenses (GPL, AGPL, LGPL) and proprietary-incompatible licenses based on organizational policy. It cross-references licenses against the SPDX License List for standardized identification and generates compliance reports in SPDX and CycloneDX SBOM formats.

Advanced features include dual-license resolution, license exception handling (e.g., Classpath exception for GPL), and risk scoring based on license permissiveness. The skill integrates with legal review workflows, generating approval requests for newly detected license types. It supports policy-as-code via Snyk’s org-level settings and can gate pull requests when non-compliant dependencies are introduced.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill snyk-license-compliance-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill snyk-license-compliance-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill snyk-license-compliance-checker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill snyk-license-compliance-checker -a codex
```

### OpenClaw

```bash
clawhub install snyk-license-compliance-checker
```

## Source

- Marketplace: https://agentskillexchange.com/skills/snyk-license-compliance-checker/
