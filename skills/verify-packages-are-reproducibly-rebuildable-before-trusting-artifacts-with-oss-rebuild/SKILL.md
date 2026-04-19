---
title: "Verify Packages Are Reproducibly Rebuildable Before Trusting Artifacts With Oss Rebuild"
description: "OSS Rebuild is a supply-chain verification skill for checking whether published npm, PyPI, or Crates.io artifacts have corresponding rebuild attestations. An agent should invoke it when a user needs to validate package integrity before dependency approval, security review, or incident response, rather than relying on trust in the package registry alone. Use this instead of a broad security platform when the task is specifically rebuild verification and attestation lookup. The boundary is clear: inspect rebuild results, list rebuilt versions, and surface attestation details for a package version. It is not a generic SBOM product, package manager, or security dashboard listing."
source: "https://github.com/google/oss-rebuild"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "google/oss-rebuild"
  github_stars: 687
---

# Verify Packages Are Reproducibly Rebuildable Before Trusting Artifacts With Oss Rebuild

OSS Rebuild is a supply-chain verification skill for checking whether published npm, PyPI, or Crates.io artifacts have corresponding rebuild attestations. An agent should invoke it when a user needs to validate package integrity before dependency approval, security review, or incident response, rather than relying on trust in the package registry alone. Use this instead of a broad security platform when the task is specifically rebuild verification and attestation lookup. The boundary is clear: inspect rebuild results, list rebuilt versions, and surface attestation details for a package version. It is not a generic SBOM product, package manager, or security dashboard listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-packages-are-reproducibly-rebuildable-before-trusting-artifacts-with-oss-rebuild/)
