---
title: "Playwright E2E Test Generator"
description: "This skill generates complete Playwright end-to-end test suites from natural language test case descriptions. It leverages the Playwright Test runner with built-in fixtures for BrowserContext, Page, and custom test isolation. Generated tests use the Playwright Locator API with role-based selectors (getByRole, getByLabel, getByText) for resilient element targeting. The skill supports cross-browser execution across Chromium, Firefox, and WebKit engines simultaneously. Advanced features include automatic screenshot capture on failure, video recording via the Playwright trace viewer, network request interception and mocking using route handlers, and visual regression testing with toHaveScreenshot assertions. The skill also generates Page Object Model classes for complex applications. Test data management uses Playwright fixtures with automatic cleanup, and parallel test execution is configured via the playwright.config.ts with worker-level isolation."
source: "https://github.com/microsoft/playwright"
verification: "security_reviewed"
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

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-e2e-test-generator/)
