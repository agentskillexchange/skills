---
title: "Scan images filesystems and SBOMs for end-of-life software before unsupported components ship with Xeol"
description: "Find packages that are out of support even when they do not show up as a classic CVE finding yet."
verification: "security_reviewed"
source: "https://github.com/xeol-io/xeol"
author: "xeol-io"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "xeol-io/xeol"
  github_stars: 435
---

# Scan images filesystems and SBOMs for end-of-life software before unsupported components ship with Xeol

Find packages that are out of support even when they do not show up as a classic CVE finding yet.

## Prerequisites

Xeol CLI, a container image filesystem path or SBOM input, and optional CI integration for release gating.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Xeol from the upstream release, package, or container instructions, point it at the target image, directory, or SBOM source, and review the EOL findings before release or deployment.
```

## Documentation

- https://www.xeol.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-images-filesystems-and-sboms-for-end-of-life-software-before-unsupported-components-ship-with-xeol/)
