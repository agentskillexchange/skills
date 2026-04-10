---
title: "HashiCorp Vault Secrets Rotation Agent"
description: "Automates secret rotation in HashiCorp Vault using the Vault API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token generation with TTL policies."
slug: "hashicorp-vault-secrets-rotation-agent-2"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/hashicorp-vault-secrets-rotation-agent-2/"
listed: true
---

# HashiCorp Vault Secrets Rotation Agent

Automates secret rotation in HashiCorp Vault using the Vault API and dynamic secrets engines. Manages database credential leases, PKI certificate renewal, and AWS STS token generation with TTL policies.

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
clawhub install hashicorp-vault-secrets-rotation-agent-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The HashiCorp Vault Secrets Rotation Agent skill manages the complete lifecycle of secrets and credentials through the HashiCorp Vault HTTP API. It configures dynamic secrets engines for databases (PostgreSQL, MySQL, MongoDB), cloud providers (AWS STS, GCP service accounts, Azure AD), and PKI certificate authorities. The skill implements automatic credential rotation based on configurable TTL policies, ensuring no static long-lived credentials exist in production environments. Database credential leases are monitored and renewed or rotated before expiration to prevent application downtime. PKI certificates are automatically renewed with proper Subject Alternative Names and key usage extensions. The skill manages Vault policies using HCL syntax, configures authentication methods (Kubernetes auth, AppRole, OIDC), and implements response wrapping for secure secret delivery to applications. Audit logging tracks all secret access patterns for compliance and security review. Integration with Kubernetes external-secrets-operator synchronizes Vault secrets into Kubernetes Secret resources.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-secrets-rotation-agent-2/)
