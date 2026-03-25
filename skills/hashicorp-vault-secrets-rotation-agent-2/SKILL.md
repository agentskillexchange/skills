---
name: "HashiCorp Vault Secrets Rotation Agent"
description: "Automates secret rotation in HashiCorp Vault using the Vault API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token generation with TTL policies."
category: "Security & Verification"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/hashicorp-vault-secrets-rotation-agent-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "vault"  # from ase_tool_match
  github_stars: 35266  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/vault"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# HashiCorp Vault Secrets Rotation Agent

Automates secret rotation in HashiCorp Vault using the Vault API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token generation with TTL policies.

## Overview

The HashiCorp Vault Secrets Rotation Agent skill manages the complete lifecycle of secrets and credentials through the HashiCorp Vault HTTP API. It configures dynamic secrets engines for databases (PostgreSQL, MySQL, MongoDB), cloud providers (AWS STS, GCP service accounts, Azure AD), and PKI certificate authorities. The skill implements automatic credential rotation based on configurable TTL policies, ensuring no static long-lived credentials exist in production environments. Database credential leases are monitored and renewed or rotated before expiration to prevent application downtime. PKI certificates are automatically renewed with proper Subject Alternative Names and key usage extensions. The skill manages Vault policies using HCL syntax, configures authentication methods (Kubernetes auth, AppRole, OIDC), and implements response wrapping for secure secret delivery to applications. Audit logging tracks all secret access patterns for compliance and security review. Integration with Kubernetes external-secrets-operator synchronizes Vault secrets into Kubernetes Secret resources.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secrets-rotation-agent-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secrets-rotation-agent-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secrets-rotation-agent-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secrets-rotation-agent-2 -a codex
```

### OpenClaw

```bash
clawhub install hashicorp-vault-secrets-rotation-agent-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/hashicorp-vault-secrets-rotation-agent-2/
