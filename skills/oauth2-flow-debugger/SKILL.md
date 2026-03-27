---
name: "OAuth2 Flow Debugger"
description: "Inspects and debugs OAuth 2.0 authorization flows including PKCE, client credentials, and device code grants. Uses jose JWT library and node-fetch to validate tokens, decode claims, and trace redirect chains."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/oauth2-flow-debugger/"
---

# OAuth2 Flow Debugger

Inspects and debugs OAuth 2.0 authorization flows including PKCE, client credentials, and device code grants. Uses jose JWT library and node-fetch to validate tokens, decode claims, and trace redirect chains.

## Overview

The OAuth2 Flow Debugger provides comprehensive inspection and debugging of OAuth 2.0 authorization flows across all grant types. It supports Authorization Code with PKCE, Client Credentials, Device Code, and Implicit flows with step-by-step tracing of each protocol exchange. Using the jose library, it decodes and validates JWT access tokens and ID tokens, checking signature algorithms (RS256, ES256, EdDSA), expiration times, audience claims, and issuer validation against OIDC discovery endpoints. The tool uses node-fetch to trace HTTP redirect chains during authorization, logging each 302 redirect with headers and query parameters for debugging misconfigured callback URLs. It validates PKCE code_verifier and code_challenge pairs using S256 transformation, catching common implementation errors. For client credentials flows, it inspects token endpoint authentication methods including client_secret_basic, client_secret_post, and private_key_jwt. The debugger also tests token refresh flows, introspection endpoints (RFC 7662), and revocation endpoints (RFC 7009) with detailed request/response logging.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill oauth2-flow-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill oauth2-flow-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill oauth2-flow-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill oauth2-flow-debugger -a codex
```

### OpenClaw

```bash
clawhub install oauth2-flow-debugger
```

## Source

- Marketplace: https://agentskillexchange.com/skills/oauth2-flow-debugger/
