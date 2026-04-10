---
title: "Hanko Open Source Passkey Authentication and User Management"
description: "Hanko is an open-source authentication and user management platform built on passkeys and WebAuthn. It provides a drop-in authentication solution as an alternative to Auth0, Clerk, and Stytch, with pre-built web components, a REST API, and an admin dashboard."
slug: "hanko-passkey-authentication-platform"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/teamhanko/hanko"
tool_ecosystem:
  github_repo: "teamhanko/hanko"
  github_stars: 8893
listed: true
---

# Hanko Open Source Passkey Authentication and User Management

Hanko is an open-source authentication and user management platform built on passkeys and WebAuthn. It provides a drop-in authentication solution as an alternative to Auth0, Clerk, and Stytch, with pre-built web components, a REST API, and an admin dashboard.

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
clawhub install hanko-passkey-authentication-platform
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Hanko is an open-source authentication and user management solution built on privacy-first principles including data minimalism and phishing resistance through passkeys. It provides a complete authentication backend with a Go-based server, pre-built web components for login flows, and an admin dashboard — designed as a self-hostable alternative to Auth0, Clerk, WorkOS, and Stytch.
How It Works
Hanko consists of a Go backend server that handles all authentication logic (passkey registration/authentication, email verification, session management, user management) and exposes a REST API. The frontend integration uses Hanko Elements — framework-agnostic web components built with the Web Components standard — that provide complete login, registration, and user profile UIs out of the box. Developers embed these components in their app, configure the Hanko backend URL, and get a fully functional passkey-first authentication system.
Key Features
- Passkey-first authentication: Built on FIDO2/WebAuthn standards for phishing-resistant, passwordless login. Users register and authenticate using device biometrics (fingerprint, face ID) or security keys.
- Pre-built web components: Hanko Elements provide drop-in login, registration, and profile management UIs that work with any framework — React, Vue, Angular, Svelte, or plain HTML.
- Flexible auth methods: Supports passkeys, email passcodes, OAuth/OIDC providers (Google, Apple, GitHub, etc.), and combination flows.
- Session management: JWT-based session tokens with configurable expiration, issued via secure cookies or bearer tokens.
- Admin dashboard: Built-in admin UI for user management, authentication method configuration, and monitoring.
- REST API: Full API for user CRUD, session management, passkey management, and webhook configuration.
- Self-hosted or cloud: Deploy via Docker or use Hanko Cloud. No vendor lock-in — data freely migrates between cloud and self-hosted instances.
- Passkey API: A separate FIDO2-certified passkey server and SDK library for adding passkey support to apps with existing auth systems.
Integration Points
Deploy the Hanko backend with Docker: docker run -p 8000:8000 teamhanko/hanko. Install frontend elements via npm: npm install @teamhanko/hanko-elements. Configure the Hanko API URL in your app, embed the <hanko-auth> web component, and authentication is ready. Backend SDKs are available for validating JWTs in your API middleware. The admin dashboard runs alongside the auth server.
Agent Integration
AI agents building web applications can integrate Hanko to add complete authentication flows without implementing auth from scratch. The REST API enables programmatic user management, while the pre-built web components eliminate the need for agents to generate complex authentication UI code. Agents can configure OAuth providers, manage user sessions, and set up webhook listeners for auth events through the API.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hanko-passkey-authentication-platform/)
