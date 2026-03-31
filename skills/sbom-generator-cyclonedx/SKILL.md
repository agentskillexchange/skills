---
name: "SBOM Generator with CycloneDX"
description: "Generates Software Bill of Materials in CycloneDX 1.5 format using cdxgen and syft. Enriches component data with license detection from clearlydefined.io and vulnerability cross-referencing via OSV.dev."
category: "Security &amp; Verification"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sbom-generator-cyclonedx/"
---
# SBOM Generator with CycloneDX

Generates Software Bill of Materials in CycloneDX 1.5 format using cdxgen and syft. Enriches component data with license detection from clearlydefined.io and vulnerability cross-referencing via OSV.dev.

## Overview

The SBOM Generator with CycloneDX skill automates the creation of comprehensive Software Bills of Materials compliant with the CycloneDX 1.5 specification. It orchestrates multiple scanning tools including cdxgen for application dependencies and syft for container image analysis to produce merged, deduplicated SBOMs.

The skill enriches raw dependency data by querying clearlydefined.io for authoritative license classifications, resolving ambiguous SPDX expressions, and flagging components with unknown or copyleft licenses that may conflict with your project's licensing policy. Vulnerability enrichment queries the OSV.dev API and NVD to attach CVE/GHSA identifiers with CVSS scores and exploitability metrics.

For container images, the skill performs layer-by-layer analysis identifying which base image introduced each vulnerable package. It supports all major ecosystems including npm, PyPI, Maven, Go modules, Cargo, and NuGet. Output formats include CycloneDX JSON/XML, SPDX 2.3, and human-readable HTML reports. The skill can also validate existing SBOMs against the NTIA minimum elements checklist and generate VEX (Vulnerability Exploitability eXchange) documents for known false positives.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sbom-generator-cyclonedx
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sbom-generator-cyclonedx -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sbom-generator-cyclonedx -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sbom-generator-cyclonedx -a codex
```

### OpenClaw

```bash
clawhub install sbom-generator-cyclonedx
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sbom-generator-cyclonedx/)
