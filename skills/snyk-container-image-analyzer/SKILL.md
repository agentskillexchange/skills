---
title: "Snyk Container Image Analyzer"
description: "Scans Docker and OCI container images for OS and application vulnerabilities using Snyk Container API. Cross-references findings against the Snyk vulnerability database with CVSS scoring and provides Dockerfile remediation suggestions."
verification: "security_reviewed"
source: "https://github.com/snyk/cli"
category:
  - "Security & Verification"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "snyk/cli"
  github_stars: 5496
---

# Snyk Container Image Analyzer

The Snyk Container Image Analyzer performs comprehensive vulnerability assessment of container images throughout the CI/CD pipeline and runtime environments. It connects to the Snyk Container API to scan both OS-level packages (dpkg, rpm, apk) and application dependencies embedded within image layers.

The analyzer pulls image manifests from any OCI-compliant registry including Docker Hub, Amazon ECR, Google Artifact Registry, and Azure Container Registry. Each layer is unpacked and analyzed against the Snyk vulnerability database, which aggregates data from NVD, distribution security advisories, and Snyk proprietary research.

Findings include CVSS v3.1 scores, exploit maturity ratings, and specific remediation paths. For Dockerfile-based images, the skill generates actionable fix suggestions including base image upgrades, package pinning recommendations, and multi-stage build optimizations to reduce attack surface. Results integrate with GitHub Actions and GitLab CI via SARIF output, and support Snyk monitoring for continuous image tracking with Slack notifications when new vulnerabilities affect deployed images.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/snyk-container-image-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/snyk-container-image-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/snyk-container-image-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-container-image-analyzer/)
