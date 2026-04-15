---
title: "Playwright Cross-Browser Test Runner"
description: "Runs end-to-end browser tests using Playwright Test with page.goto, page.locator, and expect assertions. Supports Chromium, Firefox, and WebKit with parallel execution and trace recording via trace.zip artifacts."
verification: security_reviewed
source: "https://github.com/microsoft/playwright"
category:
  - "Browser Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  npm_package: "playwright"
  npm_weekly_downloads: 47883561
---

# Playwright Cross-Browser Test Runner

This skill manages comprehensive cross-browser testing using the Playwright Test framework. It configures playwright.config.ts with projects for Chromium, Firefox, and WebKit, enabling parallel test execution with configurable workers. Tests use the Page object model with page.goto() for navigation, page.locator() with CSS and role-based selectors for element interaction, and page.waitForSelector() for dynamic content. Assertions leverage expect() with auto-retrying matchers like toBeVisible(), toHaveText(), and toHaveURL(). The agent sets up test fixtures using test.extend() for shared authentication states and page objects. Network interception is handled through page.route() for mocking API responses during testing. Visual regression testing uses expect(page).toHaveScreenshot() with configurable thresholds. Trace recording is enabled via trace: on-first-retry in config, producing trace.zip artifacts viewable in Playwright Trace Viewer. The skill handles CI integration with GitHub Actions workflows, including browser installation via npx playwright install –with-deps.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/playwright-cross-browser-test-runner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/playwright-cross-browser-test-runner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-cross-browser-test-runner/)
