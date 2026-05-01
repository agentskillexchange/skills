---
title: "Scan images filesystems and SBOMs for end-of-life software before unsupported components ship with Xeol"
description: "Find packages that are out of support even when they do not show up as a classic CVE finding yet."
verification: "listed"
source: "https://github.com/xeol-io/xeol"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "xeol-io/xeol"
  github_stars: 435
---

# Scan images filesystems and SBOMs for end-of-life software before unsupported components ship with Xeol

Use Xeol when an agent needs an end-of-life inventory check over a container image, filesystem, or SBOM, not when the user is running a general vulnerability scanner. The workflow is bounded: inspect the software bill of materials or image contents, identify packages that have reached or are nearing end of support, and return an upgrade or exception list before release. That scope boundary, EOL exposure detection rather than generic CVE scanning, keeps this distinct and skill-shaped.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/scan-images-filesystems-and-sboms-for-end-of-life-software-before-unsupported-components-ship-with-xeol/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scan-images-filesystems-and-sboms-for-end-of-life-software-before-unsupported-components-ship-with-xeol
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/scan-images-filesystems-and-sboms-for-end-of-life-software-before-unsupported-components-ship-with-xeol`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-images-filesystems-and-sboms-for-end-of-life-software-before-unsupported-components-ship-with-xeol/)
