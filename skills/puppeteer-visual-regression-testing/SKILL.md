---
name: "Puppeteer Visual Regression Testing"
description: "Runs pixel-level visual regression tests using Puppeteer page.screenshot() and pixelmatch diffing library. Compares baseline screenshots against current renders with configurable threshold tolerance."
category: "Browser Automation"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/puppeteer-visual-regression-testing/"
---
# Puppeteer Visual Regression Testing

Runs pixel-level visual regression tests using Puppeteer page.screenshot() and pixelmatch diffing library. Compares baseline screenshots against current renders with configurable threshold tolerance.

This skill implements automated visual regression testing using Puppeteer for browser control and the pixelmatch library for pixel-level image comparison. It launches Chrome via puppeteer.launch() with configurable viewport dimensions using page.setViewport({ width, height }). For each test case, it captures full-page screenshots using page.screenshot({ fullPage: true, type: “png” }) and compares them against stored baseline images. The diffing engine uses pixelmatch with adjustable threshold (0.0-1.0) and alpha channel handling. When differences exceed the configured tolerance, the skill generates a diff image highlighting changed pixels in red. It supports testing across multiple viewport sizes for responsive design verification, running parallel browser instances via Promise.all for speed. Authentication is handled through page.type() for form filling and page.waitForNavigation() for login flows. Results are output as JSON reports with pass/fail status, diff percentage, and paths to diff images. Integrates with CI pipelines via exit codes and JUnit XML report generation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-testing
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-testing -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-testing -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-visual-regression-testing -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-visual-regression-testing
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-visual-regression-testing/)
