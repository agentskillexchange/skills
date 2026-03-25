---
name: "Selenium Grid Session Router"
description: "Routes browser automation sessions across Selenium Grid 4 nodes using the /status and /session endpoints. Configures RemoteWebDriver with DesiredCapabilities for cross-browser parallel execution."
category: "Browser Automation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/selenium-grid-session-router/"
tool_ecosystem:
  tool: "selenium"
  github_stars: 34174
  npm_weekly_downloads: 2000657
  github_repo: "SeleniumHQ/selenium"
  license: "Apache-2.0"
  maintained: true
---

# Selenium Grid Session Router

Routes browser automation sessions across Selenium Grid 4 nodes using the /status and /session endpoints. Configures RemoteWebDriver with DesiredCapabilities for cross-browser parallel execution.

## Overview

The Selenium Grid Session Router skill manages distributed browser automation by intelligently routing sessions across Selenium Grid 4 infrastructure. It queries the Grid /status endpoint to assess node availability and load, then distributes RemoteWebDriver sessions with appropriate DesiredCapabilities for Chrome, Firefox, and Edge browsers.

Core functionality includes session affinity management for multi-step test flows, automatic node health monitoring through /grid/api/hub/status polling, and graceful session redistribution when nodes become unavailable. The router configures WebDriverWait with ExpectedConditions for reliable element interaction across remote sessions.

Advanced features include custom capability matching with platformName and browserVersion constraints, VNC session recording integration for debugging remote test failures, and automatic session timeout management through se:recordVideo and se:timeZone capabilities. It supports Docker-based Grid deployment with automatic container scaling based on queue depth.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-router
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-router -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-router -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-session-router -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-session-router
```

## Source

- Marketplace: https://agentskillexchange.com/skills/selenium-grid-session-router/
