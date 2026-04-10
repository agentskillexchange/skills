---
title: "HashiCorp Vault Secret Scanner"
description: "Scans codebases for hardcoded secrets using HashiCorp Vault SDK and truffleHog patterns. Integrates with Vault Transit engine for automatic secret rotation and re-encryption of detected credentials."
slug: "hashicorp-vault-secret-scanner-2"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/hashicorp-vault-secret-scanner-2/"
---

# HashiCorp Vault Secret Scanner

Scans codebases for hardcoded secrets using HashiCorp Vault SDK and truffleHog patterns. Integrates with Vault Transit engine for automatic secret rotation and re-encryption of detected credentials.

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
clawhub install hashicorp-vault-secret-scanner-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill provides automated tooling for hashicorp vault secret scanner workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-secret-scanner-2/)
