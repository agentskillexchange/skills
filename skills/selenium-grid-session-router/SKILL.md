---
title: "Selenium Grid Session Router"
description: "Routes browser automation sessions across Selenium Grid 4 nodes using the /status and /session endpoints. Configures RemoteWebDriver with DesiredCapabilities for cross-browser parallel execution."
slug: "selenium-grid-session-router"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/selenium-grid-session-router/"
listed: true
---

# Selenium Grid Session Router

Routes browser automation sessions across Selenium Grid 4 nodes using the /status and /session endpoints. Configures RemoteWebDriver with DesiredCapabilities for cross-browser parallel execution.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install selenium-grid-session-router
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Selenium Grid Session Router skill manages distributed browser automation by intelligently routing sessions across Selenium Grid 4 infrastructure. It queries the Grid /status endpoint to assess node availability and load, then distributes RemoteWebDriver sessions with appropriate DesiredCapabilities for Chrome, Firefox, and Edge browsers.
Core functionality includes session affinity management for multi-step test flows, automatic node health monitoring through /grid/api/hub/status polling, and graceful session redistribution when nodes become unavailable. The router configures WebDriverWait with ExpectedConditions for reliable element interaction across remote sessions.
Advanced features include custom capability matching with platformName and browserVersion constraints, VNC session recording integration for debugging remote test failures, and automatic session timeout management through se:recordVideo and se:timeZone capabilities. It supports Docker-based Grid deployment with automatic container scaling based on queue depth.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-router/)
