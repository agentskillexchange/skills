---
title: "HashiCorp Vault Secrets Rotation Agent"
description: "The HashiCorp Vault Secrets Rotation Agent skill manages the complete lifecycle of secrets and credentials through the HashiCorp Vault HTTP API. It configures dynamic secrets engines for databases (PostgreSQL, MySQL, MongoDB), cloud providers (AWS STS, GCP service accounts, Azure AD), and PKI certificate authorities. The skill implements automatic credential rotation based on configurable TTL policies, ensuring no static long-lived credentials exist in production environments. Database credential leases are monitored and renewed or rotated before expiration to prevent application downtime. PKI certificates are automatically renewed with proper Subject Alternative Names and key usage extensions. The skill manages Vault policies using HCL syntax, configures authentication methods (Kubernetes auth, AppRole, OIDC), and implements response wrapping for secure secret delivery to applications. Audit logging tracks all secret access patterns for compliance and security review. Integration with Kubernetes external-secrets-operator synchronizes Vault secrets into Kubernetes Secret resources."
verification: security_reviewed
source: "https://github.com/hashicorp/vault"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35418
---

# HashiCorp Vault Secrets Rotation Agent

The HashiCorp Vault Secrets Rotation Agent skill manages the complete lifecycle of secrets and credentials through the HashiCorp Vault HTTP API. It configures dynamic secrets engines for databases (PostgreSQL, MySQL, MongoDB), cloud providers (AWS STS, GCP service accounts, Azure AD), and PKI certificate authorities. The skill implements automatic credential rotation based on configurable TTL policies, ensuring no static long-lived credentials exist in production environments. Database credential leases are monitored and renewed or rotated before expiration to prevent application downtime. PKI certificates are automatically renewed with proper Subject Alternative Names and key usage extensions. The skill manages Vault policies using HCL syntax, configures authentication methods (Kubernetes auth, AppRole, OIDC), and implements response wrapping for secure secret delivery to applications. Audit logging tracks all secret access patterns for compliance and security review. Integration with Kubernetes external-secrets-operator synchronizes Vault secrets into Kubernetes Secret resources.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/hashicorp-vault-secrets-rotation-agent-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/hashicorp-vault-secrets-rotation-agent-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-secrets-rotation-agent-2/)
