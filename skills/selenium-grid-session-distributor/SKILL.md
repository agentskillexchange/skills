---
title: "Selenium Grid Session Distributor"
description: "Manages browser session allocation across Selenium Grid 4 nodes using the GraphQL status endpoint and SE_NODE_MAX_SESSIONS configuration. Implements weighted round-robin distribution with health-check-based failover for Chrome, Firefox, and Edge instances."
verification: "security_reviewed"
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Session Distributor

Manages browser session allocation across Selenium Grid 4 nodes using the GraphQL status endpoint and SE_NODE_MAX_SESSIONS configuration. Implements weighted round-robin distribution with health-check-based failover for Chrome, Firefox, and Edge instances.

This skill integrates with production-grade tooling to streamline automation workflows. It handles edge cases such as timeout management, retry logic with exponential backoff, and detailed error reporting. Configuration is managed through environment variables and YAML config files, supporting both local development and CI/CD pipeline environments. The skill outputs structured JSON logs compatible with ELK stack and Datadog for observability. It includes built-in rate limiting to respect API quotas and implements proper credential rotation using vault-based secret management.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/selenium-grid-session-distributor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/selenium-grid-session-distributor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/selenium-grid-session-distributor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-distributor/)
