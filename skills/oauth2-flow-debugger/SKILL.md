---
title: "OAuth2 Flow Debugger"
description: "Inspects and debugs OAuth 2.0 authorization flows including PKCE, client credentials, and device code grants. Uses jose JWT library and node-fetch to validate tokens, decode claims, and trace redirect chains."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/oauth2-flow-debugger/"
category:
  - "Security & Verification"
framework:
  - "ChatGPT Agents"
---

# OAuth2 Flow Debugger

The OAuth2 Flow Debugger provides comprehensive inspection and debugging of OAuth 2.0 authorization flows across all grant types. It supports Authorization Code with PKCE, Client Credentials, Device Code, and Implicit flows with step-by-step tracing of each protocol exchange. Using the jose library, it decodes and validates JWT access tokens and ID tokens, checking signature algorithms (RS256, ES256, EdDSA), expiration times, audience claims, and issuer validation against OIDC discovery endpoints. The tool uses node-fetch to trace HTTP redirect chains during authorization, logging each 302 redirect with headers and query parameters for debugging misconfigured callback URLs. It validates PKCE code_verifier and code_challenge pairs using S256 transformation, catching common implementation errors. For client credentials flows, it inspects token endpoint authentication methods including client_secret_basic, client_secret_post, and private_key_jwt. The debugger also tests token refresh flows, introspection endpoints (RFC 7662), and revocation endpoints (RFC 7009) with detailed request/response logging.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/oauth2-flow-debugger/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/oauth2-flow-debugger
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/oauth2-flow-debugger`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/oauth2-flow-debugger/)
