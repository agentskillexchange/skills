---
title: Trivy Container Scanner
description: The Trivy Container Scanner skill integrates Aqua Security Trivy into
  CI/CD and agent-driven security workflows. It executes trivy image scans against
  OCI-compliant container registries, analyzing OS packages (Alpine, Debian, Ubuntu,
  RHEL) and application dependencies (npm, pip, gem, go modules) in a single pass.
  Scan results are parsed from Trivy JSON output, with vulnerabilities enriched from
  multiple data sources including the NVD (National Vulnerability Database), Red Hat
  Security Data API, and Alpine SecDB. The skill filters results using .trivyignore
  policies and OPA Rego policies for organization-specific exception handling. Output
  formats include SARIF for GitHub Advanced Security code scanning upload via the
  GitHub REST API (/repos/{owner}/{repo}/code-scanning/sarifs), CycloneDX SBOM for
  dependency tracking, and custom JSON for internal dashboards. The skill also generates
  in-toto SLSA provenance attestations attached to images via Cosign, recording the
  scan tool version, policy files, and vulnerability counts as predicate data. Registry
  authentication supports Docker Hub, GitHub Container Registry (ghcr.io), AWS ECR
  (via boto3 get-authorization-token), and Google Artifact Registry via gcloud auth
  print-access-token.
verification: security_reviewed
source: https://agentskillexchange.com/skills/trivy-container-scanner-2/
category:
- Security &amp; Verification
framework:
- OpenClaw
---

# Trivy Container Scanner

The Trivy Container Scanner skill integrates Aqua Security Trivy into CI/CD and agent-driven security workflows. It executes trivy image scans against OCI-compliant container registries, analyzing OS packages (Alpine, Debian, Ubuntu, RHEL) and application dependencies (npm, pip, gem, go modules) in a single pass. Scan results are parsed from Trivy JSON output, with vulnerabilities enriched from multiple data sources including the NVD (National Vulnerability Database), Red Hat Security Data API, and Alpine SecDB. The skill filters results using .trivyignore policies and OPA Rego policies for organization-specific exception handling. Output formats include SARIF for GitHub Advanced Security code scanning upload via the GitHub REST API (/repos/{owner}/{repo}/code-scanning/sarifs), CycloneDX SBOM for dependency tracking, and custom JSON for internal dashboards. The skill also generates in-toto SLSA provenance attestations attached to images via Cosign, recording the scan tool version, policy files, and vulnerability counts as predicate data. Registry authentication supports Docker Hub, GitHub Container Registry (ghcr.io), AWS ECR (via boto3 get-authorization-token), and Google Artifact Registry via gcloud auth print-access-token.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trivy-container-scanner-2/)
