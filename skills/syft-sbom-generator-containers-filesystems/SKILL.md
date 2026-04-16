---
title: "Syft SBOM Generator for Containers and Filesystems"
description: "Syft by Anchore is a CLI tool for generating Software Bills of Materials (SBOMs) from container images and filesystems. Supports CycloneDX, SPDX, and multiple output formats with coverage across dozens of packaging ecosystems including npm, PyPI, Go, and more."
verification: "security_reviewed"
source: "https://github.com/anchore/syft"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "anchore/syft"
  github_stars: 8628
---

# Syft SBOM Generator for Containers and Filesystems

Syft is a command-line tool and Go library developed by Anchore for generating Software Bills of Materials from container images, filesystems, and archives. With over 6,000 GitHub stars, 100+ contributors, and regular releases, it has become one of the most widely deployed SBOM generation tools in the open-source ecosystem.


The tool supports dozens of packaging ecosystems out of the box, including Alpine (apk), Debian (dpkg), RPM, Go modules, Python (pip/poetry/conda), Java (Maven/Gradle), JavaScript (npm/yarn), Ruby (gems), Rust (cargo), PHP (composer), .NET (NuGet), and many more. For container scanning, it handles OCI images, Docker images, Singularity containers, and can scan directly from registries without pulling the full image.


Syft produces SBOMs in multiple industry-standard formats: CycloneDX JSON and XML, SPDX JSON and tag-value, the native Syft JSON format, and GitHub’s dependency snapshot format. It can also convert between SBOM formats, making it useful as a normalization layer in supply chain security pipelines. For attestation workflows, Syft can create signed SBOM attestations using the in-toto specification, integrating with Sigstore for keyless signing.


The tool pairs naturally with Anchore’s vulnerability scanner Grype: pipe Syft’s SBOM output into Grype to get vulnerability matches against multiple vulnerability databases. Installation is available through Homebrew, APT, RPM, Scoop, Chocolatey, Nix, and a Docker image (anchore/syft). Basic usage is straightforward: syft alpine:latest scans a container image, while syft ./my-project scans a local directory. Adding -o cyclonedx-json outputs in CycloneDX format. The project is licensed under Apache-2.0 and maintained at github.com/anchore/syft with active community meetings and comprehensive documentation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/syft-sbom-generator-containers-filesystems/)
