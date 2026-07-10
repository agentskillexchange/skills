---
title: "Scan agent dependencies and container inputs with OWASP dep-scan"
description: "Run OWASP dep-scan before adopting dependencies, containers, or generated code so agents get a reviewable vulnerability, license, SBOM, and risk report."
verification: "security_reviewed"
source: "https://github.com/owasp-dep-scan/dep-scan"
author: "OWASP dep-scan"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "owasp-dep-scan/dep-scan"
  github_stars: 1260
---

# Scan agent dependencies and container inputs with OWASP dep-scan

Run OWASP dep-scan before adopting dependencies, containers, or generated code so agents get a reviewable vulnerability, license, SBOM, and risk report.

## Prerequisites

Python, pip, OWASP dep-scan, optional CycloneDX cdxgen, Docker for container-image scans, CI runner or local shell

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install CycloneDX cdxgen when SBOM generation is needed, install dep-scan with pip install owasp-depscan or pip install owasp-depscan[all], change into the project to scan, then run depscan --src $PWD --reports-dir $PWD/reports or point --src at a container image with the appropriate type.
```

## Documentation

- https://depscan.readthedocs.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-dependencies-and-container-inputs-with-owasp-dep-scan/)
