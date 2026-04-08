---
title: HashiCorp Vault Secrets Rotation Agent
description: The HashiCorp Vault Secrets Rotation Agent skill manages the complete
  lifecycle of secrets and credentials through the HashiCorp Vault HTTP API. It configures
  dynamic secrets engines for databases (PostgreSQL, MySQL, MongoDB), cloud providers
  (AWS STS, GCP service accounts, Azure AD), and PKI certificate authorities. The
  skill implements automatic credential rotation based on configurable TTL policies,
  ensuring no static long-lived credentials exist in production environments. Database
  credential leases are monitored and renewed or rotated before expiration to prevent
  application downtime. PKI certificates are automatically renewed with proper Subject
  Alternative Names and key usage extensions. The skill manages Vault policies using
  HCL syntax, configures authentication methods (Kubernetes auth, AppRole, OIDC),
  and implements response wrapping for secure secret delivery to applications. Audit
  logging tracks all secret access patterns for compliance and security review. Integration
  with Kubernetes external-secrets-operator synchronizes Vault secrets into Kubernetes
  Secret resources.
verification: security_reviewed
source: https://agentskillexchange.com/skills/hashicorp-vault-secrets-rotation-agent-2/
category:
- Security &amp; Verification
framework:
- MCP
---

# HashiCorp Vault Secrets Rotation Agent

The HashiCorp Vault Secrets Rotation Agent skill manages the complete lifecycle of secrets and credentials through the HashiCorp Vault HTTP API. It configures dynamic secrets engines for databases (PostgreSQL, MySQL, MongoDB), cloud providers (AWS STS, GCP service accounts, Azure AD), and PKI certificate authorities. The skill implements automatic credential rotation based on configurable TTL policies, ensuring no static long-lived credentials exist in production environments. Database credential leases are monitored and renewed or rotated before expiration to prevent application downtime. PKI certificates are automatically renewed with proper Subject Alternative Names and key usage extensions. The skill manages Vault policies using HCL syntax, configures authentication methods (Kubernetes auth, AppRole, OIDC), and implements response wrapping for secure secret delivery to applications. Audit logging tracks all secret access patterns for compliance and security review. Integration with Kubernetes external-secrets-operator synchronizes Vault secrets into Kubernetes Secret resources.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-secrets-rotation-agent-2/)
