---
name: "WordPress Content Optimizer"
description: "Optimizes WordPress posts for SEO using the Yoast SEO REST API fields alongside WP REST API v2 for content updates. Analyzes readability via textstat Python library and generates meta descriptions with Claude API prompt chains."
category: "Content Writing & SEO"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wordpress-content-optimizer-yoast-rest/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20976  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# WordPress Content Optimizer

Optimizes WordPress posts for SEO using the Yoast SEO REST API fields alongside WP REST API v2 for content updates. Analyzes readability via textstat Python library and generates meta descriptions with Claude API prompt chains.

## Overview

Optimizes WordPress posts for SEO using the Yoast SEO REST API fields alongside WP REST API v2 for content updates. Analyzes readability via textstat Python library and generates meta descriptions with Claude API prompt chains.

This skill provides a comprehensive automation layer for developers and teams who need reliable, repeatable workflows. It handles authentication, rate limiting, and error recovery automatically, so you can focus on the logic that matters. The agent monitors for changes in real time and applies incremental updates to minimize API calls and reduce latency. Configuration is handled through a simple YAML manifest that defines inputs, outputs, and trigger conditions. Built-in logging captures every action for audit trails and debugging. Supports both interactive and headless modes, making it suitable for CI/CD pipelines as well as local development. The skill includes pre-built templates for common use cases and can be extended with custom plugins. Error handling follows exponential backoff with jitter for transient failures and provides clear diagnostic messages for permanent errors. Compatible with major operating systems and containerized environments. Tested against production workloads with comprehensive integration test suites.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-optimizer-yoast-rest
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-optimizer-yoast-rest -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-optimizer-yoast-rest -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-optimizer-yoast-rest -a codex
```

### OpenClaw

```bash
clawhub install wordpress-content-optimizer-yoast-rest
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wordpress-content-optimizer-yoast-rest/
