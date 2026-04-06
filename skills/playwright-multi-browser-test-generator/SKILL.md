---
name: Playwright Multi-Browser Test Generator
description: Generates Playwright test scripts for Chromium, Firefox, and WebKit from
  natural language descriptions. Uses the Playwright codegen recorder API and assertion
  library for reliable E2E tests.
category: Browser Automation
framework: Codex
verification: security_reviewed
source: "https://agentskillexchange.com/skills/playwright-multi-browser-test-generator/"
---
# Playwright Multi-Browser Test Generator

Generates Playwright test scripts for Chromium, Firefox, and WebKit from natural language descriptions. Uses the Playwright codegen recorder API and assertion library for reliable E2E tests.

The Playwright Multi-Browser Test Generator creates production-ready end-to-end test scripts targeting all three browser engines supported by Playwright: Chromium, Firefox, and WebKit. Given natural language descriptions of user flows, it generates TypeScript test files using Playwright Test runner with proper fixtures, page object models, and auto-waiting assertions. The skill leverages Playwright locator strategies—role-based selectors, text content matching, and CSS/XPath fallbacks—to create resilient selectors that survive UI changes. It configures browser contexts with viewport settings, geolocation, permissions, and color scheme preferences for comprehensive coverage. Network interception via page.route() is used to mock API responses for deterministic testing. The generated tests include visual regression checks using Playwright screenshot comparison with configurable threshold values. Parallel execution is configured across browser projects with shared authentication state via storageState, and HTML test reports are generated with trace viewer integration for debugging failures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-browser-test-generator -a codex
```

### OpenClaw

```bash
clawhub install playwright-multi-browser-test-generator
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-multi-browser-test-generator/)
