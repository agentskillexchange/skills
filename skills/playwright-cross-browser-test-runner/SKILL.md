---
name: "Playwright Cross-Browser Test Runner"
description: "Runs end-to-end browser tests using Playwright Test with page.goto, page.locator, and expect assertions. Supports Chromium, Firefox, and WebKit with parallel execution and trace recording via trace.zip artifacts."
category: "Browser Automation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/playwright-cross-browser-test-runner/"
---
# Playwright Cross-Browser Test Runner

Runs end-to-end browser tests using Playwright Test with page.goto, page.locator, and expect assertions. Supports Chromium, Firefox, and WebKit with parallel execution and trace recording via trace.zip artifacts.

This skill manages comprehensive cross-browser testing using the Playwright Test framework. It configures playwright.config.ts with projects for Chromium, Firefox, and WebKit, enabling parallel test execution with configurable workers. Tests use the Page object model with page.goto() for navigation, page.locator() with CSS and role-based selectors for element interaction, and page.waitForSelector() for dynamic content. Assertions leverage expect() with auto-retrying matchers like toBeVisible(), toHaveText(), and toHaveURL(). The agent sets up test fixtures using test.extend() for shared authentication states and page objects. Network interception is handled through page.route() for mocking API responses during testing. Visual regression testing uses expect(page).toHaveScreenshot() with configurable thresholds. Trace recording is enabled via trace: on-first-retry in config, producing trace.zip artifacts viewable in Playwright Trace Viewer. The skill handles CI integration with GitHub Actions workflows, including browser installation via npx playwright install –with-deps.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-cross-browser-test-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-cross-browser-test-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-cross-browser-test-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-cross-browser-test-runner -a codex
```

### OpenClaw

```bash
clawhub install playwright-cross-browser-test-runner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-cross-browser-test-runner/)
