---
name: "Verify shared and private fleet memory through Caura MCP"
slug: "verify-shared-and-private-fleet-memory-through-caura-mcp"
description: "Use two provisioned agent identities to check fleet recall, private-memory boundaries and writer provenance before connecting a team to shared memory."
github_stars: 559
verification: "security_reviewed"
source: "https://github.com/caura-ai/caura"
author: "caura-ai"
publisher_type: "Community"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "caura-ai/caura"
  github_stars: 559
  npm_package: "@caura/client"
  npm_weekly_downloads: 0
---

# Verify shared and private fleet memory through Caura MCP

Use two provisioned agent identities to check fleet recall, private-memory boundaries and writer provenance before connecting a team to shared memory.

## Prerequisites

Two MCP Streamable HTTP clients, an existing Caura service with independent agent credentials, HTTP client for whoami, authorized test tenant and fleet

## Installation

Install or set up from the source-backed instructions:

Use an existing managed or self-hosted Caura service that supports the required authenticated agent identities. Configure each MCP client with that service HTTPS /mcp URL and its separate protected X-API-Key or Bearer credential. Confirm identity through /api/v1/whoami before test writes. Upstream self-hosting instructions are at https://github.com/caura-ai/caura/blob/main/docs/self-hosting.md; do not use keyless standalone mode to validate identity isolation. No npm package is required for this MCP path.

- Source: https://github.com/caura-ai/caura

## Documentation

- https://github.com/caura-ai/caura/blob/main/docs/agent-fleet-memory.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-shared-and-private-fleet-memory-through-caura-mcp/)
