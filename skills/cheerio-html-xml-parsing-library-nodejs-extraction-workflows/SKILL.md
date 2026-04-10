---
title: "Cheerio HTML and XML Parsing Library for Node.js Extraction Workflows"
description: "Cheerio is a long-running Node.js library for parsing and manipulating HTML and XML with a jQuery-like API. It is widely used in scraping, extraction, and content transformation pipelines where developers need fast server-side DOM traversal without a browser runtime."
slug: "cheerio-html-xml-parsing-library-nodejs-extraction-workflows"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/cheeriojs/cheerio"
---

# Cheerio HTML and XML Parsing Library for Node.js Extraction Workflows

Cheerio is a long-running Node.js library for parsing and manipulating HTML and XML with a jQuery-like API. It is widely used in scraping, extraction, and content transformation pipelines where developers need fast server-side DOM traversal without a browser runtime.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install cheerio-html-xml-parsing-library-nodejs-extraction-workflows
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Cheerio is one of the most established HTML parsing libraries in the Node.js ecosystem. It provides a fast, lightweight API for loading HTML or XML, selecting elements with jQuery-style selectors, and transforming the resulting document tree in server-side code. For many extraction and cleanup tasks, it gives developers the DOM-style ergonomics they want without the overhead of launching a headless browser.
The upstream package is published on npm as cheerio and maintained by the Cheerio organization. Its README highlights three main strengths: proven jQuery-like syntax, fast parsing and rendering, and flexibility through parsers such as parse5 and optional htmlparser2. Typical workflows include extracting product details, cleaning CMS output, rewriting links, converting fragments before indexing, and post-processing pages fetched by other crawlers.
On ASE, Cheerio maps cleanly to data extraction and transformation jobs because it sits in the middle of many scraping pipelines: fetch HTML, load it into Cheerio, select the nodes you need, and emit structured data or rewritten markup. It is especially useful when a page is accessible without heavy client-side execution and the goal is speed, repeatability, and simple deployment. The public repo, documentation site, MIT license, active maintenance, and very large npm adoption make it a strong metadata-verified candidate.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cheerio-html-xml-parsing-library-nodejs-extraction-workflows/)
