---
title: "Trivy Container Scanner"
description: "The Trivy Container Scanner skill integrates Aqua Security Trivy into CI/CD and agent-driven security workflows. It executes trivy image scans against OCI-compliant container registries, analyzing OS packages (Alpine, Debian, Ubuntu, RHEL) and application dependencies (npm, pip, gem, go modules) in a single pass. Scan results are parsed from Trivy JSON output, with vulnerabilities enriched from multiple data sources including the NVD (National Vulnerability Database), Red Hat Security Data API, and Alpine SecDB. The skill filters results using .trivyignore policies and OPA Rego policies for organization-specific exception handling. Output formats include SARIF for GitHub Advanced Security code scanning upload via the GitHub REST API (/repos/{owner}/{repo}/code-scanning/sarifs), CycloneDX SBOM for dependency tracking, and custom JSON for internal dashboards. The skill also generates in-toto SLSA provenance attestations attached to images via Cosign, recording the scan tool version, policy files, and vulnerability counts as predicate data. Registry authentication supports Docker Hub, GitHub Container Registry (ghcr.io), AWS ECR (via boto3 get-authorization-token), and Google Artifact Registry via gcloud auth print-access-token."
source: "https://github.com/aquasecurity/trivy"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "aquasecurity/trivy"
  github_stars: 34488
---

# Trivy Container Scanner

The Trivy Container Scanner skill integrates Aqua Security Trivy into CI/CD and agent-driven security workflows. It executes trivy image scans against OCI-compliant container registries, analyzing OS packages (Alpine, Debian, Ubuntu, RHEL) and application dependencies (npm, pip, gem, go modules) in a single pass. Scan results are parsed from Trivy JSON output, with vulnerabilities enriched from multiple data sources including the NVD (National Vulnerability Database), Red Hat Security Data API, and Alpine SecDB. The skill filters results using .trivyignore policies and OPA Rego policies for organization-specific exception handling. Output formats include SARIF for GitHub Advanced Security code scanning upload via the GitHub REST API (/repos/{owner}/{repo}/code-scanning/sarifs), CycloneDX SBOM for dependency tracking, and custom JSON for internal dashboards. The skill also generates in-toto SLSA provenance attestations attached to images via Cosign, recording the scan tool version, policy files, and vulnerability counts as predicate data. Registry authentication supports Docker Hub, GitHub Container Registry (ghcr.io), AWS ECR (via boto3 get-authorization-token), and Google Artifact Registry via gcloud auth print-access-token.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trivy-container-scanner-2/)
