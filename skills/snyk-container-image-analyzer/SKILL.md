---
title: "Snyk Container Image Analyzer"
description: "The Snyk Container Image Analyzer performs comprehensive vulnerability assessment of container images throughout the CI/CD pipeline and runtime environments. It connects to the Snyk Container API to scan both OS-level packages (dpkg, rpm, apk) and application dependencies embedded within image layers.\nThe analyzer pulls image manifests from any OCI-compliant registry including Docker Hub, Amazon ECR, Google Artifact Registry, and Azure Container Registry. Each layer is unpacked and analyzed against the Snyk vulnerability database, which aggregates data from NVD, distribution security advisories, and Snyk proprietary research.\nFindings include CVSS v3.1 scores, exploit maturity ratings, and specific remediation paths. For Dockerfile-based images, the skill generates actionable fix suggestions including base image upgrades, package pinning recommendations, and multi-stage build optimizations to reduce attack surface. Results integrate with GitHub Actions and GitLab CI via SARIF output, and support Snyk monitoring for continuous image tracking with Slack notifications when new vulnerabilities affect deployed images."
verification: security_reviewed
source: "https://github.com/snyk/cli"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/snyk-container-image-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/snyk-container-image-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-container-image-analyzer/)
