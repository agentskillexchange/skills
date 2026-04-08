---
title: Snyk License Compliance Checker
description: The Snyk License Compliance Checker skill integrates with the Snyk CLI
  and REST API to perform comprehensive license auditing across software projects.
  It analyzes dependency trees for npm, PyPI, Maven, Go modules, and NuGet packages,
  identifying all transitive dependency licenses. The skill maintains configurable
  license allowlists and denylists, flagging copyleft licenses (GPL, AGPL, LGPL) and
  proprietary-incompatible licenses based on organizational policy. It cross-references
  licenses against the SPDX License List for standardized identification and generates
  compliance reports in SPDX and CycloneDX SBOM formats. Advanced features include
  dual-license resolution, license exception handling (e.g., Classpath exception for
  GPL), and risk scoring based on license permissiveness. The skill integrates with
  legal review workflows, generating approval requests for newly detected license
  types. It supports policy-as-code via Snyk’s org-level settings and can gate pull
  requests when non-compliant dependencies are introduced.
verification: security_reviewed
source: https://agentskillexchange.com/skills/snyk-license-compliance-checker/
category:
- Security &amp; Verification
framework:
- Cursor
---

# Snyk License Compliance Checker

The Snyk License Compliance Checker skill integrates with the Snyk CLI and REST API to perform comprehensive license auditing across software projects. It analyzes dependency trees for npm, PyPI, Maven, Go modules, and NuGet packages, identifying all transitive dependency licenses. The skill maintains configurable license allowlists and denylists, flagging copyleft licenses (GPL, AGPL, LGPL) and proprietary-incompatible licenses based on organizational policy. It cross-references licenses against the SPDX License List for standardized identification and generates compliance reports in SPDX and CycloneDX SBOM formats. Advanced features include dual-license resolution, license exception handling (e.g., Classpath exception for GPL), and risk scoring based on license permissiveness. The skill integrates with legal review workflows, generating approval requests for newly detected license types. It supports policy-as-code via Snyk’s org-level settings and can gate pull requests when non-compliant dependencies are introduced.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-license-compliance-checker/)
