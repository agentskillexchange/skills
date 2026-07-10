---
name: "Scan agent dependencies and container inputs with OWASP dep-scan"
slug: "scan-agent-dependencies-and-container-inputs-with-owasp-dep-scan"
description: "Run OWASP dep-scan before adopting dependencies, containers, or generated code so agents get a reviewable vulnerability, license, SBOM, and risk report."
github_stars: 1260
verification: "security_reviewed"
source: "https://github.com/owasp-dep-scan/dep-scan"
author: "OWASP dep-scan"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "owasp-dep-scan/dep-scan"
  github_stars: 1260
---

# Scan agent dependencies and container inputs with OWASP dep-scan

Run OWASP dep-scan before adopting dependencies, containers, or generated code so agents get a reviewable vulnerability, license, SBOM, and risk report.

## Prerequisites

Python, pip, OWASP dep-scan, optional CycloneDX cdxgen, Docker for container-image scans, CI runner or local shell

## Installation

Use the upstream install or setup path that matches your environment:
- pip install owasp-depscan
- pip install owasp-depscan[all]
- docker save -o /tmp/scanslim.tar shiftleft/scan-slim:latest
- docker run --rm -v $PWD:/app ghcr.io/owasp-dep-scan/dep-scan depscan --src /app --reports-dir /app/reports

Requirements and caveats from upstream:
- [Scanning projects locally (Python version)](#scanning-projects-locally-python-version)
- [Scanning containers locally (Python version)](#scanning-containers-locally-python-version)
- [Scanning projects locally (Docker container)](#scanning-projects-locally-docker-container)

Basic usage or getting-started notes:
- [Quick Start](#quick-start)
- [Example analysis for a Java project](https://depscan.readthedocs.io/reachability-analysis#example-analysis-for-a-java-project)
- [Example analysis for a JavaScript project](https://depscan.readthedocs.io/reachability-analysis#example-analysis-for-a-java-project)

- Source: https://github.com/owasp-dep-scan/dep-scan
- Extracted from upstream docs: https://raw.githubusercontent.com/owasp-dep-scan/dep-scan/HEAD/README.md

## Documentation

- https://depscan.readthedocs.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-dependencies-and-container-inputs-with-owasp-dep-scan/)
