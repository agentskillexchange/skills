---
title: Playwright Cross-Browser Test Runner
description: 'This skill manages comprehensive cross-browser testing using the Playwright
  Test framework. It configures playwright.config.ts with projects for Chromium, Firefox,
  and WebKit, enabling parallel test execution with configurable workers. Tests use
  the Page object model with page.goto() for navigation, page.locator() with CSS and
  role-based selectors for element interaction, and page.waitForSelector() for dynamic
  content. Assertions leverage expect() with auto-retrying matchers like toBeVisible(),
  toHaveText(), and toHaveURL(). The agent sets up test fixtures using test.extend()
  for shared authentication states and page objects. Network interception is handled
  through page.route() for mocking API responses during testing. Visual regression
  testing uses expect(page).toHaveScreenshot() with configurable thresholds. Trace
  recording is enabled via trace: on-first-retry in config, producing trace.zip artifacts
  viewable in Playwright Trace Viewer. The skill handles CI integration with GitHub
  Actions workflows, including browser installation via npx playwright install –with-deps.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/playwright-cross-browser-test-runner/
category:
- Browser Automation
framework:
- ChatGPT Agents
---

# Playwright Cross-Browser Test Runner

This skill manages comprehensive cross-browser testing using the Playwright Test framework. It configures playwright.config.ts with projects for Chromium, Firefox, and WebKit, enabling parallel test execution with configurable workers. Tests use the Page object model with page.goto() for navigation, page.locator() with CSS and role-based selectors for element interaction, and page.waitForSelector() for dynamic content. Assertions leverage expect() with auto-retrying matchers like toBeVisible(), toHaveText(), and toHaveURL(). The agent sets up test fixtures using test.extend() for shared authentication states and page objects. Network interception is handled through page.route() for mocking API responses during testing. Visual regression testing uses expect(page).toHaveScreenshot() with configurable thresholds. Trace recording is enabled via trace: on-first-retry in config, producing trace.zip artifacts viewable in Playwright Trace Viewer. The skill handles CI integration with GitHub Actions workflows, including browser installation via npx playwright install –with-deps.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-cross-browser-test-runner/)
