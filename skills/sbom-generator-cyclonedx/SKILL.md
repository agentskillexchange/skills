---
title: "SBOM Generator with CycloneDX"
description: "Generates Software Bill of Materials in CycloneDX 1.5 format using cdxgen and syft. Enriches component data with license detection from clearlydefined.io and vulnerability cross-referencing via OSV.dev."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sbom-generator-cyclonedx/"
category:
  - "Security & Verification"
framework:
  - "Gemini"
---

# SBOM Generator with CycloneDX

The SBOM Generator with CycloneDX skill automates the creation of comprehensive Software Bills of Materials compliant with the CycloneDX 1.5 specification. It orchestrates multiple scanning tools including cdxgen for application dependencies and syft for container image analysis to produce merged, deduplicated SBOMs.

The skill enriches raw dependency data by querying clearlydefined.io for authoritative license classifications, resolving ambiguous SPDX expressions, and flagging components with unknown or copyleft licenses that may conflict with your project’s licensing policy. Vulnerability enrichment queries the OSV.dev API and NVD to attach CVE/GHSA identifiers with CVSS scores and exploitability metrics.

For container images, the skill performs layer-by-layer analysis identifying which base image introduced each vulnerable package. It supports all major ecosystems including npm, PyPI, Maven, Go modules, Cargo, and NuGet. Output formats include CycloneDX JSON/XML, SPDX 2.3, and human-readable HTML reports. The skill can also validate existing SBOMs against the NTIA minimum elements checklist and generate VEX (Vulnerability Exploitability eXchange) documents for known false positives.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sbom-generator-cyclonedx/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sbom-generator-cyclonedx
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sbom-generator-cyclonedx`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sbom-generator-cyclonedx/)
