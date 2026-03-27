---
name: "Playwright E2E Test Generator"
description: "Generates Playwright test suites from natural language descriptions using the Playwright Test API. Supports cross-browser testing with Chromium, Firefox, and WebKit via BrowserContext fixtures."
category: "Developer Tools"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/playwright-e2e-test-generator/"
tool_ecosystem:
  tool: playwright
  github_stars: 84938
  npm_weekly_downloads: 39806814
  github_repo: microsoft/playwright
  license: Apache-2.0
  maintained: true
---

# Playwright E2E Test Generator

Generates Playwright test suites from natural language descriptions using the Playwright Test API. Supports cross-browser testing with Chromium, Firefox, and WebKit via BrowserContext fixtures.

## Overview

This skill generates complete Playwright end-to-end test suites from natural language test case descriptions. It leverages the Playwright Test runner with built-in fixtures for BrowserContext, Page, and custom test isolation.

Generated tests use the Playwright Locator API with role-based selectors (getByRole, getByLabel, getByText) for resilient element targeting. The skill supports cross-browser execution across Chromium, Firefox, and WebKit engines simultaneously.

Advanced features include automatic screenshot capture on failure, video recording via the Playwright trace viewer, network request interception and mocking using route handlers, and visual regression testing with toHaveScreenshot assertions. The skill also generates Page Object Model classes for complex applications.

Test data management uses Playwright fixtures with automatic cleanup, and parallel test execution is configured via the playwright.config.ts with worker-level isolation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-e2e-test-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-e2e-test-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-e2e-test-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-e2e-test-generator -a codex
```

### OpenClaw

```bash
clawhub install playwright-e2e-test-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-e2e-test-generator/
