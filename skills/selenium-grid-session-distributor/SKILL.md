---
name: "Selenium Grid Session Distributor"
description: "Manages browser session allocation across Selenium Grid 4 nodes using the GraphQL status endpoint and SE_NODE_MAX_SESSIONS configuration. Implements weighted round-robin distribution with health-check-based failover for Chrome, Firefox, and Edge instances."
category: "Browser Automation"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/selenium-grid-session-distributor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "selenium"  # from ase_tool_match
  github_stars: 34174  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2000657  # from ase_npm_downloads
  github_repo: "SeleniumHQ/selenium"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Selenium Grid Session Distributor

Manages browser session allocation across Selenium Grid 4 nodes using the GraphQL status endpoint and SE_NODE_MAX_SESSIONS configuration. Implements weighted round-robin distribution with health-check-based failover for Chrome, Firefox, and Edge instances.

## Overview

Manages browser session allocation across Selenium Grid 4 nodes using the GraphQL status endpoint and SE_NODE_MAX_SESSIONS configuration. Implements weighted round-robin distribution with health-check-based failover for Chrome, Firefox, and Edge instances.

This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-distributor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-distributor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-distributor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-distributor -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-session-distributor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/selenium-grid-session-distributor/
