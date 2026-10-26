---
name: "Preflight Nudgebee runbooks before saving or execution"
slug: "preflight-nudgebee-runbooks-before-saving-or-execution"
description: "Validate a proposed Nudgebee runbook, repair supported schema errors, and return an operator review packet without saving, activating or executing it."
github_stars: 520
verification: "security_reviewed"
source: "https://github.com/nudgebee/nudgebee"
author: "Nudgebee"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "nudgebee/nudgebee"
  github_stars: 520
---

# Preflight Nudgebee runbooks before saving or execution

Validate a proposed Nudgebee runbook, repair supported schema errors, and return an operator review packet without saving, activating or executing it.

## Prerequisites

HTTP client; JSON/YAML parser; existing operator-managed Nudgebee runbook service with an approved authenticated gateway or protected internal connection

## Installation

Install or set up from the source-backed instructions:

Use an existing operator-managed Nudgebee deployment and its approved connection; this procedure does not install or expose the platform. Confirm the deployed Workflow schema, GET /tasks and POST /workflows/validate interfaces against the pinned documentation. Supply only operator-authorized tenant, user and account context using the deployment connection. No standalone npm package or upstream packaged skill is claimed.

- Source: https://github.com/nudgebee/nudgebee

## Documentation

- https://github.com/nudgebee/nudgebee/blob/106871af75c2ef2ffe041561712071c112b2189c/runbook-server/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/preflight-nudgebee-runbooks-before-saving-or-execution/)
