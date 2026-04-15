---
title: "Trafilatura Web Text Extraction and Crawling Toolkit"
description: "Trafilatura is a Python package and CLI tool for gathering text from the web. It handles crawling, downloading, and extracting main text content, metadata, and comments from raw HTML, outputting clean structured data in CSV, JSON, Markdown, XML, and TXT formats."
verification: security_reviewed
source: "https://github.com/adbar/trafilatura"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "adbar/trafilatura"
  github_stars: 5638
---

# Trafilatura Web Text Extraction and Crawling Toolkit

Trafilatura is a Python package and command-line tool designed to simplify the process of turning raw HTML into structured, meaningful data. It performs web crawling, page downloads, scraping, and extraction of main text content, metadata, and comments from web pages. The tool outputs clean text in multiple formats including CSV, JSON, HTML, Markdown, TXT, and XML.

Core Capabilities
The library handles advanced web crawling with support for sitemaps (TXT and XML formats) and feeds (ATOM, JSON, RSS). It includes smart URL management with deduplication and filtering. Trafilatura processes both live URLs and previously downloaded HTML files, supporting parallel processing for efficient batch operations.

Text Extraction Engine
The extraction engine uses multiple algorithms including jusText and readability to identify and extract the main content from web pages. It strips away navigation bars, headers, footers, sidebars, and other boilerplate elements while preserving the actual article or page content. The extractor balances precision (limiting noise) with recall (including all valid content parts). Metadata extraction covers title, author, date, site name, categories, and tags.

Integration and Usage
Trafilatura is widely used and integrated into thousands of projects by organizations including HuggingFace, IBM, Microsoft Research, the Allen Institute, Stanford, the Tokyo Institute of Technology, and the University of Munich. It is available on PyPI via pip install trafilatura and as a standalone CLI tool. The library supports Python 3.6+ and is licensed under Apache 2.0. It is particularly valuable for building RAG pipelines, training data collection, corpus construction, and content aggregation workflows.

Agent Skill Application
An agent skill built on Trafilatura can automate web content harvesting at scale. The agent can crawl target domains, extract clean text, and output structured datasets for downstream NLP tasks. The CLI interface makes it directly invocable from agent tool calls, and the Python API allows deep integration into custom agent pipelines. With over 5,600 GitHub stars and academic citations, it is one of the most trusted web text extraction tools available.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/trafilatura-web-text-extraction-crawling
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/trafilatura-web-text-extraction-crawling` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trafilatura-web-text-extraction-crawling/)
