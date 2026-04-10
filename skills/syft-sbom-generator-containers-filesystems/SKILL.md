---
title: "Syft SBOM Generator for Containers and Filesystems"
description: "Syft by Anchore is a CLI tool for generating Software Bills of Materials (SBOMs) from container images and filesystems. Supports CycloneDX, SPDX, and multiple output formats with coverage across dozens of packaging ecosystems including npm, PyPI, Go, and more."
slug: "syft-sbom-generator-containers-filesystems"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/anchore/syft"
tool_ecosystem:
  github_repo: "anchore/syft"
  github_stars: 8628
---

# Syft SBOM Generator for Containers and Filesystems

Syft by Anchore is a CLI tool for generating Software Bills of Materials (SBOMs) from container images and filesystems. Supports CycloneDX, SPDX, and multiple output formats with coverage across dozens of packaging ecosystems including npm, PyPI, Go, and more.

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
clawhub install syft-sbom-generator-containers-filesystems
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Syft is a command-line tool and Go library developed by Anchore for generating Software Bills of Materials from container images, filesystems, and archives. With over 6,000 GitHub stars, 100+ contributors, and regular releases, it has become one of the most widely deployed SBOM generation tools in the open-source ecosystem.
The tool supports dozens of packaging ecosystems out of the box, including Alpine (apk), Debian (dpkg), RPM, Go modules, Python (pip/poetry/conda), Java (Maven/Gradle), JavaScript (npm/yarn), Ruby (gems), Rust (cargo), PHP (composer), .NET (NuGet), and many more. For container scanning, it handles OCI images, Docker images, Singularity containers, and can scan directly from registries without pulling the full image.
Syft produces SBOMs in multiple industry-standard formats: CycloneDX JSON and XML, SPDX JSON and tag-value, the native Syft JSON format, and GitHub’s dependency snapshot format. It can also convert between SBOM formats, making it useful as a normalization layer in supply chain security pipelines. For attestation workflows, Syft can create signed SBOM attestations using the in-toto specification, integrating with Sigstore for keyless signing.
The tool pairs naturally with Anchore’s vulnerability scanner Grype: pipe Syft’s SBOM output into Grype to get vulnerability matches against multiple vulnerability databases. Installation is available through Homebrew, APT, RPM, Scoop, Chocolatey, Nix, and a Docker image (anchore/syft). Basic usage is straightforward: syft alpine:latest scans a container image, while syft ./my-project scans a local directory. Adding -o cyclonedx-json outputs in CycloneDX format. The project is licensed under Apache-2.0 and maintained at github.com/anchore/syft with active community meetings and comprehensive documentation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/syft-sbom-generator-containers-filesystems/)
