---
title: "Selenium Grid Session Router"
description: "Routes browser automation sessions across Selenium Grid 4 nodes using the /status and /session endpoints. Configures RemoteWebDriver with DesiredCapabilities for cross-browser parallel execution."
verification: security_reviewed
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  ase_npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Session Router

The Selenium Grid Session Router skill manages distributed browser automation by intelligently routing sessions across Selenium Grid 4 infrastructure. It queries the Grid /status endpoint to assess node availability and load, then distributes RemoteWebDriver sessions with appropriate DesiredCapabilities for Chrome, Firefox, and Edge browsers.

Core functionality includes session affinity management for multi-step test flows, automatic node health monitoring through /grid/api/hub/status polling, and graceful session redistribution when nodes become unavailable. The router configures WebDriverWait with ExpectedConditions for reliable element interaction across remote sessions.

Advanced features include custom capability matching with platformName and browserVersion constraints, VNC session recording integration for debugging remote test failures, and automatic session timeout management through se:recordVideo and se:timeZone capabilities. It supports Docker-based Grid deployment with automatic container scaling based on queue depth.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/selenium-grid-session-router
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/selenium-grid-session-router` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-router/)
