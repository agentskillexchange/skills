---
title: "Terraform Plan Diff Analyzer"
description: "Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
---

# Terraform Plan Diff Analyzer

This skill analyzes Terraform plan output to provide human-readable summaries and policy checks before applying infrastructure changes. It parses the JSON output from terraform show -json or retrieves plan artifacts from the Terraform Cloud API using the /api/v2/plans/{id}/json-output endpoint. The skill categorizes resources by action type (create, update, delete, replace) and highlights destructive changes with red-flag annotations. It integrates with Open Policy Agent (OPA) by submitting the plan JSON to a configured OPA policy server or running rego policies locally via the opa eval command. Policy violations block the pipeline and generate detailed reports. The skill supports Terraform workspaces, remote backends, and module-level change summaries. Output formats include Markdown, JSON, and GitHub Pull Request comments via the GitHub Checks API.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/)
