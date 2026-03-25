---
name: "WordPress Content Publisher"
description: "Structured publishing workflow for WordPress drafts, metadata, and content operations."
category: "WordPress & CMS"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wordpress-content-publisher/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20976  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# WordPress Content Publisher

Structured publishing workflow for WordPress drafts, metadata, and content operations.

## Overview

**WordPress Content Publisher** is built around WordPress CMS and REST API ecosystem. The underlying ecosystem is represented by `WordPress/WordPress` (20,973+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like posts, pages, taxonomies, media, custom fields, auth, plugin hooks and preserving the operational context that matters for real tasks.

For content workflows, the skill uses wordpress primitives as the system of record, so an agent can read structured inputs, apply transformations, and publish or sync output without losing metadata, IDs, or status fields. The original use case is clear: Structured publishing workflow for WordPress drafts, metadata, and content operations. The implementation typically relies on posts, pages, taxonomies, media, custom fields, auth, plugin hooks, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses posts, pages, taxonomies, media, custom fields, auth, plugin hooks instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as content publishing, plugin dev, REST endpoints, and editorial automation.

Key integration points include content publishing, plugin dev, REST endpoints, and editorial automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-publisher
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-publisher -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-publisher -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-publisher -a codex
```

### OpenClaw

```bash
clawhub install wordpress-content-publisher
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wordpress-content-publisher/
