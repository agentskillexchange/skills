---
title: "SBOM Generator with CycloneDX"
description: "Generates Software Bill of Materials in CycloneDX 1.5 format using cdxgen and syft. Enriches component data with license detection from clearlydefined.io and vulnerability cross-referencing via OSV.dev."
slug: "sbom-generator-cyclonedx"
category:
  - "Security &amp; Verification"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sbom-generator-cyclonedx/"
---

# SBOM Generator with CycloneDX

Generates Software Bill of Materials in CycloneDX 1.5 format using cdxgen and syft. Enriches component data with license detection from clearlydefined.io and vulnerability cross-referencing via OSV.dev.

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
clawhub install sbom-generator-cyclonedx
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SBOM Generator with CycloneDX skill automates the creation of comprehensive Software Bills of Materials compliant with the CycloneDX 1.5 specification. It orchestrates multiple scanning tools including cdxgen for application dependencies and syft for container image analysis to produce merged, deduplicated SBOMs.
The skill enriches raw dependency data by querying clearlydefined.io for authoritative license classifications, resolving ambiguous SPDX expressions, and flagging components with unknown or copyleft licenses that may conflict with your project’s licensing policy. Vulnerability enrichment queries the OSV.dev API and NVD to attach CVE/GHSA identifiers with CVSS scores and exploitability metrics.
For container images, the skill performs layer-by-layer analysis identifying which base image introduced each vulnerable package. It supports all major ecosystems including npm, PyPI, Maven, Go modules, Cargo, and NuGet. Output formats include CycloneDX JSON/XML, SPDX 2.3, and human-readable HTML reports. The skill can also validate existing SBOMs against the NTIA minimum elements checklist and generate VEX (Vulnerability Exploitability eXchange) documents for known false positives.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sbom-generator-cyclonedx/)
