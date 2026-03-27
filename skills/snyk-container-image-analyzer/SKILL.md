---
name: "Snyk Container Image Analyzer"
description: "Scans Docker and OCI container images for OS and application vulnerabilities using Snyk Container API. Cross-references findings against the Snyk vulnerability database with CVSS scoring and provides Dockerfile remediation suggestions."
category: "Security & Verification"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/snyk-container-image-analyzer/"
tool_ecosystem:
  tool: snyk
  github_stars: 5458
  npm_weekly_downloads: 601684
  github_repo: snyk/cli
  maintained: true
---

# Snyk Container Image Analyzer

Scans Docker and OCI container images for OS and application vulnerabilities using Snyk Container API. Cross-references findings against the Snyk vulnerability database with CVSS scoring and provides Dockerfile remediation suggestions.

## Overview

The Snyk Container Image Analyzer performs comprehensive vulnerability assessment of container images throughout the CI/CD pipeline and runtime environments. It connects to the Snyk Container API to scan both OS-level packages (dpkg, rpm, apk) and application dependencies embedded within image layers.

The analyzer pulls image manifests from any OCI-compliant registry including Docker Hub, Amazon ECR, Google Artifact Registry, and Azure Container Registry. Each layer is unpacked and analyzed against the Snyk vulnerability database, which aggregates data from NVD, distribution security advisories, and Snyk proprietary research.

Findings include CVSS v3.1 scores, exploit maturity ratings, and specific remediation paths. For Dockerfile-based images, the skill generates actionable fix suggestions including base image upgrades, package pinning recommendations, and multi-stage build optimizations to reduce attack surface. Results integrate with GitHub Actions and GitLab CI via SARIF output, and support Snyk monitoring for continuous image tracking with Slack notifications when new vulnerabilities affect deployed images.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill snyk-container-image-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill snyk-container-image-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill snyk-container-image-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill snyk-container-image-analyzer -a codex
```

### OpenClaw

```bash
clawhub install snyk-container-image-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/snyk-container-image-analyzer/
