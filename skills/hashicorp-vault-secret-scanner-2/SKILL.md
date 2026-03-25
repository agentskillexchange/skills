---
name: "HashiCorp Vault Secret Scanner"
description: "Scans codebases for hardcoded secrets using HashiCorp Vault SDK and truffleHog patterns. Integrates with Vault Transit engine for automatic secret rotation and re-encryption of detected credentials."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/hashicorp-vault-secret-scanner-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "vault"  # from ase_tool_match
  github_stars: 35266  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/vault"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# HashiCorp Vault Secret Scanner

Scans codebases for hardcoded secrets using HashiCorp Vault SDK and truffleHog patterns. Integrates with Vault Transit engine for automatic secret rotation and re-encryption of detected credentials.

## Overview

Scans codebases for hardcoded secrets using HashiCorp Vault SDK and truffleHog patterns. Integrates with Vault Transit engine for automatic secret rotation and re-encryption of detected credentials.

This skill provides automated tooling for hashicorp vault secret scanner workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secret-scanner-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secret-scanner-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secret-scanner-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secret-scanner-2 -a codex
```

### OpenClaw

```bash
clawhub install hashicorp-vault-secret-scanner-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/hashicorp-vault-secret-scanner-2/
