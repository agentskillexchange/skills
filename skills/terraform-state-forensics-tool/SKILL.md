---
title: "Terraform State Forensics Tool"
description: "Analyzes Terraform state files and plan outputs to detect drift, orphaned resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for security scanning, and Infracost API for cost impact analysis."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform State Forensics Tool

Analyzes Terraform state files and plan outputs to detect drift, orphaned resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for security scanning, and Infracost API for cost impact analysis.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-state-forensics-tool/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-state-forensics-tool
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-state-forensics-tool`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-forensics-tool/)
