---
title: "Checkov Infrastructure Policy Scanner"
description: "Scans IaC files with Bridgecrew Checkov for policy violations across Terraform, CloudFormation, Kubernetes, and Dockerfile configurations. Supports custom Python-based policy authoring and Prisma Cloud integration."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
---

# Checkov Infrastructure Policy Scanner

The Checkov Infrastructure Policy Scanner skill enforces security and compliance policies across Infrastructure-as-Code repositories using the Bridgecrew Checkov static analysis engine. It scans Terraform HCL and plan files, AWS CloudFormation templates, Kubernetes manifests, Helm charts, Dockerfiles, and Serverless Framework configurations for misconfigurations and policy violations. Built-in policies cover CIS benchmarks for major cloud providers (AWS, Azure, GCP), SOC2 controls, HIPAA requirements, and PCI-DSS compliance standards. The skill supports custom policy authoring in Python using the Checkov BaseCheck and BaseGraphCheck classes for organization-specific rules that inspect individual resources or cross-resource relationships. Graph-based policies detect complex violations like unrestricted security group chains or IAM privilege escalation paths. Results include severity ratings, compliance framework mappings, and guided remediation code fixes. Integration with Prisma Cloud enables centralized policy management across repositories, drift detection between deployed infrastructure and code, and supply chain security analysis of module dependencies.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/)
