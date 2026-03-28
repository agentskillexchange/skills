---
name: "Playwright PDF Export Automation"
description: "Automates headless PDF generation from web pages using the Playwright chromium.launch() API with custom page.pdf() options. Supports A4/Letter sizing, header/footer templates, and configurable margins via Playwright’s PDFOptions interface."
category: "Browser Automation"
framework: "Claude Code"
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

# Playwright PDF Export Automation

Automates headless PDF generation from web pages using the Playwright chromium.launch() API with custom page.pdf() options. Supports A4/Letter sizing, header/footer templates, and configurable margins via Playwright’s PDFOptions interface.

## Overview

This skill leverages the Playwright browser automation library to generate high-fidelity PDF documents from any web URL or local HTML file. It uses chromium.launch({ headless: true }) to spin up a headless Chromium instance, then navigates to the target page using page.goto() with configurable waitUntil options (load, domcontentloaded, networkidle). The PDF generation uses page.pdf() with full control over format (A4, Letter, Legal), margins (top, bottom, left, right in CSS units), scale factor, print background graphics, and custom header/footer HTML templates. The skill handles authentication scenarios by injecting cookies via context.addCookies() or setting HTTP headers. It includes retry logic for pages with lazy-loaded content, using page.waitForSelector() to ensure all dynamic content is rendered before capture. Output PDFs are saved locally or uploaded to S3 via the AWS SDK putObject API. Ideal for invoice generation, report archiving, and compliance documentation workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-pdf-export-automation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-pdf-export-automation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-pdf-export-automation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-pdf-export-automation -a codex
```

### OpenClaw

```bash
clawhub install playwright-pdf-export-automation
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-pdf-export-automation/
