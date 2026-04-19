---
title: "SBOM Generator with CycloneDX"
description: "The SBOM Generator with CycloneDX skill automates the creation of comprehensive Software Bills of Materials compliant with the CycloneDX 1.5 specification. It orchestrates multiple scanning tools including cdxgen for application dependencies and syft for container image analysis to produce merged, deduplicated SBOMs. The skill enriches raw dependency data by querying clearlydefined.io for authoritative license classifications, resolving ambiguous SPDX expressions, and flagging components with unknown or copyleft licenses that may conflict with your project&#8217;s licensing policy. Vulnerability enrichment queries the OSV.dev API and NVD to attach CVE/GHSA identifiers with CVSS scores and exploitability metrics. For container images, the skill performs layer-by-layer analysis identifying which base image introduced each vulnerable package. It supports all major ecosystems including npm, PyPI, Maven, Go modules, Cargo, and NuGet. Output formats include CycloneDX JSON/XML, SPDX 2.3, and human-readable HTML reports. The skill can also validate existing SBOMs against the NTIA minimum elements checklist and generate VEX (Vulnerability Exploitability eXchange) documents for known false positives."
source: "https://agentskillexchange.com/skills/sbom-generator-cyclonedx/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Gemini"
---

# SBOM Generator with CycloneDX

The SBOM Generator with CycloneDX skill automates the creation of comprehensive Software Bills of Materials compliant with the CycloneDX 1.5 specification. It orchestrates multiple scanning tools including cdxgen for application dependencies and syft for container image analysis to produce merged, deduplicated SBOMs. The skill enriches raw dependency data by querying clearlydefined.io for authoritative license classifications, resolving ambiguous SPDX expressions, and flagging components with unknown or copyleft licenses that may conflict with your project&#8217;s licensing policy. Vulnerability enrichment queries the OSV.dev API and NVD to attach CVE/GHSA identifiers with CVSS scores and exploitability metrics. For container images, the skill performs layer-by-layer analysis identifying which base image introduced each vulnerable package. It supports all major ecosystems including npm, PyPI, Maven, Go modules, Cargo, and NuGet. Output formats include CycloneDX JSON/XML, SPDX 2.3, and human-readable HTML reports. The skill can also validate existing SBOMs against the NTIA minimum elements checklist and generate VEX (Vulnerability Exploitability eXchange) documents for known false positives.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sbom-generator-cyclonedx/)
