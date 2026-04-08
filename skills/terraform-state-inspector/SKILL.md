---
title: Terraform State Inspector
description: The Terraform State Inspector skill provides deep analysis of Terraform
  infrastructure state for drift detection and troubleshooting. It uses terraform
  state list and terraform state show commands to enumerate and inspect managed resources.
  The Terraform Cloud API v2 is leveraged for remote state access, workspace management,
  and run history analysis. Drift detection compares actual cloud provider state against
  the stored Terraform state, identifying resources modified outside of Terraform
  control. Orphaned resource detection finds state entries referencing deleted cloud
  resources. Dependency cycle analysis examines the resource graph to identify circular
  dependencies causing plan failures. The skill also validates backend configuration,
  checks state locking status via DynamoDB or Consul backends, and can generate import
  blocks for bringing existing infrastructure under Terraform management.
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-state-inspector/
category:
- Runbooks &amp; Diagnostics
framework:
- Gemini
---

# Terraform State Inspector

The Terraform State Inspector skill provides deep analysis of Terraform infrastructure state for drift detection and troubleshooting. It uses terraform state list and terraform state show commands to enumerate and inspect managed resources. The Terraform Cloud API v2 is leveraged for remote state access, workspace management, and run history analysis. Drift detection compares actual cloud provider state against the stored Terraform state, identifying resources modified outside of Terraform control. Orphaned resource detection finds state entries referencing deleted cloud resources. Dependency cycle analysis examines the resource graph to identify circular dependencies causing plan failures. The skill also validates backend configuration, checks state locking status via DynamoDB or Consul backends, and can generate import blocks for bringing existing infrastructure under Terraform management.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-inspector/)
