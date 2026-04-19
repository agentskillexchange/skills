---
title: "Selenium Grid Parallel Executor"
description: "This skill manages large-scale browser automation through Selenium Grid infrastructure. It configures Grid Hub and Node topology using selenium-server-standalone JAR or Docker Compose with selenium/hub and selenium/node-chrome images. Tests connect via RemoteWebDriver with DesiredCapabilities specifying browser name, version, and platform. WebDriverWait with ExpectedConditions handles dynamic page elements including visibility_of_element_located, element_to_be_clickable, and staleness_of for stale element reference recovery. The agent uses TestNG or pytest-xdist for parallel test distribution across grid nodes with configurable thread counts. Session management includes automatic cleanup via driver.quit() in teardown hooks and grid session timeout configuration. The skill integrates ExtentReports for rich HTML test reports with screenshots on failure using driver.get_screenshot_as_png(). Page Object Model architecture separates locators from test logic. Handles file download testing through ChromeOptions with download.default_directory preference. Supports cross-browser matrix testing with parameterized configurations for Chrome, Firefox, and Edge."
source: "https://github.com/SeleniumHQ/selenium"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Parallel Executor

This skill manages large-scale browser automation through Selenium Grid infrastructure. It configures Grid Hub and Node topology using selenium-server-standalone JAR or Docker Compose with selenium/hub and selenium/node-chrome images. Tests connect via RemoteWebDriver with DesiredCapabilities specifying browser name, version, and platform. WebDriverWait with ExpectedConditions handles dynamic page elements including visibility_of_element_located, element_to_be_clickable, and staleness_of for stale element reference recovery. The agent uses TestNG or pytest-xdist for parallel test distribution across grid nodes with configurable thread counts. Session management includes automatic cleanup via driver.quit() in teardown hooks and grid session timeout configuration. The skill integrates ExtentReports for rich HTML test reports with screenshots on failure using driver.get_screenshot_as_png(). Page Object Model architecture separates locators from test logic. Handles file download testing through ChromeOptions with download.default_directory preference. Supports cross-browser matrix testing with parameterized configurations for Chrome, Firefox, and Edge.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-executor/)
