---
title: Selenium Grid Parallel Executor
description: This skill manages large-scale browser automation through Selenium Grid
  infrastructure. It configures Grid Hub and Node topology using selenium-server-standalone
  JAR or Docker Compose with selenium/hub and selenium/node-chrome images. Tests connect
  via RemoteWebDriver with DesiredCapabilities specifying browser name, version, and
  platform. WebDriverWait with ExpectedConditions handles dynamic page elements including
  visibility_of_element_located, element_to_be_clickable, and staleness_of for stale
  element reference recovery. The agent uses TestNG or pytest-xdist for parallel test
  distribution across grid nodes with configurable thread counts. Session management
  includes automatic cleanup via driver.quit() in teardown hooks and grid session
  timeout configuration. The skill integrates ExtentReports for rich HTML test reports
  with screenshots on failure using driver.get_screenshot_as_png(). Page Object Model
  architecture separates locators from test logic. Handles file download testing through
  ChromeOptions with download.default_directory preference. Supports cross-browser
  matrix testing with parameterized configurations for Chrome, Firefox, and Edge.
verification: security_reviewed
source: https://agentskillexchange.com/skills/selenium-grid-parallel-executor/
category:
- Browser Automation
framework:
- Custom Agents
---

# Selenium Grid Parallel Executor

This skill manages large-scale browser automation through Selenium Grid infrastructure. It configures Grid Hub and Node topology using selenium-server-standalone JAR or Docker Compose with selenium/hub and selenium/node-chrome images. Tests connect via RemoteWebDriver with DesiredCapabilities specifying browser name, version, and platform. WebDriverWait with ExpectedConditions handles dynamic page elements including visibility_of_element_located, element_to_be_clickable, and staleness_of for stale element reference recovery. The agent uses TestNG or pytest-xdist for parallel test distribution across grid nodes with configurable thread counts. Session management includes automatic cleanup via driver.quit() in teardown hooks and grid session timeout configuration. The skill integrates ExtentReports for rich HTML test reports with screenshots on failure using driver.get_screenshot_as_png(). Page Object Model architecture separates locators from test logic. Handles file download testing through ChromeOptions with download.default_directory preference. Supports cross-browser matrix testing with parameterized configurations for Chrome, Firefox, and Edge.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-executor/)
