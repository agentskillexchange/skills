---
title: "Scan images filesystems and SBOMs for end-of-life software before unsupported components ship with Xeol"
description: "Use Xeol when an agent needs an end-of-life inventory check over a container image, filesystem, or SBOM, not when the user is running a general vulnerability scanner. The workflow is bounded: inspect the software bill of materials or image contents, identify packages that have reached or are nearing end of support, and return an upgrade or exception list before release. That scope boundary, EOL exposure detection rather than generic CVE scanning, keeps this distinct and skill-shaped."
source: "https://github.com/xeol-io/xeol"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "xeol-io/xeol"
  github_stars: 435
---

# Scan images filesystems and SBOMs for end-of-life software before unsupported components ship with Xeol

Use Xeol when an agent needs an end-of-life inventory check over a container image, filesystem, or SBOM, not when the user is running a general vulnerability scanner. The workflow is bounded: inspect the software bill of materials or image contents, identify packages that have reached or are nearing end of support, and return an upgrade or exception list before release. That scope boundary, EOL exposure detection rather than generic CVE scanning, keeps this distinct and skill-shaped.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-images-filesystems-and-sboms-for-end-of-life-software-before-unsupported-components-ship-with-xeol/)
