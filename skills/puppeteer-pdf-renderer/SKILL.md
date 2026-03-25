---
name: "Puppeteer PDF Renderer"
description: "Generates pixel-perfect PDFs from web pages using Puppeteer with custom headers, footers, and page breaks. Supports authenticated pages via cookie injection."
category: "Browser Automation"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/puppeteer-pdf-renderer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "puppeteer"  # from ase_tool_match
  github_stars: 93932  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8696130  # from ase_npm_downloads
  github_repo: "puppeteer/puppeteer"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Puppeteer PDF Renderer

Generates pixel-perfect PDFs from web pages using Puppeteer with custom headers, footers, and page breaks. Supports authenticated pages via cookie injection.

## Overview

The Puppeteer PDF Renderer skill converts live web pages into high-fidelity PDF documents using the Puppeteer headless Chrome API. It handles complex CSS layouts including flexbox, grid, and print media queries to produce pixel-perfect output.

The skill supports custom header and footer templates with dynamic page numbers, date stamps, and document titles. Page break control uses CSS break-before and break-after properties, with intelligent orphan and widow handling for text-heavy content.

Authentication is handled through cookie injection from exported browser profiles or via programmatic login flows. The renderer waits for lazy-loaded images, web fonts, and async JavaScript before capture. Batch mode processes multiple URLs concurrently with configurable parallelism. Output options include A4, Letter, Legal, and custom page sizes with adjustable margins.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-pdf-renderer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-pdf-renderer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-pdf-renderer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-pdf-renderer -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-pdf-renderer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/puppeteer-pdf-renderer/
