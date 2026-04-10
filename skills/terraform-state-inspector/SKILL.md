---
title: "Terraform State Inspector"
description: "Inspects and diagnoses Terraform state files using terraform CLI commands and the Terraform Cloud API v2. Detects drift, orphaned resources, and dependency cycles in state data."
slug: "terraform-state-inspector"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/terraform-state-inspector/"
---

# Terraform State Inspector

Inspects and diagnoses Terraform state files using terraform CLI commands and the Terraform Cloud API v2. Detects drift, orphaned resources, and dependency cycles in state data.

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
clawhub install terraform-state-inspector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Terraform State Inspector skill provides deep analysis of Terraform infrastructure state for drift detection and troubleshooting. It uses terraform state list and terraform state show commands to enumerate and inspect managed resources. The Terraform Cloud API v2 is leveraged for remote state access, workspace management, and run history analysis. Drift detection compares actual cloud provider state against the stored Terraform state, identifying resources modified outside of Terraform control. Orphaned resource detection finds state entries referencing deleted cloud resources. Dependency cycle analysis examines the resource graph to identify circular dependencies causing plan failures. The skill also validates backend configuration, checks state locking status via DynamoDB or Consul backends, and can generate import blocks for bringing existing infrastructure under Terraform management.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-inspector/)
