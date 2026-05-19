---
name: "CycloneDX SBOM Generator"
slug: "cyclonedx-sbom-generator"
description: "Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration."
github_stars: 956
verification: "security_reviewed"
source: "https://github.com/cdxgen/cdxgen"
author: "cdxgen"
category: "Security & Verification"
framework: "Cursor"
tool_ecosystem:
  github_repo: "cdxgen/cdxgen"
  github_stars: 956
---

# CycloneDX SBOM Generator

Generates Software Bill of Materials in CycloneDX format using cdxgen and Syft. Scans npm, pip, and Go modules for known CVEs via OSV.dev API integration.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @cyclonedx/cdxgen
- $ brew install cdxgen
- docker run --rm -e CDXGEN_DEBUG_MODE=debug -v /tmp:/tmp -v $(pwd):/app:rw -t ghcr.io/cyclonedx/cdxgen:master -r /app -o /app/bom.json
- docker run --rm -e CDXGEN_DEBUG_MODE=debug -v /tmp:/tmp -v $(pwd):/app:rw -t ghcr.io/cyclonedx/cdxgen-deno:master -r /app -o /app/bom.json

Requirements and caveats from upstream:
- Software-as-a-Service (SaaSBOM) - For Java, Python, JavaScript, TypeScript, and PHP projects.
- You can also use the cdxgen container image with node, deno, or bun runtime versions.
- The default version uses Node.js 23

Basic usage or getting-started notes:
- | **Developers** | Generate a CycloneDX BOM from a local repo, git URL, purl, or container image | cdxgen -o bom.json . | [CLI Usage][docs-cli], [Supported Project Types][docs-project-types] |
- | **AppSec** | Enrich BOMs with evidence, run BOM audit rules, and feed downstream security workflows | cdxgen -o bom.json --profile appsec --evidence --bom-audit . | [BOM Audit](docs/BOM_AUDIT.md), [Threat Model](doc...
- | **SOC analysts** | Build OBOM inventories for live hosts and triage runtime posture issues | obom -o obom.json --deep --bom-audit --bom-audit-categories obom-runtime | [OBOM lessons](docs/OBOM_LESSONS.md), [Server U...

- Source: https://github.com/cdxgen/cdxgen
- Extracted from upstream docs: https://raw.githubusercontent.com/cdxgen/cdxgen/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cyclonedx-sbom-generator/)
