---
name: "Dockerfile Security Hardening Advisor"
description: "Audits Dockerfiles for security vulnerabilities using Hadolint and Trivy container scanner. Recommends hardening steps based on CIS Docker Benchmark and Snyk container advisories."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dockerfile-security-hardening-advisor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "docker"  # from ase_tool_match
  github_stars: 71560  # from ase_github_stars (integer, not string)
  github_repo: "moby/moby"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Dockerfile Security Hardening Advisor

Audits Dockerfiles for security vulnerabilities using Hadolint and Trivy container scanner. Recommends hardening steps based on CIS Docker Benchmark and Snyk container advisories.

## Overview

The Dockerfile Security Hardening Advisor skill provides comprehensive security auditing for container images starting from the Dockerfile. It runs Hadolint for Dockerfile best practice validation and Trivy for vulnerability scanning of base images and installed packages.

The skill checks Dockerfiles against the CIS Docker Benchmark v1.5 controls, verifying that containers run as non-root users, use specific image tags instead of latest, minimize installed packages, and properly handle secrets. It queries the Snyk Container API for known vulnerabilities in base images.

Using Docker Scout API integration, the skill provides SBOM-based analysis of the final image layers, identifying which layer introduced each vulnerability. It recommends specific base image alternatives with fewer CVEs, comparing options across Alpine, Distroless, and Chainguard images.

The hardening report includes a prioritized action list with copy-paste Dockerfile modifications, estimated CVE reduction for each change, and a compliance score against organizational security policies. Output supports SARIF format for integration with GitHub Advanced Security.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dockerfile-security-hardening-advisor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dockerfile-security-hardening-advisor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dockerfile-security-hardening-advisor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dockerfile-security-hardening-advisor -a codex
```

### OpenClaw

```bash
clawhub install dockerfile-security-hardening-advisor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dockerfile-security-hardening-advisor/
