---
title: "Playwright E2E Test Generator"
description: "Generates Playwright test suites from natural language descriptions using the Playwright Test API. Supports cross-browser testing with Chromium, Firefox, and WebKit via BrowserContext fixtures."
verification: "security_reviewed"
source: "https://github.com/microsoft/playwright"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  npm_package: "playwright"
  npm_weekly_downloads: 47883561
---

# Playwright E2E Test Generator

This skill generates complete Playwright end-to-end test suites from natural language test case descriptions. It leverages the Playwright Test runner with built-in fixtures for BrowserContext, Page, and custom test isolation. Generated tests use the Playwright Locator API with role-based selectors (getByRole, getByLabel, getByText) for resilient element targeting. The skill supports cross-browser execution across Chromium, Firefox, and WebKit engines simultaneously. Advanced features include automatic screenshot capture on failure, video recording via the Playwright trace viewer, network request interception and mocking using route handlers, and visual regression testing with toHaveScreenshot assertions. The skill also generates Page Object Model classes for complex applications. Test data management uses Playwright fixtures with automatic cleanup, and parallel test execution is configured via the playwright.config.ts with worker-level isolation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/playwright-e2e-test-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/playwright-e2e-test-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/playwright-e2e-test-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-e2e-test-generator/)
