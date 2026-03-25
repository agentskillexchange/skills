---
name: "Checkov Infrastructure Policy Scanner"
description: "Scans IaC files with Bridgecrew Checkov for policy violations across Terraform, CloudFormation, Kubernetes, and Dockerfile configurations. Supports custom Python-based policy authoring and Prisma Cloud integration."
category: "Security & Verification"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# Checkov Infrastructure Policy Scanner

Scans IaC files with Bridgecrew Checkov for policy violations across Terraform, CloudFormation, Kubernetes, and Dockerfile configurations. Supports custom Python-based policy authoring and Prisma Cloud integration.

## Overview

The Checkov Infrastructure Policy Scanner skill enforces security and compliance policies across Infrastructure-as-Code repositories using the Bridgecrew Checkov static analysis engine. It scans Terraform HCL and plan files, AWS CloudFormation templates, Kubernetes manifests, Helm charts, Dockerfiles, and Serverless Framework configurations for misconfigurations and policy violations. Built-in policies cover CIS benchmarks for major cloud providers (AWS, Azure, GCP), SOC2 controls, HIPAA requirements, and PCI-DSS compliance standards. The skill supports custom policy authoring in Python using the Checkov BaseCheck and BaseGraphCheck classes for organization-specific rules that inspect individual resources or cross-resource relationships. Graph-based policies detect complex violations like unrestricted security group chains or IAM privilege escalation paths. Results include severity ratings, compliance framework mappings, and guided remediation code fixes. Integration with Prisma Cloud enables centralized policy management across repositories, drift detection between deployed infrastructure and code, and supply chain security analysis of module dependencies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill checkov-infrastructure-policy-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill checkov-infrastructure-policy-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill checkov-infrastructure-policy-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill checkov-infrastructure-policy-scanner -a codex
```

### OpenClaw

```bash
clawhub install checkov-infrastructure-policy-scanner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/
