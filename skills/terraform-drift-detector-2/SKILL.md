---
name: "Terraform Drift Detector"
description: "Detect infrastructure drift by comparing Terraform state with live cloud resources using terraform plan and the Terraform Cloud API. Supports AWS, GCP, and Azure provider state analysis."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-drift-detector-2/"
---
# Terraform Drift Detector

Detect infrastructure drift by comparing Terraform state with live cloud resources using terraform plan and the Terraform Cloud API. Supports AWS, GCP, and Azure provider state analysis.

The Terraform Drift Detector skill identifies configuration drift between Terraform-managed infrastructure state and actual cloud resource configurations. It runs terraform plan -detailed-exitcode to detect changes not managed by Terraform, parsing the plan output for resource additions, modifications, and deletions. The skill integrates with Terraform Cloud via the TFC API (workspaces/{id}/runs, state-versions) to access remote state, trigger speculative plans, and compare state versions over time. It supports multi-provider drift detection across AWS (using aws_instance, aws_security_group, aws_iam_role resources), GCP (google_compute_instance, google_project_iam_member), and Azure (azurerm_virtual_machine, azurerm_network_security_group). The detector generates drift reports categorized by severity—critical for security group changes, high for IAM modifications, medium for compute configuration changes—and correlates drift with CloudTrail/Audit Log events to identify the source of out-of-band changes. It supports workspace-level scanning across Terraform Cloud organizations and can trigger remediation runs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-drift-detector-2 -a codex
```

### OpenClaw

```bash
clawhub install terraform-drift-detector-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-drift-detector-2/)
