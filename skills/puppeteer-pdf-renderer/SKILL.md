---
title: "Puppeteer PDF Renderer"
description: "Generates pixel-perfect PDFs from web pages using Puppeteer with custom headers, footers, and page breaks. Supports authenticated pages via cookie injection."
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Browser Automation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer PDF Renderer

The Puppeteer PDF Renderer skill converts live web pages into high-fidelity PDF documents using the Puppeteer headless Chrome API. It handles complex CSS layouts including flexbox, grid, and print media queries to produce pixel-perfect output.

The skill supports custom header and footer templates with dynamic page numbers, date stamps, and document titles. Page break control uses CSS break-before and break-after properties, with intelligent orphan and widow handling for text-heavy content.

Authentication is handled through cookie injection from exported browser profiles or via programmatic login flows. The renderer waits for lazy-loaded images, web fonts, and async JavaScript before capture. Batch mode processes multiple URLs concurrently with configurable parallelism. Output options include A4, Letter, Legal, and custom page sizes with adjustable margins.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-pdf-renderer/)
