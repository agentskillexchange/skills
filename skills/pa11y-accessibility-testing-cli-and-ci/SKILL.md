---
name: "Pa11y Accessibility Testing CLI and CI"
slug: "pa11y-accessibility-testing-cli-and-ci"
description: "Pa11y is a real open-source accessibility testing tool that lets agents audit pages for WCAG issues from the command line or in CI. This skill uses Pa11y to turn page-level accessibility checks into actionable reports with issue counts, selectors, and remediation context."
github_stars: 4418
verification: "listed"
source: "https://github.com/pa11y/pa11y"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "pa11y/pa11y"
  github_stars: 4418
  npm_package: "pa11y"
  npm_weekly_downloads: 221677
---

# Pa11y Accessibility Testing CLI and CI

Pa11y is a real open-source accessibility testing tool that lets agents audit pages for WCAG issues from the command line or in CI. This skill uses Pa11y to turn page-level accessibility checks into actionable reports with issue counts, selectors, and remediation context.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install nvm
- npm install -g pa11y
- npm install pa11y --save-dev
- npm run lint # Lint the code

Requirements and caveats from upstream:
- Pa11y is your automated accessibility testing pal. It runs accessibility tests on your pages via the command line or Node.js, so you can automate your testing process.
- [![Node.js version support][shield-node]][info-node]
- const pa11y = require('pa11y');

Basic usage or getting-started notes:
- pa11y https://example.com
- pa11y('https://example.com').then((results) => {
- ### Linux and macOS

- Source: https://github.com/pa11y/pa11y
- Extracted from upstream docs: https://raw.githubusercontent.com/pa11y/pa11y/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pa11y-accessibility-testing-cli-and-ci/)
