---
name: "markdownify Python HTML to Markdown Conversion Library"
description: "markdownify is a Python library that converts HTML content to clean Markdown text. It supports tag filtering, heading styles, custom converters, and code language detection, making it essential for content extraction and document transformation pipelines."
category: "Data Extraction &amp; Transformation"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/matthewwithanm/python-markdownify"
tool_ecosystem:
  github_repo: "matthewwithanm/python-markdownify"
  github_stars: 2130
---
# markdownify Python HTML to Markdown Conversion Library

markdownify is a Python library that converts HTML content to clean Markdown text. It supports tag filtering, heading styles, custom converters, and code language detection, making it essential for content extraction and document transformation pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill markdownify-python-html-to-markdown-converter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill markdownify-python-html-to-markdown-converter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill markdownify-python-html-to-markdown-converter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill markdownify-python-html-to-markdown-converter -a codex
```

### OpenClaw

```bash
clawhub install markdownify-python-html-to-markdown-converter
```

## Details

Overview
markdownify is a Python library that converts HTML to Markdown. Created by Matthew Tretter, it uses BeautifulSoup under the hood to parse HTML and produces clean, configurable Markdown output. It is widely used in web scraping pipelines, content migration tools, and LLM data preparation workflows — notably, Microsoft’s MarkItDown uses markdownify internally for its HTML conversion step.

Core Capabilities
The library handles a comprehensive range of HTML elements: headings, paragraphs, bold, italic, links, images, lists (ordered and unordered), blockquotes, code blocks, tables, horizontal rules, and more. Configuration options include heading style (ATX, SETEXT), bullet characters, strong/em symbols, newline style (spaces or backslash), and escape behavior for special Markdown characters.

Advanced features include tag-level strip/convert filtering (choose exactly which HTML tags to convert or ignore), custom converter classes for extending behavior per-tag, code language detection via callbacks, and inline image preservation in table cells and headings.

Agent Integration
For AI agents, markdownify is a critical building block in content processing chains. When scraping web pages, agents can feed raw HTML through markdownify to produce clean Markdown suitable for LLM context windows. It is lighter weight than full browser-based solutions when the goal is text extraction rather than rendering. Agents can subclass MarkdownConverter to create domain-specific converters that handle custom HTML structures.

Installation and Usage
Install via pip: pip install markdownify. Basic usage: from markdownify import markdownify as md; result = md('<b>Hello</b> <a href="https://example.com">World</a>'). The library requires Python 3.x and depends on BeautifulSoup4 and six.

Documentation and Community
The project README on GitHub serves as the primary documentation with full option reference and custom converter examples. The library has over 2,100 GitHub stars, is MIT licensed, and is published on PyPI with consistent download numbers. It has been a stable dependency in the Python ecosystem for over a decade.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/markdownify-python-html-to-markdown-converter/)
