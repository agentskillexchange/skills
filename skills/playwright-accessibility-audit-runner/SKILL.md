---
title: "Playwright Accessibility Audit Runner"
description: "Runs automated WCAG 2.1 AA/AAA accessibility audits using Playwright with axe-core integration. Generates detailed violation reports with CSS selectors, ARIA role analysis, and remediation suggestions."
slug: "playwright-accessibility-audit-runner"
category:
  - "Browser Automation"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/playwright-accessibility-audit-runner/"
listed: true
---

# Playwright Accessibility Audit Runner

Runs automated WCAG 2.1 AA/AAA accessibility audits using Playwright with axe-core integration. Generates detailed violation reports with CSS selectors, ARIA role analysis, and remediation suggestions.

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
clawhub install playwright-accessibility-audit-runner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Playwright Accessibility Audit Runner automates comprehensive web accessibility testing by combining Playwright browser automation with the axe-core accessibility engine. It crawls target sites and evaluates each page against WCAG 2.1 Level AA and AAA success criteria.
The skill injects @axe-core/playwright into each page context, running full DOM analysis including shadow DOM traversal, iframe content inspection, and dynamic content evaluation after JavaScript rendering. Results include precise CSS selectors for each violation, affected ARIA roles, color contrast ratios, and keyboard navigation paths.
Reports are generated in multiple formats: HTML with interactive violation highlighting, JSON for CI pipeline integration, and CSV for spreadsheet analysis. Each violation includes specific remediation code snippets tailored to the framework detected (React, Vue, Angular, or vanilla HTML).
Supports authenticated testing via Playwright storage state, custom viewport configurations for responsive accessibility checks, and parallel execution across multiple pages using Playwright test runner sharding.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-accessibility-audit-runner/)
