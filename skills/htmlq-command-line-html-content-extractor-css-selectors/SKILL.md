---
title: "htmlq Command-Line HTML Content Extractor with CSS Selectors"
description: "htmlq is a command-line tool for extracting content from HTML using CSS selectors, functioning as the HTML equivalent of jq. Written in Rust, it lets you pipe HTML through CSS selectors to extract text, attributes, and structured content directly from the terminal."
slug: "htmlq-command-line-html-content-extractor-css-selectors"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/mgdm/htmlq"
tool_ecosystem:
  github_repo: "mgdm/htmlq"
  github_stars: 7514
---

# htmlq Command-Line HTML Content Extractor with CSS Selectors

htmlq is a command-line tool for extracting content from HTML using CSS selectors, functioning as the HTML equivalent of jq. Written in Rust, it lets you pipe HTML through CSS selectors to extract text, attributes, and structured content directly from the terminal.

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
clawhub install htmlq-command-line-html-content-extractor-css-selectors
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

What is htmlq?
htmlq is a lightweight, fast command-line utility written in Rust that applies CSS selectors to HTML input and extracts matching content. Think of it as jq for HTML — where jq processes JSON with filter expressions, htmlq processes HTML with CSS selectors. It reads HTML from stdin or files and outputs selected elements, text content, or attribute values.
How It Works
htmlq uses the Servo browser engine CSS selector implementation (the same engine behind Firefox) for parsing and matching. You pipe HTML content into htmlq along with a CSS selector expression, and it returns the matching elements. The tool supports extracting inner text with the -t flag, pulling specific attributes with -a, removing unwanted nodes before output with -r, pretty-printing output with -p, and detecting base URLs for resolving relative links.
Real-World Usage
Typical workflows include extracting all links from a page (curl a URL and pipe to htmlq “a” -a href), pulling headlines (htmlq “h1, h2, h3” -t), scraping structured data from tables, removing navigation and sidebar elements before extracting article content, and integrating with shell pipelines for web scraping automation. The tool excels in CI/CD pipelines where you need to verify HTML output, extract build artifacts from dashboards, or parse release notes from web pages.
Installation
htmlq is installable via cargo (cargo install htmlq), Homebrew (brew install htmlq), Scoop on Windows (scoop install htmlq), or FreeBSD packages (pkg install htmlq). Pre-built binaries are available on the GitHub releases page.
Integration Points
htmlq integrates naturally with curl, wget, and other HTTP clients for web scraping pipelines. It pairs well with jq for post-processing extracted JSON data, xargs for batch operations, and standard Unix tools like grep, sed, and awk. Agents can use it to extract structured data from web pages without needing a full browser automation setup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/htmlq-command-line-html-content-extractor-css-selectors/)
