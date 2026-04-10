---
title: "Snyk License Compliance Checker"
description: "Uses the Snyk CLI and REST API to audit open-source dependencies for license compliance across npm, PyPI, Maven, and Go modules. Generates SPDX license reports and flags copyleft violations."
slug: "snyk-license-compliance-checker"
category:
  - "Security &amp; Verification"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/snyk-license-compliance-checker/"
---

# Snyk License Compliance Checker

Uses the Snyk CLI and REST API to audit open-source dependencies for license compliance across npm, PyPI, Maven, and Go modules. Generates SPDX license reports and flags copyleft violations.

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
clawhub install snyk-license-compliance-checker
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Snyk License Compliance Checker skill integrates with the Snyk CLI and REST API to perform comprehensive license auditing across software projects. It analyzes dependency trees for npm, PyPI, Maven, Go modules, and NuGet packages, identifying all transitive dependency licenses.
The skill maintains configurable license allowlists and denylists, flagging copyleft licenses (GPL, AGPL, LGPL) and proprietary-incompatible licenses based on organizational policy. It cross-references licenses against the SPDX License List for standardized identification and generates compliance reports in SPDX and CycloneDX SBOM formats.
Advanced features include dual-license resolution, license exception handling (e.g., Classpath exception for GPL), and risk scoring based on license permissiveness. The skill integrates with legal review workflows, generating approval requests for newly detected license types. It supports policy-as-code via Snyk’s org-level settings and can gate pull requests when non-compliant dependencies are introduced.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-license-compliance-checker/)
