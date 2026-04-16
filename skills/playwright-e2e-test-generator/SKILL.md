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
  ase_npm_package: "playwright"
  npm_weekly_downloads: 47883561
  license: "Apache-2.0"
---

# Playwright E2E Test Generator

This skill generates complete Playwright end-to-end test suites from natural language test case descriptions. It leverages the Playwright Test runner with built-in fixtures for BrowserContext, Page, and custom test isolation.

Generated tests use the Playwright Locator API with role-based selectors (getByRole, getByLabel, getByText) for resilient element targeting. The skill supports cross-browser execution across Chromium, Firefox, and WebKit engines simultaneously.

Advanced features include automatic screenshot capture on failure, video recording via the Playwright trace viewer, network request interception and mocking using route handlers, and visual regression testing with toHaveScreenshot assertions. The skill also generates Page Object Model classes for complex applications.

Test data management uses Playwright fixtures with automatic cleanup, and parallel test execution is configured via the playwright.config.ts with worker-level isolation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-e2e-test-generator/)
