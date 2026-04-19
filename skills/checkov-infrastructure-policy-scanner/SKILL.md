---
title: "Checkov Infrastructure Policy Scanner"
description: "The Checkov Infrastructure Policy Scanner skill enforces security and compliance policies across Infrastructure-as-Code repositories using the Bridgecrew Checkov static analysis engine. It scans Terraform HCL and plan files, AWS CloudFormation templates, Kubernetes manifests, Helm charts, Dockerfiles, and Serverless Framework configurations for misconfigurations and policy violations. Built-in policies cover CIS benchmarks for major cloud providers (AWS, Azure, GCP), SOC2 controls, HIPAA requirements, and PCI-DSS compliance standards. The skill supports custom policy authoring in Python using the Checkov BaseCheck and BaseGraphCheck classes for organization-specific rules that inspect individual resources or cross-resource relationships. Graph-based policies detect complex violations like unrestricted security group chains or IAM privilege escalation paths. Results include severity ratings, compliance framework mappings, and guided remediation code fixes. Integration with Prisma Cloud enables centralized policy management across repositories, drift detection between deployed infrastructure and code, and supply chain security analysis of module dependencies."
source: "https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
---

# Checkov Infrastructure Policy Scanner

The Checkov Infrastructure Policy Scanner skill enforces security and compliance policies across Infrastructure-as-Code repositories using the Bridgecrew Checkov static analysis engine. It scans Terraform HCL and plan files, AWS CloudFormation templates, Kubernetes manifests, Helm charts, Dockerfiles, and Serverless Framework configurations for misconfigurations and policy violations. Built-in policies cover CIS benchmarks for major cloud providers (AWS, Azure, GCP), SOC2 controls, HIPAA requirements, and PCI-DSS compliance standards. The skill supports custom policy authoring in Python using the Checkov BaseCheck and BaseGraphCheck classes for organization-specific rules that inspect individual resources or cross-resource relationships. Graph-based policies detect complex violations like unrestricted security group chains or IAM privilege escalation paths. Results include severity ratings, compliance framework mappings, and guided remediation code fixes. Integration with Prisma Cloud enables centralized policy management across repositories, drift detection between deployed infrastructure and code, and supply chain security analysis of module dependencies.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/)
