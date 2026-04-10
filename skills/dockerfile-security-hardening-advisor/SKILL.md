---
title: "Dockerfile Security Hardening Advisor"
description: "Audits Dockerfiles for security vulnerabilities using Hadolint and Trivy container scanner. Recommends hardening steps based on CIS Docker Benchmark and Snyk container advisories."
slug: "dockerfile-security-hardening-advisor"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dockerfile-security-hardening-advisor/"
---

# Dockerfile Security Hardening Advisor

Audits Dockerfiles for security vulnerabilities using Hadolint and Trivy container scanner. Recommends hardening steps based on CIS Docker Benchmark and Snyk container advisories.

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
clawhub install dockerfile-security-hardening-advisor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Dockerfile Security Hardening Advisor skill provides comprehensive security auditing for container images starting from the Dockerfile. It runs Hadolint for Dockerfile best practice validation and Trivy for vulnerability scanning of base images and installed packages.
The skill checks Dockerfiles against the CIS Docker Benchmark v1.5 controls, verifying that containers run as non-root users, use specific image tags instead of latest, minimize installed packages, and properly handle secrets. It queries the Snyk Container API for known vulnerabilities in base images.
Using Docker Scout API integration, the skill provides SBOM-based analysis of the final image layers, identifying which layer introduced each vulnerability. It recommends specific base image alternatives with fewer CVEs, comparing options across Alpine, Distroless, and Chainguard images.
The hardening report includes a prioritized action list with copy-paste Dockerfile modifications, estimated CVE reduction for each change, and a compliance score against organizational security policies. Output supports SARIF format for integration with GitHub Advanced Security.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dockerfile-security-hardening-advisor/)
