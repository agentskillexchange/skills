---
name: "Playwright Accessibility Audit Runner"
description: "Runs automated WCAG 2.1 AA/AAA accessibility audits using Playwright with axe-core integration. Generates detailed violation reports with CSS selectors, ARIA role analysis, and remediation suggestions."
category: "Browser Automation"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/microsoft/playwright"
tool_ecosystem:
  tool: playwright
  github_stars: 84938
  npm_weekly_downloads: 39806814
  github_repo: microsoft/playwright
  license: Apache-2.0
  maintained: true
---
# Playwright Accessibility Audit Runner

Runs automated WCAG 2.1 AA/AAA accessibility audits using Playwright with axe-core integration. Generates detailed violation reports with CSS selectors, ARIA role analysis, and remediation suggestions.

## Overview

The Playwright Accessibility Audit Runner automates comprehensive web accessibility testing by combining Playwright browser automation with the axe-core accessibility engine. It crawls target sites and evaluates each page against WCAG 2.1 Level AA and AAA success criteria.

The skill injects @axe-core/playwright into each page context, running full DOM analysis including shadow DOM traversal, iframe content inspection, and dynamic content evaluation after JavaScript rendering. Results include precise CSS selectors for each violation, affected ARIA roles, color contrast ratios, and keyboard navigation paths.

Reports are generated in multiple formats: HTML with interactive violation highlighting, JSON for CI pipeline integration, and CSV for spreadsheet analysis. Each violation includes specific remediation code snippets tailored to the framework detected (React, Vue, Angular, or vanilla HTML).

Supports authenticated testing via Playwright storage state, custom viewport configurations for responsive accessibility checks, and parallel execution across multiple pages using Playwright test runner sharding.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-accessibility-audit-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-accessibility-audit-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-accessibility-audit-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-accessibility-audit-runner -a codex
```

### OpenClaw

```bash
clawhub install playwright-accessibility-audit-runner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-accessibility-audit-runner/)
