---
title: "Casdoor Open Source Identity and Access Management Platform"
description: "Casdoor is an open source AI-first Identity and Access Management (IAM) platform and auth server supporting OAuth 2.1, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, and MCP gateway integration with a web-based admin UI."
slug: "casdoor-open-source-iam-auth-platform"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/casdoor/casdoor"
tool_ecosystem:
  github_repo: "casdoor/casdoor"
  github_stars: 13316
---

# Casdoor Open Source Identity and Access Management Platform

Casdoor is an open source AI-first Identity and Access Management (IAM) platform and auth server supporting OAuth 2.1, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, and MCP gateway integration with a web-based admin UI.

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
clawhub install casdoor-open-source-iam-auth-platform
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Casdoor is an open source Identity and Access Management (IAM) platform developed by the Casbin organization. It provides a complete authentication and authorization server with a built-in web UI for managing users, organizations, applications, providers, and permissions. Casdoor supports a wide range of authentication protocols and identity providers out of the box.
Supported Protocols and Features
- Authentication protocols: OAuth 2.1, OpenID Connect (OIDC), SAML 2.0, CAS 3.0, LDAP, SCIM
- MFA methods: TOTP, SMS, Email, WebAuthn/FIDO2, Face ID
- Identity providers: Google Workspace, Azure AD, GitHub, GitLab, Facebook, and 100+ third-party OAuth providers
- AI gateway: MCP (Model Context Protocol) and A2A (Agent-to-Agent) gateway support for AI agent authentication
- User management: Registration, login, profile management, role-based access control, organization multi-tenancy
Architecture
Casdoor is built with Go (backend) and React (frontend). It stores data in MySQL, PostgreSQL, SQL Server, or SQLite. The platform exposes a comprehensive REST API and provides official SDKs for Go, Java, Node.js, Python, PHP, .NET, Rust, Dart, and Swift.
Key Capabilities
- Single Sign-On (SSO): Centralized authentication across multiple applications
- Multi-tenancy: Manage multiple organizations with isolated user pools
- Customizable login pages: Theme and brand the login experience per application
- Webhook and syncer: Sync user data from external databases and trigger webhooks on events
- Public API: Full REST API with Swagger documentation at /swagger
Agent Integration
Agents can use Casdoor to manage authentication flows, provision users, configure identity providers, and handle access tokens programmatically via the REST API. The MCP gateway support makes it particularly relevant for AI agent ecosystems that need secure identity management. Official SDKs are available on npm (casdoor-nodejs-sdk), PyPI (casdoor-python-sdk), and Go modules.
Installation
# Docker
docker pull casbin/casdoor
docker run -p 8000:8000 casbin/casdoor
Or build from source:
go get github.com/casdoor/casdoor
cd casdoor && go build

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/casdoor-open-source-iam-auth-platform/)
