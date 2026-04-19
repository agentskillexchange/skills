---
title: "Puppeteer PDF Renderer"
description: "The Puppeteer PDF Renderer skill converts live web pages into high-fidelity PDF documents using the Puppeteer headless Chrome API. It handles complex CSS layouts including flexbox, grid, and print media queries to produce pixel-perfect output. The skill supports custom header and footer templates with dynamic page numbers, date stamps, and document titles. Page break control uses CSS break-before and break-after properties, with intelligent orphan and widow handling for text-heavy content. Authentication is handled through cookie injection from exported browser profiles or via programmatic login flows. The renderer waits for lazy-loaded images, web fonts, and async JavaScript before capture. Batch mode processes multiple URLs concurrently with configurable parallelism. Output options include A4, Letter, Legal, and custom page sizes with adjustable margins."
source: "https://github.com/puppeteer/puppeteer"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer PDF Renderer

The Puppeteer PDF Renderer skill converts live web pages into high-fidelity PDF documents using the Puppeteer headless Chrome API. It handles complex CSS layouts including flexbox, grid, and print media queries to produce pixel-perfect output. The skill supports custom header and footer templates with dynamic page numbers, date stamps, and document titles. Page break control uses CSS break-before and break-after properties, with intelligent orphan and widow handling for text-heavy content. Authentication is handled through cookie injection from exported browser profiles or via programmatic login flows. The renderer waits for lazy-loaded images, web fonts, and async JavaScript before capture. Batch mode processes multiple URLs concurrently with configurable parallelism. Output options include A4, Letter, Legal, and custom page sizes with adjustable margins.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-pdf-renderer/)
