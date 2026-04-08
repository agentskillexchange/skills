---
title: Selenium Grid Session Router
description: The Selenium Grid Session Router skill manages distributed browser automation
  by intelligently routing sessions across Selenium Grid 4 infrastructure. It queries
  the Grid /status endpoint to assess node availability and load, then distributes
  RemoteWebDriver sessions with appropriate DesiredCapabilities for Chrome, Firefox,
  and Edge browsers. Core functionality includes session affinity management for multi-step
  test flows, automatic node health monitoring through /grid/api/hub/status polling,
  and graceful session redistribution when nodes become unavailable. The router configures
  WebDriverWait with ExpectedConditions for reliable element interaction across remote
  sessions. Advanced features include custom capability matching with platformName
  and browserVersion constraints, VNC session recording integration for debugging
  remote test failures, and automatic session timeout management through se:recordVideo
  and se:timeZone capabilities. It supports Docker-based Grid deployment with automatic
  container scaling based on queue depth.
verification: security_reviewed
source: https://agentskillexchange.com/skills/selenium-grid-session-router/
category:
- Browser Automation
framework:
- OpenClaw
---

# Selenium Grid Session Router

The Selenium Grid Session Router skill manages distributed browser automation by intelligently routing sessions across Selenium Grid 4 infrastructure. It queries the Grid /status endpoint to assess node availability and load, then distributes RemoteWebDriver sessions with appropriate DesiredCapabilities for Chrome, Firefox, and Edge browsers. Core functionality includes session affinity management for multi-step test flows, automatic node health monitoring through /grid/api/hub/status polling, and graceful session redistribution when nodes become unavailable. The router configures WebDriverWait with ExpectedConditions for reliable element interaction across remote sessions. Advanced features include custom capability matching with platformName and browserVersion constraints, VNC session recording integration for debugging remote test failures, and automatic session timeout management through se:recordVideo and se:timeZone capabilities. It supports Docker-based Grid deployment with automatic container scaling based on queue depth.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-session-router/)
