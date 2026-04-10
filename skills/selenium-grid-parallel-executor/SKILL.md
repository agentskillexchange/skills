---
title: "Selenium Grid Parallel Executor"
description: "Orchestrates parallel browser automation across Selenium Grid nodes using RemoteWebDriver, DesiredCapabilities, and WebDriverWait. Manages session distribution, retry policies, and HTML test reports via ExtentReports."
slug: "selenium-grid-parallel-executor"
category:
  - "Browser Automation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/selenium-grid-parallel-executor/"
listed: true
---

# Selenium Grid Parallel Executor

Orchestrates parallel browser automation across Selenium Grid nodes using RemoteWebDriver, DesiredCapabilities, and WebDriverWait. Manages session distribution, retry policies, and HTML test reports via ExtentReports.

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
clawhub install selenium-grid-parallel-executor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill manages large-scale browser automation through Selenium Grid infrastructure. It configures Grid Hub and Node topology using selenium-server-standalone JAR or Docker Compose with selenium/hub and selenium/node-chrome images. Tests connect via RemoteWebDriver with DesiredCapabilities specifying browser name, version, and platform. WebDriverWait with ExpectedConditions handles dynamic page elements including visibility_of_element_located, element_to_be_clickable, and staleness_of for stale element reference recovery. The agent uses TestNG or pytest-xdist for parallel test distribution across grid nodes with configurable thread counts. Session management includes automatic cleanup via driver.quit() in teardown hooks and grid session timeout configuration. The skill integrates ExtentReports for rich HTML test reports with screenshots on failure using driver.get_screenshot_as_png(). Page Object Model architecture separates locators from test logic. Handles file download testing through ChromeOptions with download.default_directory preference. Supports cross-browser matrix testing with parameterized configurations for Chrome, Firefox, and Edge.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-executor/)
