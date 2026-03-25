---
name: "Selenium Grid Session Manager"
description: "Manages distributed browser sessions on Selenium Grid 4 via the GraphQL API and /status endpoint. Handles node scaling, session queuing, and capability matching for parallel test execution."
category: "Browser Automation"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/selenium-grid-session-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "selenium"  # from ase_tool_match
  github_stars: 34174  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2000657  # from ase_npm_downloads
  github_repo: "SeleniumHQ/selenium"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Selenium Grid Session Manager

Manages distributed browser sessions on Selenium Grid 4 via the GraphQL API and /status endpoint. Handles node scaling, session queuing, and capability matching for parallel test execution.

## Overview

The Selenium Grid Session Manager orchestrates distributed browser testing infrastructure using Selenium Grid 4’s modern architecture. It communicates with the Grid via the GraphQL API endpoint (/graphql) for detailed session and node information, and the /status REST endpoint for health monitoring.

The skill handles dynamic node registration and capability matching, ensuring test sessions are routed to nodes with the correct browser version, platform, and custom capabilities. It manages session queuing with configurable timeout and retry policies, preventing queue overflow during peak testing periods.

Advanced features include automatic node scaling based on queue depth (integrating with Docker API for container-based nodes), session video recording via Selenium Video docker images, and VNC live-view connections for debugging. The manager tracks session lifecycle events (created, assigned, completed, failed) and generates utilization dashboards. It supports both hub-node and fully distributed Grid architectures, with health checks that automatically drain unhealthy nodes and redistribute pending sessions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-manager -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-session-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/selenium-grid-session-manager/
