---
title: "Selenium Grid Parallel Executor"
description: "Orchestrates parallel browser automation across Selenium Grid nodes using RemoteWebDriver, DesiredCapabilities, and WebDriverWait. Manages session distribution, retry policies, and HTML test reports via ExtentReports."
verification: security_reviewed
source: "https://github.com/SeleniumHQ/selenium"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-executor/)
