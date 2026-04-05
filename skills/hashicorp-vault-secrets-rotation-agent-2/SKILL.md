---
name: "HashiCorp Vault Secrets Rotation Agent"
description: "Automates secret rotation in HashiCorp Vault using the Vault API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token generation with TTL policies."
category: "Security &amp; Verification"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/hashicorp-vault-secrets-rotation-agent-2/"
---
# HashiCorp Vault Secrets Rotation Agent

Automates secret rotation in HashiCorp Vault using the Vault API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token generation with TTL policies.

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

## Details

The HashiCorp Vault Secrets Rotation Agent skill manages the complete lifecycle of secrets and credentials through the HashiCorp Vault HTTP API. It configures dynamic secrets engines for databases (PostgreSQL, MySQL, MongoDB), cloud providers (AWS STS, GCP service accounts, Azure AD), and PKI certificate authorities. The skill implements automatic credential rotation based on configurable TTL policies, ensuring no static long-lived credentials exist in production environments. Database credential leases are monitored and renewed or rotated before expiration to prevent application downtime. PKI certificates are automatically renewed with proper Subject Alternative Names and key usage extensions. The skill manages Vault policies using HCL syntax, configures authentication methods (Kubernetes auth, AppRole, OIDC), and implements response wrapping for secure secret delivery to applications. Audit logging tracks all secret access patterns for compliance and security review. Integration with Kubernetes external-secrets-operator synchronizes Vault secrets into Kubernetes Secret resources.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-secrets-rotation-agent-2/)
