---
title: "Playwright Accessibility Audit Runner"
description: "Runs automated WCAG 2.1 AA/AAA accessibility audits using Playwright with axe-core integration. Generates detailed violation reports with CSS selectors, ARIA role analysis, and remediation suggestions."
verification: security_reviewed
source: "https://github.com/microsoft/playwright"
category:
  - "Browser Automation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  npm_package: "playwright"
  npm_weekly_downloads: 47883561
  license: "Apache-2.0"
---

# Playwright Accessibility Audit Runner

The Playwright Accessibility Audit Runner automates comprehensive web accessibility testing by combining Playwright browser automation with the axe-core accessibility engine. It crawls target sites and evaluates each page against WCAG 2.1 Level AA and AAA success criteria.

The skill injects @axe-core/playwright into each page context, running full DOM analysis including shadow DOM traversal, iframe content inspection, and dynamic content evaluation after JavaScript rendering. Results include precise CSS selectors for each violation, affected ARIA roles, color contrast ratios, and keyboard navigation paths.

Reports are generated in multiple formats: HTML with interactive violation highlighting, JSON for CI pipeline integration, and CSV for spreadsheet analysis. Each violation includes specific remediation code snippets tailored to the framework detected (React, Vue, Angular, or vanilla HTML).

Supports authenticated testing via Playwright storage state, custom viewport configurations for responsive accessibility checks, and parallel execution across multiple pages using Playwright test runner sharding.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/playwright-accessibility-audit-runner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/playwright-accessibility-audit-runner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-accessibility-audit-runner/)
