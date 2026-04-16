---
title: "Puppeteer PDF Renderer"
description: "Generates pixel-perfect PDFs from web pages using Puppeteer with custom headers, footers, and page breaks. Supports authenticated pages via cookie injection."
verification: "security_reviewed"
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Browser Automation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
  license: "Apache-2.0"
---

# Puppeteer PDF Renderer

The Puppeteer PDF Renderer skill converts live web pages into high-fidelity PDF documents using the Puppeteer headless Chrome API. It handles complex CSS layouts including flexbox, grid, and print media queries to produce pixel-perfect output.

The skill supports custom header and footer templates with dynamic page numbers, date stamps, and document titles. Page break control uses CSS break-before and break-after properties, with intelligent orphan and widow handling for text-heavy content.

Authentication is handled through cookie injection from exported browser profiles or via programmatic login flows. The renderer waits for lazy-loaded images, web fonts, and async JavaScript before capture. Batch mode processes multiple URLs concurrently with configurable parallelism. Output options include A4, Letter, Legal, and custom page sizes with adjustable margins.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-pdf-renderer/)
