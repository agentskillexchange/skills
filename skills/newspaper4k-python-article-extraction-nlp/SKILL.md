---
title: "Newspaper4k Python Article Extraction and NLP Library"
description: "Newspaper4k is an actively maintained fork of the popular Newspaper3k library for Python. It extracts articles, titles, images, authors, and metadata from news websites, with built-in NLP for keyword extraction and text summarization."
slug: "newspaper4k-python-article-extraction-nlp"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/AndyTheFactory/newspaper4k"
listed: true
---

# Newspaper4k Python Article Extraction and NLP Library

Newspaper4k is an actively maintained fork of the popular Newspaper3k library for Python. It extracts articles, titles, images, authors, and metadata from news websites, with built-in NLP for keyword extraction and text summarization.

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
clawhub install newspaper4k-python-article-extraction-nlp
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Newspaper4k is a modern Python library for news article scraping, extraction, and curation. It is a community-maintained fork of the widely-used Newspaper3k library by codelucas, which had not been updated since September 2020. Newspaper4k brings the project back to life with active development, bug fixes, and new features while maintaining full backward compatibility with the original Newspaper3k API.
Core Capabilities
The library handles the full article processing pipeline: downloading, parsing, and natural language processing. Given any news article URL, Newspaper4k extracts the article text, authors, publish date, top image, embedded videos, and metadata. Its NLP module provides automatic keyword extraction and text summarization using NLTK under the hood.
CLI and Python API
Newspaper4k ships with a command-line interface that lets you extract articles directly from the terminal. Run python -m newspaper --url="https://example.com/article" --language=en --output-format=json to get structured JSON output. The Python API supports both single-article extraction via newspaper.article(url) and full-source building via the Source class, which discovers all articles and RSS feeds on a news website.
Multi-threaded Source Building
The Source class parses a newspaper website front page, detects category links, discovers RSS feeds, and builds a comprehensive list of article URLs. The download_articles() method uses ThreadPoolExecutor for concurrent downloads, making bulk extraction efficient. You can configure the number of threads and add request throttling.
Language Support and Extensibility
Newspaper4k supports over 40 languages for article extraction and NLP processing. It uses language-specific stopword lists and stemming algorithms. The library integrates well with data science workflows, feeding extracted text into pandas DataFrames, LLM pipelines, or custom NLP analysis. It requires Python 3.10+ and is available on PyPI as newspaper4k.
Agent Integration
For AI coding agents and automation workflows, Newspaper4k serves as a reliable content extraction layer. Agents can use it to gather training data, monitor news sources, build content databases, or feed article text into RAG pipelines. The structured output (JSON) makes it easy to chain with downstream processing steps.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/newspaper4k-python-article-extraction-nlp/)
