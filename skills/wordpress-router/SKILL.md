---
name: "WordPress Router"
description: "Route WordPress tasks to the right workflow fast. Core Capabilities Manage WordPress sites using WP-CLI and the WordPress REST API Automate plugin, theme, and core update workflows Handle content op"
category: "WordPress & CMS"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wordpress-router/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20976  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# WordPress Router

Route WordPress tasks to the right workflow fast. Core Capabilities Manage WordPress sites using WP-CLI and the WordPress REST API Automate plugin, theme, and core update workflows Handle content op

## Overview

**WordPress Router** is built around WordPress CMS and REST API ecosystem. The underlying ecosystem is represented by `WordPress/WordPress` (20,973+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like posts, pages, taxonomies, media, custom fields, auth, plugin hooks and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to wordpress so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Route WordPress tasks to the right workflow fast. The implementation typically relies on posts, pages, taxonomies, media, custom fields, auth, plugin hooks, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses posts, pages, taxonomies, media, custom fields, auth, plugin hooks instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as content publishing, plugin dev, REST endpoints, and editorial automation.

Key integration points include content publishing, plugin dev, REST endpoints, and editorial automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-router
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-router -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-router -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-router -a codex
```

### OpenClaw

```bash
clawhub install wordpress-router
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wordpress-router/
