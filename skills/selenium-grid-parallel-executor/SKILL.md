---
name: "Selenium Grid Parallel Executor"
description: "Orchestrates parallel browser automation across Selenium Grid nodes using RemoteWebDriver, DesiredCapabilities, and WebDriverWait. Manages session distribution, retry policies, and HTML test reports via ExtentReports."
category: "Browser Automation"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/selenium-grid-parallel-executor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "selenium"  # from ase_tool_match
  github_stars: 34174  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2000657  # from ase_npm_downloads
  github_repo: "SeleniumHQ/selenium"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Selenium Grid Parallel Executor

Orchestrates parallel browser automation across Selenium Grid nodes using RemoteWebDriver, DesiredCapabilities, and WebDriverWait. Manages session distribution, retry policies, and HTML test reports via ExtentReports.

## Overview

This skill manages large-scale browser automation through Selenium Grid infrastructure. It configures Grid Hub and Node topology using selenium-server-standalone JAR or Docker Compose with selenium/hub and selenium/node-chrome images. Tests connect via RemoteWebDriver with DesiredCapabilities specifying browser name, version, and platform. WebDriverWait with ExpectedConditions handles dynamic page elements including visibility_of_element_located, element_to_be_clickable, and staleness_of for stale element reference recovery. The agent uses TestNG or pytest-xdist for parallel test distribution across grid nodes with configurable thread counts. Session management includes automatic cleanup via driver.quit() in teardown hooks and grid session timeout configuration. The skill integrates ExtentReports for rich HTML test reports with screenshots on failure using driver.get_screenshot_as_png(). Page Object Model architecture separates locators from test logic. Handles file download testing through ChromeOptions with download.default_directory preference. Supports cross-browser matrix testing with parameterized configurations for Chrome, Firefox, and Edge.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-executor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-executor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-executor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-executor -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-parallel-executor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/selenium-grid-parallel-executor/
