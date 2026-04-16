---
title: "Selenium Grid Multi-Browser Test Runner"
description: "Orchestrates parallel cross-browser testing across Selenium Grid nodes using WebDriver RemoteConnection API. Supports Chrome, Firefox, and Edge with configurable DesiredCapabilities for each browser matrix."
verification: "security_reviewed"
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
---

# Selenium Grid Multi-Browser Test Runner

This skill manages parallel cross-browser test execution using Selenium Grid 4 with the WebDriver protocol. It connects to a Selenium Hub via webdriver.Remote() with configurable hub URL and DesiredCapabilities for each target browser (Chrome, Firefox, Edge). The skill constructs a browser matrix from configuration, spawning concurrent sessions using asyncio.gather() for Python or Promise.all() for Node.js implementations. Each session uses the standard WebDriver API: driver.get() for navigation, driver.find_element(By.CSS_SELECTOR) for element location, element.click() and element.send_keys() for interaction. It implements the Page Object Model pattern for maintainable test organization. Screenshots on failure use driver.save_screenshot() with timestamped filenames. The skill handles session lifecycle management including implicit/explicit waits via WebDriverWait with expected_conditions, and proper cleanup with driver.quit() in finally blocks. Test results aggregate across all browser nodes into a unified HTML report using the Allure framework integration. Supports custom Chrome options via ChromeOptions.add_argument() for headless mode, proxy settings, and window sizing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-multi-browser-test-runner/)
