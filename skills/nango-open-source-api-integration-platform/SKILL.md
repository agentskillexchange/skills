---
name: Nango Open Source API Integration Platform
description: Nango is an open-source platform for building product integrations with
  700+ APIs. It handles OAuth, token management, API proxying, and execution of custom
  TypeScript sync and action logic on managed infrastructure.
verification: security_reviewed
source: https://github.com/NangoHQ/nango
category:
- Integrations &amp; Connectors
framework:
- Custom Agents
tool_ecosystem:
  github_repo: NangoHQ/nango
  github_stars: 7003
  ase_npm_package: nango
  npm_weekly_downloads: 14801
---
# Nango Open Source API Integration Platform

Nango is an open-source integration platform that provides the infrastructure for connecting your product to over 700 external APIs. Built in TypeScript and available on npm as @nangohq/node, Nango abstracts away the complexity of OAuth flows, credential storage, token refresh, rate limiting, and retry logic — the tedious plumbing that makes API integrations fragile and time-consuming to maintain. With nearly 7,000 GitHub stars and production use at companies like Replit and Ramp, Nango has proven itself as serious integration infrastructure.
The platform offers three core primitives. First, managed authentication: embed a white-label OAuth flow in your frontend using nango.openConnectUI(), and Nango handles the entire auth dance, credential storage, and automatic token refresh for each of your users' connections. Second, an API proxy: make authenticated requests to any supported API through Nango's proxy layer, which automatically resolves the provider, injects the right credentials, handles retries on transient failures, and respects rate limits. Third, custom integration logic: write TypeScript functions (syncs and actions) that run on Nango's managed runtime with built-in observability, storage, and scheduling.
Nango supports every common integration pattern including two-way data syncing for RAG pipelines and indexing, webhook processing from external APIs, API unification with custom schemas, AI tool calling and MCP server exposure, and per-customer configuration. The platform can be self-hosted or used as a managed cloud service. Integration scripts are version-controlled and deployed through a CLI, and the AI builder can generate integration code from natural language descriptions of your use case.
For agent developers, Nango is particularly valuable as a connector layer. Rather than hand-rolling OAuth flows and API clients for each service your agent needs to interact with, Nango provides a unified interface. The platform's built-in support for MCP means agent frameworks can leverage Nango's 700+ API connections as tool endpoints, with authentication and error handling already solved.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nango-open-source-api-integration-platform/)
