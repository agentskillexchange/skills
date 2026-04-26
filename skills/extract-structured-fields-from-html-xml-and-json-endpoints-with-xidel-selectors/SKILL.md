---
title: "Extract structured fields from HTML XML and JSON endpoints with Xidel selectors"
description: "Use Xidel to pull targeted values from pages, XML documents, or JSON APIs with CSS selectors, XPath, XQuery, or JSONiq expressions."
verification: "security_reviewed"
source: "https://github.com/benibela/xidel"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "benibela/xidel"
  github_stars: 835
---

# Extract structured fields from HTML XML and JSON endpoints with Xidel selectors

Use this skill when an agent needs to extract structured values from markup or API responses without spinning up a full browser-automation stack. Xidel can download and query HTML, XML, and JSON sources using CSS selectors, XPath, XQuery, and JSONiq, which makes it a strong fit for precise field extraction, feed harvesting, or transformation-oriented scraping tasks.

Invoke it instead of using the product normally when the requested job is a narrow selector-driven extraction pass: fetch a source, run declarative queries, and return structured results. That scope boundary keeps this from being a generic scraper or CLI listing. The agent is not selling a browser framework or broad crawling platform; it is performing a concrete extraction workflow over supplied sources.

Xidel is also distinct from simpler HTML-only selector tools because the same invocation model spans HTML, XML, and JSON inputs and supports richer query languages such as XPath, XQuery, and JSONiq. The upstream repository explicitly presents it as a command-line tool for downloading and extracting data from HTML/XML pages or JSON APIs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/extract-structured-fields-from-html-xml-and-json-endpoints-with-xidel-selectors/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/extract-structured-fields-from-html-xml-and-json-endpoints-with-xidel-selectors
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/extract-structured-fields-from-html-xml-and-json-endpoints-with-xidel-selectors`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-structured-fields-from-html-xml-and-json-endpoints-with-xidel-selectors/)
