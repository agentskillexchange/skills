---
name: HashiCorp Vault Secret Scanner
description: Scans codebases for hardcoded secrets using HashiCorp Vault SDK and truffleHog
  patterns. Integrates with Vault Transit engine for automatic secret rotation and
  re-encryption of detected credentials.
verification: security_reviewed
source: https://agentskillexchange.com/skills/hashicorp-vault-secret-scanner-2/
category:
- Security &amp; Verification
framework:
- Claude Code
---
# HashiCorp Vault Secret Scanner

Scans codebases for hardcoded secrets using HashiCorp Vault SDK and truffleHog patterns. Integrates with Vault Transit engine for automatic secret rotation and re-encryption of detected credentials.
This skill provides automated tooling for hashicorp vault secret scanner workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-secret-scanner-2/)
