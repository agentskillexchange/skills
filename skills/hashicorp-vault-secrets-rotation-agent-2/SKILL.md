---
title: "HashiCorp Vault Secrets Rotation Agent"
description: "The HashiCorp Vault Secrets Rotation Agent skill manages the complete lifecycle of secrets and credentials through the HashiCorp Vault HTTP API. It configures dynamic secrets engines for databases (PostgreSQL, MySQL, MongoDB), cloud providers (AWS STS, GCP service accounts, Azure AD), and PKI certificate authorities. The skill implements automatic credential rotation based on configurable TTL policies, ensuring no static long-lived credentials exist in production environments. Database credential leases are monitored and renewed or rotated before expiration to prevent application downtime. PKI certificates are automatically renewed with proper Subject Alternative Names and key usage extensions. The skill manages Vault policies using HCL syntax, configures authentication methods (Kubernetes auth, AppRole, OIDC), and implements response wrapping for secure secret delivery to applications. Audit logging tracks all secret access patterns for compliance and security review. Integration with Kubernetes external-secrets-operator synchronizes Vault secrets into Kubernetes Secret resources."
source: "https://github.com/hashicorp/vault"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35418
---

# HashiCorp Vault Secrets Rotation Agent

The HashiCorp Vault Secrets Rotation Agent skill manages the complete lifecycle of secrets and credentials through the HashiCorp Vault HTTP API. It configures dynamic secrets engines for databases (PostgreSQL, MySQL, MongoDB), cloud providers (AWS STS, GCP service accounts, Azure AD), and PKI certificate authorities. The skill implements automatic credential rotation based on configurable TTL policies, ensuring no static long-lived credentials exist in production environments. Database credential leases are monitored and renewed or rotated before expiration to prevent application downtime. PKI certificates are automatically renewed with proper Subject Alternative Names and key usage extensions. The skill manages Vault policies using HCL syntax, configures authentication methods (Kubernetes auth, AppRole, OIDC), and implements response wrapping for secure secret delivery to applications. Audit logging tracks all secret access patterns for compliance and security review. Integration with Kubernetes external-secrets-operator synchronizes Vault secrets into Kubernetes Secret resources.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-secrets-rotation-agent-2/)
