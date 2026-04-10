---
title: "Playwright PDF Export Automation"
description: "Automates headless PDF generation from web pages using the Playwright chromium.launch() API with custom page.pdf() options. Supports A4/Letter sizing, header/footer templates, and configurable margins via Playwright’s PDFOptions interface."
slug: "playwright-pdf-export-automation"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/playwright-pdf-export-automation/"
---

# Playwright PDF Export Automation

Automates headless PDF generation from web pages using the Playwright chromium.launch() API with custom page.pdf() options. Supports A4/Letter sizing, header/footer templates, and configurable margins via Playwright’s PDFOptions interface.

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
clawhub install playwright-pdf-export-automation
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill leverages the Playwright browser automation library to generate high-fidelity PDF documents from any web URL or local HTML file. It uses chromium.launch({ headless: true }) to spin up a headless Chromium instance, then navigates to the target page using page.goto() with configurable waitUntil options (load, domcontentloaded, networkidle). The PDF generation uses page.pdf() with full control over format (A4, Letter, Legal), margins (top, bottom, left, right in CSS units), scale factor, print background graphics, and custom header/footer HTML templates. The skill handles authentication scenarios by injecting cookies via context.addCookies() or setting HTTP headers. It includes retry logic for pages with lazy-loaded content, using page.waitForSelector() to ensure all dynamic content is rendered before capture. Output PDFs are saved locally or uploaded to S3 via the AWS SDK putObject API. Ideal for invoice generation, report archiving, and compliance documentation workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-pdf-export-automation/)
