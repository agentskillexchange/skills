---
title: "OAuth2 Flow Debugger"
description: "Inspects and debugs OAuth 2.0 authorization flows including PKCE, client credentials, and device code grants. Uses jose JWT library and node-fetch to validate tokens, decode claims, and trace redirect chains."
slug: "oauth2-flow-debugger"
category:
  - "Security &amp; Verification"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/oauth2-flow-debugger/"
listed: true
---

# OAuth2 Flow Debugger

Inspects and debugs OAuth 2.0 authorization flows including PKCE, client credentials, and device code grants. Uses jose JWT library and node-fetch to validate tokens, decode claims, and trace redirect chains.

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
clawhub install oauth2-flow-debugger
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OAuth2 Flow Debugger provides comprehensive inspection and debugging of OAuth 2.0 authorization flows across all grant types. It supports Authorization Code with PKCE, Client Credentials, Device Code, and Implicit flows with step-by-step tracing of each protocol exchange. Using the jose library, it decodes and validates JWT access tokens and ID tokens, checking signature algorithms (RS256, ES256, EdDSA), expiration times, audience claims, and issuer validation against OIDC discovery endpoints. The tool uses node-fetch to trace HTTP redirect chains during authorization, logging each 302 redirect with headers and query parameters for debugging misconfigured callback URLs. It validates PKCE code_verifier and code_challenge pairs using S256 transformation, catching common implementation errors. For client credentials flows, it inspects token endpoint authentication methods including client_secret_basic, client_secret_post, and private_key_jwt. The debugger also tests token refresh flows, introspection endpoints (RFC 7662), and revocation endpoints (RFC 7009) with detailed request/response logging.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/oauth2-flow-debugger/)
