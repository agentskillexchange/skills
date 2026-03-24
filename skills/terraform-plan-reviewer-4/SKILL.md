---
name: "Terraform Plan Reviewer"
description: "Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-plan-reviewer-4/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 47996  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform Plan Reviewer

Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries.

## Overview

The Terraform Plan Reviewer skill analyzes Terraform plan output to provide intelligent infrastructure change reviews before apply. It parses the JSON plan format produced by terraform show -json and integrates with the hashicorp/terraform-exec Go SDK for programmatic plan execution. The skill classifies resource changes into categories: creates, updates, destroys, and replacements, flagging potentially destructive operations like database deletions or security group modifications. Integration with the Infracost API provides estimated cost impact for AWS, GCP, and Azure resources before changes are applied. The reviewer generates structured approval summaries with risk scores based on the sensitivity of modified resources, blast radius estimation, and dependency chain analysis. It supports Terraform workspace-aware reviews, module-level change grouping, and state drift detection by comparing plan output against expected configurations. The skill also validates provider version constraints, checks for deprecated resource attributes, and ensures backend configuration consistency. Output formats include Markdown summaries for PR comments, Slack notifications, and structured JSON for integration with custom approval workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-plan-reviewer-4 -a codex
```

### OpenClaw

```bash
clawhub install terraform-plan-reviewer-4
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-plan-reviewer-4/
