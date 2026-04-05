---
name: "xq Command-Line XML and HTML Beautifier and Content Extractor"
description: "xq is a command-line XML and HTML beautifier and content extractor written in Go. It provides syntax highlighting, automatic formatting, XPath and CSS selector queries, and JSON output conversion for XML and HTML documents."
category: "Data Extraction &amp; Transformation"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/sibprogrammer/xq"
tool_ecosystem:
  github_repo: "sibprogrammer/xq"
  github_stars: 1100
  license: "MIT"
---
# xq Command-Line XML and HTML Beautifier and Content Extractor

xq is a command-line XML and HTML beautifier and content extractor written in Go. It provides syntax highlighting, automatic formatting, XPath and CSS selector queries, and JSON output conversion for XML and HTML documents.

What is xq? xq is a command-line tool for formatting, highlighting, and extracting content from XML and HTML documents. Built in Go and distributed as a single binary, it serves as a Swiss-army knife for working with XML data in the terminal. It supports syntax highlighting with automatic color detection, intelligent indentation and pretty-printing, XPath query expressions for extracting node content, CSS selectors for HTML processing, JSON output mode, and in-place file formatting.

How It Works Pass an XML or HTML file as an argument or pipe content through stdin. By default, xq formats and syntax-highlights the output with automatic pagination. Use the -x flag with an XPath expression to extract specific nodes (e.g., xq -x //city to get all city elements). The -q flag enables CSS selector queries for HTML content. The -j flag converts XML output to JSON format, preserving the document structure with attributes prefixed by @ and text content stored under #text. The -m flag switches to HTML mode for processing web pages.

Key Features xq handles multiple files at once, supports in-place formatting with -i, can extract attribute values with -a, and outputs node content as plain text or with surrounding tags using -n. It processes both well-formed XML and real-world HTML with tag soup tolerance. The JSON output mode is particularly useful for piping XML data into jq for further processing, bridging the gap between XML and JSON toolchains.

Installation xq is available through Homebrew (brew install xq), as a snap package (snap install xq), in many Linux distribution repositories, via Go install (go install github.com/sibprogrammer/xq@latest), or as pre-built binaries from GitHub releases for Linux, macOS, and Windows.

Integration Points xq fits into shell pipelines alongside curl for fetching and parsing web APIs that return XML, pairs with jq via its JSON output mode, and works as a formatting pre-processor for XML config files in CI/CD workflows. Agents working with SOAP APIs, RSS feeds, SVG files, Maven POMs, or any XML-based configuration can use xq to extract and transform data without heavyweight XML libraries.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill xq-command-line-xml-html-beautifier-content-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill xq-command-line-xml-html-beautifier-content-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill xq-command-line-xml-html-beautifier-content-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill xq-command-line-xml-html-beautifier-content-extractor -a codex
```

### OpenClaw

```bash
clawhub install xq-command-line-xml-html-beautifier-content-extractor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/xq-command-line-xml-html-beautifier-content-extractor/)
