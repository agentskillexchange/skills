---
title: Playwright PDF Export Automation
description: 'This skill leverages the Playwright browser automation library to generate
  high-fidelity PDF documents from any web URL or local HTML file. It uses chromium.launch({
  headless: true }) to spin up a headless Chromium instance, then navigates to the
  target page using page.goto() with configurable waitUntil options (load, domcontentloaded,
  networkidle). The PDF generation uses page.pdf() with full control over format (A4,
  Letter, Legal), margins (top, bottom, left, right in CSS units), scale factor, print
  background graphics, and custom header/footer HTML templates. The skill handles
  authentication scenarios by injecting cookies via context.addCookies() or setting
  HTTP headers. It includes retry logic for pages with lazy-loaded content, using
  page.waitForSelector() to ensure all dynamic content is rendered before capture.
  Output PDFs are saved locally or uploaded to S3 via the AWS SDK putObject API. Ideal
  for invoice generation, report archiving, and compliance documentation workflows.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/playwright-pdf-export-automation/
category:
- Browser Automation
framework:
- Claude Code
---

# Playwright PDF Export Automation

This skill leverages the Playwright browser automation library to generate high-fidelity PDF documents from any web URL or local HTML file. It uses chromium.launch({ headless: true }) to spin up a headless Chromium instance, then navigates to the target page using page.goto() with configurable waitUntil options (load, domcontentloaded, networkidle). The PDF generation uses page.pdf() with full control over format (A4, Letter, Legal), margins (top, bottom, left, right in CSS units), scale factor, print background graphics, and custom header/footer HTML templates. The skill handles authentication scenarios by injecting cookies via context.addCookies() or setting HTTP headers. It includes retry logic for pages with lazy-loaded content, using page.waitForSelector() to ensure all dynamic content is rendered before capture. Output PDFs are saved locally or uploaded to S3 via the AWS SDK putObject API. Ideal for invoice generation, report archiving, and compliance documentation workflows.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-pdf-export-automation/)
