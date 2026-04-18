---
title: "HashiCorp Vault Secret Scanner"
description: "Scans codebases for hardcoded secrets using HashiCorp Vault SDK and truffleHog patterns. Integrates with Vault Transit engine for automatic secret rotation and re-encryption of detected credentials."
verification: security_reviewed
source: "https://github.com/hashicorp/vault"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35418
---

# HashiCorp Vault Secret Scanner

Scans codebases for hardcoded secrets using HashiCorp Vault SDK and truffleHog patterns. Integrates with Vault Transit engine for automatic secret rotation and re-encryption of detected credentials.

This skill provides automated tooling for hashicorp vault secret scanner workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/hashicorp-vault-secret-scanner-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/hashicorp-vault-secret-scanner-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-secret-scanner-2/)
