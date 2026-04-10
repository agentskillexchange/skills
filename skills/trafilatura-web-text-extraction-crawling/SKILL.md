---
name: Trafilatura Web Text Extraction and Crawling Toolkit
description: Trafilatura is a Python package and CLI tool for gathering text from
  the web. It handles crawling, downloading, and extracting main text content, metadata,
  and comments from raw HTML, outputting clean structured data in CSV, JSON, Markdown,
  XML, and TXT formats.
verification: security_reviewed
source: https://github.com/adbar/trafilatura
category:
- Research &amp; Scraping
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: adbar/trafilatura
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trafilatura-web-text-extraction-crawling/)
