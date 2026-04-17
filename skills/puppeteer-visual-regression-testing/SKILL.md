---
title: "Puppeteer Visual Regression Testing"
description: "This skill implements automated visual regression testing using Puppeteer for browser control and the pixelmatch library for pixel-level image comparison. It launches Chrome via puppeteer.launch() with configurable viewport dimensions using page.setViewport({ width, height }). For each test case, it captures full-page screenshots using page.screenshot({ fullPage: true, type: “png” }) and compares them against stored baseline images. The diffing engine uses pixelmatch with adjustable threshold (0.0-1.0) and alpha channel handling. When differences exceed the configured tolerance, the skill generates a diff image highlighting changed pixels in red. It supports testing across multiple viewport sizes for responsive design verification, running parallel browser instances via Promise.all for speed. Authentication is handled through page.type() for form filling and page.waitForNavigation() for login flows. Results are output as JSON reports with pass/fail status, diff percentage, and paths to diff images. Integrates with CI pipelines via exit codes and JUnit XML report generation."
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Visual Regression Testing

This skill implements automated visual regression testing using Puppeteer for browser control and the pixelmatch library for pixel-level image comparison. It launches Chrome via puppeteer.launch() with configurable viewport dimensions using page.setViewport({ width, height }). For each test case, it captures full-page screenshots using page.screenshot({ fullPage: true, type: “png” }) and compares them against stored baseline images. The diffing engine uses pixelmatch with adjustable threshold (0.0-1.0) and alpha channel handling. When differences exceed the configured tolerance, the skill generates a diff image highlighting changed pixels in red. It supports testing across multiple viewport sizes for responsive design verification, running parallel browser instances via Promise.all for speed. Authentication is handled through page.type() for form filling and page.waitForNavigation() for login flows. Results are output as JSON reports with pass/fail status, diff percentage, and paths to diff images. Integrates with CI pipelines via exit codes and JUnit XML report generation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/puppeteer-visual-regression-testing
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/puppeteer-visual-regression-testing` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-visual-regression-testing/)
