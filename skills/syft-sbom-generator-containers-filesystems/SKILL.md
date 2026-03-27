---
name: "Syft SBOM Generator for Containers and Filesystems"
description: "Syft by Anchore is a CLI tool for generating Software Bills of Materials (SBOMs) from container images and filesystems. Supports CycloneDX, SPDX, and multiple output formats with coverage across dozens of packaging ecosystems including npm, PyPI, Go, and more."
category: "Security & Verification"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/syft-sbom-generator-containers-filesystems/"
---

# Syft SBOM Generator for Containers and Filesystems

Syft by Anchore is a CLI tool for generating Software Bills of Materials (SBOMs) from container images and filesystems. Supports CycloneDX, SPDX, and multiple output formats with coverage across dozens of packaging ecosystems including npm, PyPI, Go, and more.

## Overview

Syft is a command-line tool and Go library developed by Anchore for generating Software Bills of Materials from container images, filesystems, and archives. With over 6,000 GitHub stars, 100+ contributors, and regular releases, it has become one of the most widely deployed SBOM generation tools in the open-source ecosystem.

The tool supports dozens of packaging ecosystems out of the box, including Alpine (apk), Debian (dpkg), RPM, Go modules, Python (pip/poetry/conda), Java (Maven/Gradle), JavaScript (npm/yarn), Ruby (gems), Rust (cargo), PHP (composer), .NET (NuGet), and many more. For container scanning, it handles OCI images, Docker images, Singularity containers, and can scan directly from registries without pulling the full image.

Syft produces SBOMs in multiple industry-standard formats: CycloneDX JSON and XML, SPDX JSON and tag-value, the native Syft JSON format, and GitHub’s dependency snapshot format. It can also convert between SBOM formats, making it useful as a normalization layer in supply chain security pipelines. For attestation workflows, Syft can create signed SBOM attestations using the in-toto specification, integrating with Sigstore for keyless signing.

The tool pairs naturally with Anchore’s vulnerability scanner Grype: pipe Syft’s SBOM output into Grype to get vulnerability matches against multiple vulnerability databases. Installation is available through Homebrew, APT, RPM, Scoop, Chocolatey, Nix, and a Docker image (anchore/syft). Basic usage is straightforward: syft alpine:latest scans a container image, while syft ./my-project scans a local directory. Adding -o cyclonedx-json outputs in CycloneDX format. The project is licensed under Apache-2.0 and maintained at github.com/anchore/syft with active community meetings and comprehensive documentation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill syft-sbom-generator-containers-filesystems
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill syft-sbom-generator-containers-filesystems -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill syft-sbom-generator-containers-filesystems -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill syft-sbom-generator-containers-filesystems -a codex
```

### OpenClaw

```bash
clawhub install syft-sbom-generator-containers-filesystems
```

## Source

- Marketplace: https://agentskillexchange.com/skills/syft-sbom-generator-containers-filesystems/
