---
title: "Selenium Grid Orchestrator"
description: "Manages Selenium Grid 4 hub and node registration for cross-browser parallel testing. Configures Chrome, Firefox, and Edge nodes with resource allocation policies."
verification: "security_reviewed"
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Orchestrator

The Selenium Grid Orchestrator skill automates the deployment and management of Selenium Grid 4 infrastructure for distributed browser testing. It handles hub configuration, node registration, and session distribution across multiple browser types and versions. The skill configures Chrome, Firefox, and Edge nodes with specific resource allocation policies including max-sessions, stereotype matching, and drain timeouts. It supports Docker-based node scaling using Selenium Docker images with automatic pull and version pinning. Health monitoring tracks node availability, session queue depth, and test throughput metrics. The orchestrator implements smart session routing based on browser capability matching and node load balancing. Integration with TestNG and JUnit parallel execution allows test suites to scale horizontally across the grid. Configuration is managed through TOML files with environment variable overrides for CI environments.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/selenium-grid-orchestrator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/selenium-grid-orchestrator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/selenium-grid-orchestrator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-orchestrator/)
