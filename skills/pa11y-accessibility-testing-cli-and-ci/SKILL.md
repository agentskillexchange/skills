---
title: Pa11y Accessibility Testing CLI and CI
description: 'Pa11y is an automated accessibility testing tool for websites and web
  applications, delivered as both a CLI and a JavaScript package. A skill built around
  Pa11y helps an agent run accessibility scans against one page, a route list, or
  a sitemap and then convert the results into a remediation plan. The concrete job-to-be-done
  is to detect accessibility issues early: missing labels, color contrast problems,
  semantic markup gaps, ARIA misuse, focus issues, and other WCAG-related violations
  that block users and create QA debt. Operationally, the skill can create a Pa11y
  configuration, set standards such as WCAG2AA or WCAG2AAA, configure runners, include
  ignore rules when needed, and execute scans in local development or CI/CD. The main
  outputs are structured issue objects, JSON results, exit codes for pipeline enforcement,
  and human-readable reports showing the affected page URL, message text, code, selector,
  and issue type. When paired with `pa11y-ci`, the same skill can scale from one-off
  checks to recurring regression coverage across multiple URLs. This is especially
  useful for documentation portals, marketing sites, dashboards, and CMS-driven properties
  where visual testing alone is not enough. Integration points include GitHub Actions,
  npm scripts, static-site builds, QA pipelines, and browser-rendered app previews.
  Technically, the skill speaks in terms of WCAG conformance, headless browser execution,
  selectors, reporters, thresholds, JSON output, and CI failure conditions. Because
  the upstream project has an official GitHub repo, npm package, and documentation
  site, the skill can be published with a trustworthy source URL and clear provenance.'
verification: security_reviewed
source: https://github.com/pa11y/pa11y
category:
- Browser Automation
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: pa11y/pa11y
  github_stars: 4418
  npm_package: pa11y
  npm_weekly_downloads: 201467
---

# Pa11y Accessibility Testing CLI and CI

Pa11y is an automated accessibility testing tool for websites and web applications, delivered as both a CLI and a JavaScript package. A skill built around Pa11y helps an agent run accessibility scans against one page, a route list, or a sitemap and then convert the results into a remediation plan. The concrete job-to-be-done is to detect accessibility issues early: missing labels, color contrast problems, semantic markup gaps, ARIA misuse, focus issues, and other WCAG-related violations that block users and create QA debt. Operationally, the skill can create a Pa11y configuration, set standards such as WCAG2AA or WCAG2AAA, configure runners, include ignore rules when needed, and execute scans in local development or CI/CD. The main outputs are structured issue objects, JSON results, exit codes for pipeline enforcement, and human-readable reports showing the affected page URL, message text, code, selector, and issue type. When paired with `pa11y-ci`, the same skill can scale from one-off checks to recurring regression coverage across multiple URLs. This is especially useful for documentation portals, marketing sites, dashboards, and CMS-driven properties where visual testing alone is not enough. Integration points include GitHub Actions, npm scripts, static-site builds, QA pipelines, and browser-rendered app previews. Technically, the skill speaks in terms of WCAG conformance, headless browser execution, selectors, reporters, thresholds, JSON output, and CI failure conditions. Because the upstream project has an official GitHub repo, npm package, and documentation site, the skill can be published with a trustworthy source URL and clear provenance.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pa11y-accessibility-testing-cli-and-ci/)
