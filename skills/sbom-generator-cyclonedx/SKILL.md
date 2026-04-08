---
title: SBOM Generator with CycloneDX
description: The SBOM Generator with CycloneDX skill automates the creation of comprehensive
  Software Bills of Materials compliant with the CycloneDX 1.5 specification. It orchestrates
  multiple scanning tools including cdxgen for application dependencies and syft for
  container image analysis to produce merged, deduplicated SBOMs. The skill enriches
  raw dependency data by querying clearlydefined.io for authoritative license classifications,
  resolving ambiguous SPDX expressions, and flagging components with unknown or copyleft
  licenses that may conflict with your project’s licensing policy. Vulnerability enrichment
  queries the OSV.dev API and NVD to attach CVE/GHSA identifiers with CVSS scores
  and exploitability metrics. For container images, the skill performs layer-by-layer
  analysis identifying which base image introduced each vulnerable package. It supports
  all major ecosystems including npm, PyPI, Maven, Go modules, Cargo, and NuGet. Output
  formats include CycloneDX JSON/XML, SPDX 2.3, and human-readable HTML reports. The
  skill can also validate existing SBOMs against the NTIA minimum elements checklist
  and generate VEX (Vulnerability Exploitability eXchange) documents for known false
  positives.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sbom-generator-cyclonedx/
category:
- Security &amp; Verification
framework:
- Gemini
---

# SBOM Generator with CycloneDX

The SBOM Generator with CycloneDX skill automates the creation of comprehensive Software Bills of Materials compliant with the CycloneDX 1.5 specification. It orchestrates multiple scanning tools including cdxgen for application dependencies and syft for container image analysis to produce merged, deduplicated SBOMs. The skill enriches raw dependency data by querying clearlydefined.io for authoritative license classifications, resolving ambiguous SPDX expressions, and flagging components with unknown or copyleft licenses that may conflict with your project’s licensing policy. Vulnerability enrichment queries the OSV.dev API and NVD to attach CVE/GHSA identifiers with CVSS scores and exploitability metrics. For container images, the skill performs layer-by-layer analysis identifying which base image introduced each vulnerable package. It supports all major ecosystems including npm, PyPI, Maven, Go modules, Cargo, and NuGet. Output formats include CycloneDX JSON/XML, SPDX 2.3, and human-readable HTML reports. The skill can also validate existing SBOMs against the NTIA minimum elements checklist and generate VEX (Vulnerability Exploitability eXchange) documents for known false positives.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sbom-generator-cyclonedx/)
