---
title: "Trivy Container Scanner"
description: "Wraps the Trivy CLI for comprehensive container image vulnerability scanning. Outputs results in SARIF format for GitHub Code Scanning API integration and generates OCI artifact attestations."
verification: "security_reviewed"
source: "https://github.com/aquasecurity/trivy"
category:
  - "Security & Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "aquasecurity/trivy"
  github_stars: 34488
---

# Trivy Container Scanner

The Trivy Container Scanner skill integrates Aqua Security Trivy into CI/CD and agent-driven security workflows. It executes trivy image scans against OCI-compliant container registries, analyzing OS packages (Alpine, Debian, Ubuntu, RHEL) and application dependencies (npm, pip, gem, go modules) in a single pass. Scan results are parsed from Trivy JSON output, with vulnerabilities enriched from multiple data sources including the NVD (National Vulnerability Database), Red Hat Security Data API, and Alpine SecDB. The skill filters results using .trivyignore policies and OPA Rego policies for organization-specific exception handling. Output formats include SARIF for GitHub Advanced Security code scanning upload via the GitHub REST API (/repos/{owner}/{repo}/code-scanning/sarifs), CycloneDX SBOM for dependency tracking, and custom JSON for internal dashboards. The skill also generates in-toto SLSA provenance attestations attached to images via Cosign, recording the scan tool version, policy files, and vulnerability counts as predicate data. Registry authentication supports Docker Hub, GitHub Container Registry (ghcr.io), AWS ECR (via boto3 get-authorization-token), and Google Artifact Registry via gcloud auth print-access-token.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/trivy-container-scanner-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/trivy-container-scanner-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/trivy-container-scanner-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trivy-container-scanner-2/)
