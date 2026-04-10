---
name: Selenium Grid Session Router
description: Routes browser automation sessions across Selenium Grid 4 nodes using
  the /status and /session endpoints. Configures RemoteWebDriver with DesiredCapabilities
  for cross-browser parallel execution.
verification: security_reviewed
source: https://agentskillexchange.com/skills/selenium-grid-session-router/
category:
- Browser Automation
framework:
- OpenClaw
---
# Selenium Grid Session Router

The Selenium Grid Session Router skill manages distributed browser automation by intelligently routing sessions across Selenium Grid 4 infrastructure. It queries the Grid /status endpoint to assess node availability and load, then distributes RemoteWebDriver sessions with appropriate DesiredCapabilities for Chrome, Firefox, and Edge browsers.
Core functionality includes session affinity management for multi-step test flows, automatic node health monitoring through /grid/api/hub/status polling, and graceful session redistribution when nodes become unavailable. The router configures WebDriverWait with ExpectedConditions for reliable element interaction across remote sessions.
Advanced features include custom capability matching with platformName and browserVersion constraints, VNC session recording integration for debugging remote test failures, and automatic session timeout management through se:recordVideo and se:timeZone capabilities. It supports Docker-based Grid deployment with automatic container scaling based on queue depth.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-router/)
