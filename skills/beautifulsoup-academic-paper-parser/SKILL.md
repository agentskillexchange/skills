---
name: "Beautiful Soup Academic Paper Parser"
description: "Extracts structured citation data from academic repositories using BeautifulSoup4 with lxml parser. Parses DOI metadata, author affiliations, and reference lists from PubMed, arXiv, and Semantic Scholar HTML."
category: "Research & Scraping"
framework: "MCP-compatible"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/beautifulsoup-academic-paper-parser/"
---

# Beautiful Soup Academic Paper Parser

Extracts structured citation data from academic repositories using BeautifulSoup4 with lxml parser. Parses DOI metadata, author affiliations, and reference lists from PubMed, arXiv, and Semantic Scholar HTML.

## Overview

This skill extracts structured bibliographic data from academic paper repositories using BeautifulSoup4 with the lxml parser for fast HTML processing. It handles the unique DOM structures of major academic platforms including PubMed, arXiv abstract pages, and Semantic Scholar.

Extraction targets include paper titles, abstract text, author names with affiliations, DOI identifiers, publication dates, journal/conference names, and full reference lists with citation counts. The skill uses CSS selectors and find_all() with regex patterns to handle varying HTML structures across platforms. DOI resolution uses the CrossRef API for metadata enrichment.

Output formats include BibTeX, RIS, and structured JSON following the CSL-JSON schema for compatibility with reference managers like Zotero and Mendeley. Rate limiting respects robots.txt directives and implements polite crawling with configurable delays between requests.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill beautifulsoup-academic-paper-parser
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill beautifulsoup-academic-paper-parser -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill beautifulsoup-academic-paper-parser -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill beautifulsoup-academic-paper-parser -a codex
```

### OpenClaw

```bash
clawhub install beautifulsoup-academic-paper-parser
```

## Source

- Marketplace: https://agentskillexchange.com/skills/beautifulsoup-academic-paper-parser/
