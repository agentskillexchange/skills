---
title: "Selenium Grid Session Router"
description: "Routes browser automation sessions across Selenium Grid 4 nodes using the /status and /session endpoints. Configures RemoteWebDriver with DesiredCapabilities for cross-browser parallel execution."
verification: "security_reviewed"
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  license: "Apache-2.0"
---

# Selenium Grid Session Router

The Selenium Grid Session Router skill manages distributed browser automation by intelligently routing sessions across Selenium Grid 4 infrastructure. It queries the Grid /status endpoint to assess node availability and load, then distributes RemoteWebDriver sessions with appropriate DesiredCapabilities for Chrome, Firefox, and Edge browsers.

Core functionality includes session affinity management for multi-step test flows, automatic node health monitoring through /grid/api/hub/status polling, and graceful session redistribution when nodes become unavailable. The router configures WebDriverWait with ExpectedConditions for reliable element interaction across remote sessions.

Advanced features include custom capability matching with platformName and browserVersion constraints, VNC session recording integration for debugging remote test failures, and automatic session timeout management through se:recordVideo and se:timeZone capabilities. It supports Docker-based Grid deployment with automatic container scaling based on queue depth.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-router/)
