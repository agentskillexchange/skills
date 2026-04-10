---
title: "Checkov Infrastructure Policy Scanner"
description: "Scans IaC files with Bridgecrew Checkov for policy violations across Terraform, CloudFormation, Kubernetes, and Dockerfile configurations. Supports custom Python-based policy authoring and Prisma Cloud integration."
slug: "checkov-infrastructure-policy-scanner"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/"
---

# Checkov Infrastructure Policy Scanner

Scans IaC files with Bridgecrew Checkov for policy violations across Terraform, CloudFormation, Kubernetes, and Dockerfile configurations. Supports custom Python-based policy authoring and Prisma Cloud integration.

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
clawhub install checkov-infrastructure-policy-scanner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Checkov Infrastructure Policy Scanner skill enforces security and compliance policies across Infrastructure-as-Code repositories using the Bridgecrew Checkov static analysis engine. It scans Terraform HCL and plan files, AWS CloudFormation templates, Kubernetes manifests, Helm charts, Dockerfiles, and Serverless Framework configurations for misconfigurations and policy violations. Built-in policies cover CIS benchmarks for major cloud providers (AWS, Azure, GCP), SOC2 controls, HIPAA requirements, and PCI-DSS compliance standards. The skill supports custom policy authoring in Python using the Checkov BaseCheck and BaseGraphCheck classes for organization-specific rules that inspect individual resources or cross-resource relationships. Graph-based policies detect complex violations like unrestricted security group chains or IAM privilege escalation paths. Results include severity ratings, compliance framework mappings, and guided remediation code fixes. Integration with Prisma Cloud enables centralized policy management across repositories, drift detection between deployed infrastructure and code, and supply chain security analysis of module dependencies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/)
