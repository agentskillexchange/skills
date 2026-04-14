---
title: "Playwright PDF Export Automation"
description: "Automates headless PDF generation from web pages using the Playwright chromium.launch() API with custom page.pdf() options. Supports A4/Letter sizing, header/footer templates, and configurable margins via Playwright’s PDFOptions interface."
verification: security_reviewed
source: "https://github.com/microsoft/playwright"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  npm_package: "playwright"
  npm_weekly_downloads: 47883561
---

# Playwright PDF Export Automation

This skill leverages the Playwright browser automation library to generate high-fidelity PDF documents from any web URL or local HTML file. It uses chromium.launch({ headless: true }) to spin up a headless Chromium instance, then navigates to the target page using page.goto() with configurable waitUntil options (load, domcontentloaded, networkidle). The PDF generation uses page.pdf() with full control over format (A4, Letter, Legal), margins (top, bottom, left, right in CSS units), scale factor, print background graphics, and custom header/footer HTML templates. The skill handles authentication scenarios by injecting cookies via context.addCookies() or setting HTTP headers. It includes retry logic for pages with lazy-loaded content, using page.waitForSelector() to ensure all dynamic content is rendered before capture. Output PDFs are saved locally or uploaded to S3 via the AWS SDK putObject API. Ideal for invoice generation, report archiving, and compliance documentation workflows.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-pdf-export-automation/)
