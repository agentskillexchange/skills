---
name: "Snyk License Compliance Checker"
description: "Uses the Snyk CLI and REST API to audit open-source dependencies for license compliance across npm, PyPI, Maven, and Go modules. Generates SPDX license reports and flags copyleft violations."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/snyk-license-compliance-checker/"
category:
  - "Security &amp; Verification"
framework:
  - "Cursor"
---

# Snyk License Compliance Checker

The Snyk License Compliance Checker skill integrates with the Snyk CLI and REST API to perform comprehensive license auditing across software projects. It analyzes dependency trees for npm, PyPI, Maven, Go modules, and NuGet packages, identifying all transitive dependency licenses.
The skill maintains configurable license allowlists and denylists, flagging copyleft licenses (GPL, AGPL, LGPL) and proprietary-incompatible licenses based on organizational policy. It cross-references licenses against the SPDX License List for standardized identification and generates compliance reports in SPDX and CycloneDX SBOM formats.
Advanced features include dual-license resolution, license exception handling (e.g., Classpath exception for GPL), and risk scoring based on license permissiveness. The skill integrates with legal review workflows, generating approval requests for newly detected license types. It supports policy-as-code via Snyk's org-level settings and can gate pull requests when non-compliant dependencies are introduced.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-license-compliance-checker/)
