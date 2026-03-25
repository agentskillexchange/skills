---
name: "Supabase MCP Server"
description: "Supabase MCP Server is built around Supabase developer platform. The underlying ecosystem is represented by supabase/supabase (99,546+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like PostgREST, Auth, Storage, Realtime, Edge Functions, RLS and preserving the operational context […]"
category: "Developer Tools"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/supabase-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "supabase"  # from ase_tool_match
  github_stars: 99546  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 14597348  # from ase_npm_downloads
  github_repo: "supabase/supabase"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Supabase MCP Server

Supabase MCP Server is built around Supabase developer platform. The underlying ecosystem is represented by supabase/supabase (99,546+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like PostgREST, Auth, Storage, Realtime, Edge Functions, RLS and preserving the operational context […]

## Overview

**Supabase MCP Server** is built around Supabase developer platform. The underlying ecosystem is represented by `supabase/supabase` (99,546+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like PostgREST, Auth, Storage, Realtime, Edge Functions, RLS and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to supabase so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on PostgREST, Auth, Storage, Realtime, Edge Functions, RLS, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses PostgREST, Auth, Storage, Realtime, Edge Functions, RLS instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as backend-as-a-service, database APIs, auth flows, and realtime apps.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include backend-as-a-service, database APIs, auth flows, and realtime apps. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill supabase-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill supabase-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill supabase-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill supabase-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install supabase-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/supabase-mcp-server/
