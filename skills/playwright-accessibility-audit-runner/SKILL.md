---
name: Playwright Accessibility Audit Runner
description: Runs automated WCAG 2.1 AA/AAA accessibility audits using Playwright
  with axe-core integration. Generates detailed violation reports with CSS selectors,
  ARIA role analysis, and remediation suggestions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/playwright-accessibility-audit-runner/
category:
- Browser Automation
framework:
- Cursor
---
# Playwright Accessibility Audit Runner

The Playwright Accessibility Audit Runner automates comprehensive web accessibility testing by combining Playwright browser automation with the axe-core accessibility engine. It crawls target sites and evaluates each page against WCAG 2.1 Level AA and AAA success criteria.
The skill injects @axe-core/playwright into each page context, running full DOM analysis including shadow DOM traversal, iframe content inspection, and dynamic content evaluation after JavaScript rendering. Results include precise CSS selectors for each violation, affected ARIA roles, color contrast ratios, and keyboard navigation paths.
Reports are generated in multiple formats: HTML with interactive violation highlighting, JSON for CI pipeline integration, and CSV for spreadsheet analysis. Each violation includes specific remediation code snippets tailored to the framework detected (React, Vue, Angular, or vanilla HTML).
Supports authenticated testing via Playwright storage state, custom viewport configurations for responsive accessibility checks, and parallel execution across multiple pages using Playwright test runner sharding.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-accessibility-audit-runner/)
