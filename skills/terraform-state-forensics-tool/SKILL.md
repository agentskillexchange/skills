---
title: "Terraform State Forensics Tool"
description: "Analyzes Terraform state files and plan outputs to detect drift, orphaned resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for security scanning, and Infracost API for cost impact analysis."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
---

# Terraform State Forensics Tool

Analyzes Terraform state files and plan outputs to detect drift, orphaned resources, and dependency cycles. Uses the Terraform CLI state commands, tfsec for security scanning, and Infracost API for cost impact analysis.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-state-forensics-tool
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/terraform-state-forensics-tool` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-state-forensics-tool/)
