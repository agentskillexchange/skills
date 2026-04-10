---
title: "Nango Integration Platform SDK"
description: "Nango is an integration platform for connecting products and agents to hundreds of APIs with managed auth, proxying, and function execution. This skill covers how to use the real Nango project for OAuth-backed integrations, API tool calling, and production sync workflows."
slug: "nango-integration-platform-sdk"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/NangoHQ/nango"
listed: true
---

# Nango Integration Platform SDK

Nango is an integration platform for connecting products and agents to hundreds of APIs with managed auth, proxying, and function execution. This skill covers how to use the real Nango project for OAuth-backed integrations, API tool calling, and production sync workflows.

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
clawhub install nango-integration-platform-sdk
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Nango Integration Platform SDK is anchored to the real Nango project from NangoHQ. Nango is an open source integration platform that helps teams connect products and agents to hundreds of third-party APIs while handling the annoying parts, like OAuth, token refresh, connection management, authenticated proxy requests, and deployable integration functions. In plain terms, it is a serious upstream for anyone building agent actions that need to talk to external SaaS systems in production.
This skill is useful when an agent needs repeatable access to external APIs without hand-rolling auth and connector glue for every provider. A typical implementation uses the @nangohq/node package and Nango runtime to open connection flows, make authenticated requests through Nango’s proxy, and ship TypeScript integration functions that can be reused across customer accounts. That gives agent builders a cleaner path for CRM syncs, ticket creation, outbound actions, data pulls, and multi-tenant integrations where security and lifecycle management matter.
Integration points include AI tool-calling systems, MCP-style API actions, SaaS sync services, support automation, revenue operations tooling, and internal admin workflows. Nango exposes primitives for auth, proxy access, and functions, so it can sit behind an agent layer or operate as the integration engine inside a larger automation platform. The upstream project has a live docs site, npm package, active GitHub repository, published license information, and recent maintenance activity, so it clears the ASE evidence gate without hand-waving. It is a real tool with a concrete job-to-be-done, not a vague integration buzzword.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nango-integration-platform-sdk/)
