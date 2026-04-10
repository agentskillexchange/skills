---
title: "Playwright Cross-Browser Test Runner"
description: "Runs end-to-end browser tests using Playwright Test with page.goto, page.locator, and expect assertions. Supports Chromium, Firefox, and WebKit with parallel execution and trace recording via trace.zip artifacts."
slug: "playwright-cross-browser-test-runner"
category:
  - "Browser Automation"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/playwright-cross-browser-test-runner/"
listed: true
---

# Playwright Cross-Browser Test Runner

Runs end-to-end browser tests using Playwright Test with page.goto, page.locator, and expect assertions. Supports Chromium, Firefox, and WebKit with parallel execution and trace recording via trace.zip artifacts.

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
clawhub install playwright-cross-browser-test-runner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill manages comprehensive cross-browser testing using the Playwright Test framework. It configures playwright.config.ts with projects for Chromium, Firefox, and WebKit, enabling parallel test execution with configurable workers. Tests use the Page object model with page.goto() for navigation, page.locator() with CSS and role-based selectors for element interaction, and page.waitForSelector() for dynamic content. Assertions leverage expect() with auto-retrying matchers like toBeVisible(), toHaveText(), and toHaveURL(). The agent sets up test fixtures using test.extend() for shared authentication states and page objects. Network interception is handled through page.route() for mocking API responses during testing. Visual regression testing uses expect(page).toHaveScreenshot() with configurable thresholds. Trace recording is enabled via trace: on-first-retry in config, producing trace.zip artifacts viewable in Playwright Trace Viewer. The skill handles CI integration with GitHub Actions workflows, including browser installation via npx playwright install –with-deps.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-cross-browser-test-runner/)
