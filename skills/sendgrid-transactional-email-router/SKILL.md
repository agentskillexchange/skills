---
name: "SendGrid Transactional Email Router"
description: "Manages transactional email delivery via SendGrid v3 Mail Send API with dynamic template rendering. Handles bounce processing, suppression group management, and event webhook parsing."
category: "Integrations & Connectors"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sendgrid-transactional-email-router/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sendgrid"  # from ase_tool_match
  github_stars: 3054  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3287627  # from ase_npm_downloads
  github_repo: "sendgrid/sendgrid-nodejs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SendGrid Transactional Email Router

Manages transactional email delivery via SendGrid v3 Mail Send API with dynamic template rendering. Handles bounce processing, suppression group management, and event webhook parsing.

## Overview

Manages transactional email delivery via SendGrid v3 Mail Send API with dynamic template rendering. Handles bounce processing, suppression group management, and event webhook parsing.

This skill automates sendgrid transactional email router operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider’s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sendgrid-transactional-email-router
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sendgrid-transactional-email-router -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sendgrid-transactional-email-router -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sendgrid-transactional-email-router -a codex
```

### OpenClaw

```bash
clawhub install sendgrid-transactional-email-router
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sendgrid-transactional-email-router/
