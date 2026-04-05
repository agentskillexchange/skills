---
name: "Trivy Container Scanner"
description: "Wraps the Trivy CLI for comprehensive container image vulnerability scanning. Outputs results in SARIF format for GitHub Code Scanning API integration and generates OCI artifact attestations."
category: "Security &amp; Verification"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/trivy-container-scanner-2/"
---
# Trivy Container Scanner

Wraps the Trivy CLI for comprehensive container image vulnerability scanning. Outputs results in SARIF format for GitHub Code Scanning API integration and generates OCI artifact attestations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill trivy-container-scanner-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill trivy-container-scanner-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill trivy-container-scanner-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill trivy-container-scanner-2 -a codex
```

### OpenClaw

```bash
clawhub install trivy-container-scanner-2
```

## Details

The Trivy Container Scanner skill integrates Aqua Security Trivy into CI/CD and agent-driven security workflows. It executes trivy image scans against OCI-compliant container registries, analyzing OS packages (Alpine, Debian, Ubuntu, RHEL) and application dependencies (npm, pip, gem, go modules) in a single pass.

Scan results are parsed from Trivy JSON output, with vulnerabilities enriched from multiple data sources including the NVD (National Vulnerability Database), Red Hat Security Data API, and Alpine SecDB. The skill filters results using .trivyignore policies and OPA Rego policies for organization-specific exception handling.

Output formats include SARIF for GitHub Advanced Security code scanning upload via the GitHub REST API (/repos/{owner}/{repo}/code-scanning/sarifs), CycloneDX SBOM for dependency tracking, and custom JSON for internal dashboards. The skill also generates in-toto SLSA provenance attestations attached to images via Cosign, recording the scan tool version, policy files, and vulnerability counts as predicate data. Registry authentication supports Docker Hub, GitHub Container Registry (ghcr.io), AWS ECR (via boto3 get-authorization-token), and Google Artifact Registry via gcloud auth print-access-token.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trivy-container-scanner-2/)
