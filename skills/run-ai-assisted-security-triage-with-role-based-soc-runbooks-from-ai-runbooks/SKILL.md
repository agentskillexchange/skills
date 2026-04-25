---
title: "Run AI-assisted security triage with role-based SOC runbooks from ai-runbooks"
description: "Use ai-runbooks to give AI assistants role-specific SOC personas, investigation steps, and incident-response procedures for structured security triage."
verification: "security_reviewed"
source: "https://github.com/dandye/ai-runbooks"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dandye/ai-runbooks"
  github_stars: 96
---

# Run AI-assisted security triage with role-based SOC runbooks from ai-runbooks

Use ai-runbooks when the task is to guide an AI assistant through a defined security operations procedure such as alert triage, IOC enrichment, threat hunting, or incident-response handling. The upstream repository is explicit that it provides role-based guides, runbooks, incident plans, and shared rules-bank content for AI-assisted cybersecurity workflows. Invoke this instead of using the product normally when you need a repeatable procedural layer for security work across supported assistants, not just a repository of general security notes. The operator workflow is concrete: choose the relevant persona or runbook, load the shared rules-bank content into the assistant environment, then work the investigation steps in a standardized sequence. The scope boundary is what keeps this publishable as a skill. This is not a generic security platform listing or a vague documentation repo card. It is the bounded workflow of running AI-assisted security triage against structured SOC playbooks and role definitions.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-ai-assisted-security-triage-with-role-based-soc-runbooks-from-ai-runbooks/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-ai-assisted-security-triage-with-role-based-soc-runbooks-from-ai-runbooks
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-ai-assisted-security-triage-with-role-based-soc-runbooks-from-ai-runbooks`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-ai-assisted-security-triage-with-role-based-soc-runbooks-from-ai-runbooks/)
