---
name: Terraform State Inspector
description: Inspects and diagnoses Terraform state files using terraform CLI commands
  and the Terraform Cloud API v2. Detects drift, orphaned resources, and dependency
  cycles in state data.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-inspector/)
