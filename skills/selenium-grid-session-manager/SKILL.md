---
title: "Selenium Grid Session Manager"
description: "Manages distributed browser sessions on Selenium Grid 4 via the GraphQL API and /status endpoint. Handles node scaling, session queuing, and capability matching for parallel test execution."
verification: security_reviewed
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  ase_npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Session Manager

The Selenium Grid Session Manager orchestrates distributed browser testing infrastructure using Selenium Grid 4’s modern architecture. It communicates with the Grid via the GraphQL API endpoint (/graphql) for detailed session and node information, and the /status REST endpoint for health monitoring.

The skill handles dynamic node registration and capability matching, ensuring test sessions are routed to nodes with the correct browser version, platform, and custom capabilities. It manages session queuing with configurable timeout and retry policies, preventing queue overflow during peak testing periods.

Advanced features include automatic node scaling based on queue depth (integrating with Docker API for container-based nodes), session video recording via Selenium Video docker images, and VNC live-view connections for debugging. The manager tracks session lifecycle events (created, assigned, completed, failed) and generates utilization dashboards. It supports both hub-node and fully distributed Grid architectures, with health checks that automatically drain unhealthy nodes and redistribute pending sessions.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/selenium-grid-session-manager
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/selenium-grid-session-manager` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-manager/)
