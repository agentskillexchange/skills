---
name: "axe-core Accessibility Testing Engine for Automated Web UI Auditing"
description: "axe-core is the industry-standard accessibility testing engine by Deque Systems that automatically detects WCAG 2.0, 2.1, and 2.2 violations in web interfaces. It integrates into any existing test framework — Playwright, Cypress, Selenium, Jest — to catch accessibility issues during development rather than after deployment."
verification: security_reviewed
source: "https://github.com/dequelabs/axe-core"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
---

# axe-core Accessibility Testing Engine for Automated Web UI Auditing

axe-core is an open-source accessibility testing engine maintained by Deque Systems that powers automated WCAG compliance checking across web applications. With nearly 7,000 GitHub stars and millions of weekly npm downloads, it is the most widely adopted accessibility testing library in the JavaScript ecosystem.
What It Does
axe-core analyzes rendered HTML against a comprehensive rule set covering WCAG 2.0, 2.1, and 2.2 at levels A, AA, and AAA. It identifies violations like missing alt text, insufficient color contrast, improper ARIA usage, missing form labels, and broken heading hierarchies. The engine returns zero false positives by design — every reported issue is a genuine accessibility barrier.
How It Works
The library runs inside a browser context (real or headless) and inspects the live DOM. You inject axe-core into your page, call axe.run(), and receive a structured results object containing violations, passes, and incomplete checks that need manual review. It automatically determines which rules apply based on the evaluation context and supports iframes at infinite depth.
Integration Points
axe-core integrates with every major testing framework through official adapter packages: @axe-core/playwright for Playwright, @axe-core/webdriverjs for Selenium WebDriver, @axe-core/puppeteer for Puppeteer, and jest-axe for Jest unit tests. The @axe-core/cli package provides a standalone command-line interface for CI/CD pipelines. It also powers the axe DevTools browser extension used by hundreds of thousands of developers.
Agent Skill Applications
An AI agent can use axe-core to run automated accessibility audits as part of code review workflows, flagging WCAG violations in pull requests before they reach production. Agents can integrate axe-core scans into CI pipelines, generate human-readable accessibility reports, prioritize fixes by impact level, and track compliance improvements over time. The structured JSON output makes it straightforward to parse results and take automated action.
Installation
Install via npm: npm install axe-core --save-dev. For framework-specific integration, install the relevant adapter package (e.g., npm install @axe-core/playwright).

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/axe-core-accessibility-testing-engine/)
