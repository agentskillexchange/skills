---
name: "Extract clean article Markdown from web pages with Defuddle"
slug: "extract-clean-article-markdown-from-web-pages-with-defuddle"
description: "Use Defuddle when an agent needs clean, metadata-rich article text or Markdown from noisy web pages before summarizing, indexing, or archiving them."
github_stars: 7176
verification: "listed"
source: "https://github.com/kepano/defuddle"
author: "kepano"
publisher_type: "open_source_project"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "kepano/defuddle"
  github_stars: 7176
  npm_package: "defuddle"
  npm_weekly_downloads: 38526
---

# Extract clean article Markdown from web pages with Defuddle

Use Defuddle when an agent needs clean, metadata-rich article text or Markdown from noisy web pages before summarizing, indexing, or archiving them.

## Prerequisites

Node.js, npx or npm, defuddle CLI

## Installation

Use the upstream install or setup path that matches your environment:
- npx defuddle parse page.html
- npx defuddle parse https://example.com/article
- npx defuddle parse page.html --markdown
- npx defuddle parse page.html --json

Requirements and caveats from upstream:
- ### Node.js
- defuddle/node accepts a DOM Document from any implementation (JSDOM, linkedom, happy-dom, etc.).
- import { Defuddle } from 'defuddle/node';

Basic usage or getting-started notes:
- Defuddle takes a URL or HTML, finds the main content, and returns cleaned HTML or Markdown. Defuddle was created for the browser extension [Obsidian Web Clipper](https://github.com/obsidianmd/obsidian-clipper), but it...
- ### Browser
- javascript

- Source: https://github.com/kepano/defuddle
- Extracted from upstream docs: https://raw.githubusercontent.com/kepano/defuddle/HEAD/README.md

## Documentation

- https://defuddle.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-clean-article-markdown-from-web-pages-with-defuddle/)
