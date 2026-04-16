---
title: "Beautiful Soup Academic Paper Parser"
description: "Extracts structured citation data from academic repositories using BeautifulSoup4 with lxml parser. Parses DOI metadata, author affiliations, and reference lists from PubMed, arXiv, and Semantic Scholar HTML."
verification: "security_reviewed"
source: "https://pypi.org/project/beautifulsoup4/"
category:
  - "Research &amp; Scraping"
framework:
  - "MCP"
tool_ecosystem:
  license: "MIT License"
---

# Beautiful Soup Academic Paper Parser

This skill extracts structured bibliographic data from academic paper repositories using BeautifulSoup4 with the lxml parser for fast HTML processing. It handles the unique DOM structures of major academic platforms including PubMed, arXiv abstract pages, and Semantic Scholar.

Extraction targets include paper titles, abstract text, author names with affiliations, DOI identifiers, publication dates, journal/conference names, and full reference lists with citation counts. The skill uses CSS selectors and find_all() with regex patterns to handle varying HTML structures across platforms. DOI resolution uses the CrossRef API for metadata enrichment.

Output formats include BibTeX, RIS, and structured JSON following the CSL-JSON schema for compatibility with reference managers like Zotero and Mendeley. Rate limiting respects robots.txt directives and implements polite crawling with configurable delays between requests.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/beautifulsoup-academic-paper-parser/)
