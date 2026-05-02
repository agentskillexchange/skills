---
title: "Cheerio HTML and XML Parsing Library for Node.js Extraction Workflows"
description: "Cheerio is a long-running Node.js library for parsing and manipulating HTML and XML with a jQuery-like API. It is widely used in scraping, extraction, and content transformation pipelines where developers need fast server-side DOM traversal without a browser runtime."
verification: "security_reviewed"
source: "https://github.com/cheeriojs/cheerio"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "cheeriojs/cheerio"
  github_stars: 30266
  npm_package: "cheerio"
  npm_weekly_downloads: 19621708
---

# Cheerio HTML and XML Parsing Library for Node.js Extraction Workflows

Cheerio is one of the most established HTML parsing libraries in the Node.js ecosystem. It provides a fast, lightweight API for loading HTML or XML, selecting elements with jQuery-style selectors, and transforming the resulting document tree in server-side code. For many extraction and cleanup tasks, it gives developers the DOM-style ergonomics they want without the overhead of launching a headless browser.

The upstream package is published on npm as cheerio and maintained by the Cheerio organization. Its README highlights three main strengths: proven jQuery-like syntax, fast parsing and rendering, and flexibility through parsers such as parse5 and optional htmlparser2. Typical workflows include extracting product details, cleaning CMS output, rewriting links, converting fragments before indexing, and post-processing pages fetched by other crawlers.

On ASE, Cheerio maps cleanly to data extraction and transformation jobs because it sits in the middle of many scraping pipelines: fetch HTML, load it into Cheerio, select the nodes you need, and emit structured data or rewritten markup. It is especially useful when a page is accessible without heavy client-side execution and the goal is speed, repeatability, and simple deployment. The public repo, documentation site, MIT license, active maintenance, and very large npm adoption make it a strong metadata-verified candidate.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cheerio-html-xml-parsing-library-nodejs-extraction-workflows/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cheerio-html-xml-parsing-library-nodejs-extraction-workflows
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cheerio-html-xml-parsing-library-nodejs-extraction-workflows`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cheerio-html-xml-parsing-library-nodejs-extraction-workflows/)
