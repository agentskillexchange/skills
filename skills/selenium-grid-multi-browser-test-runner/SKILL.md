---
name: "Selenium Grid Multi-Browser Test Runner"
description: "Orchestrates parallel cross-browser testing across Selenium Grid nodes using WebDriver RemoteConnection API. Supports Chrome, Firefox, and Edge with configurable DesiredCapabilities for each browser matrix."
category: "Browser Automation"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/selenium-grid-multi-browser-test-runner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "selenium"  # from ase_tool_match
  github_stars: 34169  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2000657  # from ase_npm_downloads
  github_repo: "SeleniumHQ/selenium"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Selenium Grid Multi-Browser Test Runner

Orchestrates parallel cross-browser testing across Selenium Grid nodes using WebDriver RemoteConnection API. Supports Chrome, Firefox, and Edge with configurable DesiredCapabilities for each browser matrix.

## Overview

This skill manages parallel cross-browser test execution using Selenium Grid 4 with the WebDriver protocol. It connects to a Selenium Hub via webdriver.Remote() with configurable hub URL and DesiredCapabilities for each target browser (Chrome, Firefox, Edge). The skill constructs a browser matrix from configuration, spawning concurrent sessions using asyncio.gather() for Python or Promise.all() for Node.js implementations. Each session uses the standard WebDriver API: driver.get() for navigation, driver.find_element(By.CSS_SELECTOR) for element location, element.click() and element.send_keys() for interaction. It implements the Page Object Model pattern for maintainable test organization. Screenshots on failure use driver.save_screenshot() with timestamped filenames. The skill handles session lifecycle management including implicit/explicit waits via WebDriverWait with expected_conditions, and proper cleanup with driver.quit() in finally blocks. Test results aggregate across all browser nodes into a unified HTML report using the Allure framework integration. Supports custom Chrome options via ChromeOptions.add_argument() for headless mode, proxy settings, and window sizing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-multi-browser-test-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-multi-browser-test-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-multi-browser-test-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-multi-browser-test-runner -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-multi-browser-test-runner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/selenium-grid-multi-browser-test-runner/
