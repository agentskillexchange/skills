---
title: Checkov Infrastructure Policy Scanner
description: The Checkov Infrastructure Policy Scanner skill enforces security and
  compliance policies across Infrastructure-as-Code repositories using the Bridgecrew
  Checkov static analysis engine. It scans Terraform HCL and plan files, AWS CloudFormation
  templates, Kubernetes manifests, Helm charts, Dockerfiles, and Serverless Framework
  configurations for misconfigurations and policy violations. Built-in policies cover
  CIS benchmarks for major cloud providers (AWS, Azure, GCP), SOC2 controls, HIPAA
  requirements, and PCI-DSS compliance standards. The skill supports custom policy
  authoring in Python using the Checkov BaseCheck and BaseGraphCheck classes for organization-specific
  rules that inspect individual resources or cross-resource relationships. Graph-based
  policies detect complex violations like unrestricted security group chains or IAM
  privilege escalation paths. Results include severity ratings, compliance framework
  mappings, and guided remediation code fixes. Integration with Prisma Cloud enables
  centralized policy management across repositories, drift detection between deployed
  infrastructure and code, and supply chain security analysis of module dependencies.
verification: security_reviewed
source: https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/
category:
- Security &amp; Verification
framework:
- Codex
---

# Checkov Infrastructure Policy Scanner

The Checkov Infrastructure Policy Scanner skill enforces security and compliance policies across Infrastructure-as-Code repositories using the Bridgecrew Checkov static analysis engine. It scans Terraform HCL and plan files, AWS CloudFormation templates, Kubernetes manifests, Helm charts, Dockerfiles, and Serverless Framework configurations for misconfigurations and policy violations. Built-in policies cover CIS benchmarks for major cloud providers (AWS, Azure, GCP), SOC2 controls, HIPAA requirements, and PCI-DSS compliance standards. The skill supports custom policy authoring in Python using the Checkov BaseCheck and BaseGraphCheck classes for organization-specific rules that inspect individual resources or cross-resource relationships. Graph-based policies detect complex violations like unrestricted security group chains or IAM privilege escalation paths. Results include severity ratings, compliance framework mappings, and guided remediation code fixes. Integration with Prisma Cloud enables centralized policy management across repositories, drift detection between deployed infrastructure and code, and supply chain security analysis of module dependencies.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/)
