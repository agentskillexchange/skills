---
name: Beautiful Soup Academic Paper Parser
description: Extracts structured citation data from academic repositories using BeautifulSoup4
  with lxml parser. Parses DOI metadata, author affiliations, and reference lists
  from PubMed, arXiv, and Semantic Scholar HTML.
verification: security_reviewed
source: https://agentskillexchange.com/skills/beautifulsoup-academic-paper-parser/
category:
- Research &amp; Scraping
framework:
- MCP
---
# Beautiful Soup Academic Paper Parser

This skill extracts structured bibliographic data from academic paper repositories using BeautifulSoup4 with the lxml parser for fast HTML processing. It handles the unique DOM structures of major academic platforms including PubMed, arXiv abstract pages, and Semantic Scholar.
Extraction targets include paper titles, abstract text, author names with affiliations, DOI identifiers, publication dates, journal/conference names, and full reference lists with citation counts. The skill uses CSS selectors and find_all() with regex patterns to handle varying HTML structures across platforms. DOI resolution uses the CrossRef API for metadata enrichment.
Output formats include BibTeX, RIS, and structured JSON following the CSL-JSON schema for compatibility with reference managers like Zotero and Mendeley. Rate limiting respects robots.txt directives and implements polite crawling with configurable delays between requests.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/beautifulsoup-academic-paper-parser/)
