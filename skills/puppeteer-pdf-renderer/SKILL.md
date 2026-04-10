---
name: Puppeteer PDF Renderer
description: Generates pixel-perfect PDFs from web pages using Puppeteer with custom
  headers, footers, and page breaks. Supports authenticated pages via cookie injection.
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteer-pdf-renderer/
category:
- Browser Automation
framework:
- Cursor
---
# Puppeteer PDF Renderer

The Puppeteer PDF Renderer skill converts live web pages into high-fidelity PDF documents using the Puppeteer headless Chrome API. It handles complex CSS layouts including flexbox, grid, and print media queries to produce pixel-perfect output.
The skill supports custom header and footer templates with dynamic page numbers, date stamps, and document titles. Page break control uses CSS break-before and break-after properties, with intelligent orphan and widow handling for text-heavy content.
Authentication is handled through cookie injection from exported browser profiles or via programmatic login flows. The renderer waits for lazy-loaded images, web fonts, and async JavaScript before capture. Batch mode processes multiple URLs concurrently with configurable parallelism. Output options include A4, Letter, Legal, and custom page sizes with adjustable margins.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-pdf-renderer/)
