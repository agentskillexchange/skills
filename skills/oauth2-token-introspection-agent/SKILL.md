---
name: "OAuth2 Token Introspection Agent"
description: "Validates OAuth2 tokens using RFC 7662 introspection endpoints. Integrates with Keycloak, Auth0, and Okta token introspection APIs to verify token claims, scopes, and expiration in real time."
category: "Security & Verification"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/oauth2-token-introspection-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "auth0"  # from ase_tool_match
  npm_weekly_downloads: 1226704  # from ase_npm_downloads
---

# OAuth2 Token Introspection Agent

Validates OAuth2 tokens using RFC 7662 introspection endpoints. Integrates with Keycloak, Auth0, and Okta token introspection APIs to verify token claims, scopes, and expiration in real time.

## Overview

A comprehensive security agent that validates OAuth2 access tokens and refresh tokens using the RFC 7662 Token Introspection specification. Connects to identity providers including Keycloak, Auth0, and Okta via their introspection endpoints. Verifies token claims such as issuer, audience, scope, and expiration. Supports both opaque and JWT tokens with automatic format detection. Includes rate limiting to prevent introspection endpoint abuse, configurable caching of introspection results for performance, and detailed audit logging of all validation decisions. Can be chained with API gateway middleware to enforce token policies before requests reach backend services. Supports multi-tenant configurations with provider-specific introspection endpoint routing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill oauth2-token-introspection-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill oauth2-token-introspection-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill oauth2-token-introspection-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill oauth2-token-introspection-agent -a codex
```

### OpenClaw

```bash
clawhub install oauth2-token-introspection-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/oauth2-token-introspection-agent/
