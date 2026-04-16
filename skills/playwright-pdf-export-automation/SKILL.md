---
title: "Playwright PDF Export Automation"
description: "Automates headless PDF generation from web pages using the Playwright chromium.launch() API with custom page.pdf() options. Supports A4/Letter sizing, header/footer templates, and configurable margins via Playwright’s PDFOptions interface."
verification: "security_reviewed"
source: "https://github.com/microsoft/playwright"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  ase_npm_package: "playwright"
  npm_weekly_downloads: 47883561
  license: "Apache-2.0"
---

# Playwright PDF Export Automation

This skill leverages the Playwright browser automation library to generate high-fidelity PDF documents from any web URL or local HTML file. It uses chromium.launch({ headless: true }) to spin up a headless Chromium instance, then navigates to the target page using page.goto() with configurable waitUntil options (load, domcontentloaded, networkidle). The PDF generation uses page.pdf() with full control over format (A4, Letter, Legal), margins (top, bottom, left, right in CSS units), scale factor, print background graphics, and custom header/footer HTML templates. The skill handles authentication scenarios by injecting cookies via context.addCookies() or setting HTTP headers. It includes retry logic for pages with lazy-loaded content, using page.waitForSelector() to ensure all dynamic content is rendered before capture. Output PDFs are saved locally or uploaded to S3 via the AWS SDK putObject API. Ideal for invoice generation, report archiving, and compliance documentation workflows.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-pdf-export-automation/)
