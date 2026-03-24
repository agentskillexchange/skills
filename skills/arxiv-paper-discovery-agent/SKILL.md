---
name: "Arxiv Paper Discovery Agent"
description: "Searches and filters academic papers from the arXiv API by subject category, date range, and keyword relevance. Parses Atom XML feeds, extracts BibTeX metadata, and generates structured reading lists with citation counts from Semantic Scholar."
category: "Research & Scraping"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/arxiv-paper-discovery-agent/"
---

# Arxiv Paper Discovery Agent

Searches and filters academic papers from the arXiv API by subject category, date range, and keyword relevance. Parses Atom XML feeds, extracts BibTeX metadata, and generates structured reading lists with citation counts from Semantic Scholar.

## Overview

Overview

The Arxiv Paper Discovery Agent skill enables automated literature search and monitoring across arXiv’s repository of over 2.4 million scholarly articles. It queries the arXiv API’s Atom feed endpoint at `http://export.arxiv.org/api/query` with structured search parameters including subject categories (cs.AI, cs.CL, stat.ML, etc.), author names, title keywords, and abstract content filters using the `search_query` syntax with boolean operators (AND, OR, ANDNOT).

How It Works

The agent constructs API queries using arXiv’s field-specific prefix syntax — `ti:` for title, `au:` for author, `abs:` for abstract, and `cat:` for category. Results are returned as Atom XML, which the skill parses with an XML parser to extract paper ID, title, authors, abstract, published date, updated date, primary category, and PDF/HTML links. For each discovered paper, the agent optionally enriches the record by querying the Semantic Scholar API at `https://api.semanticscholar.org/graph/v1/paper/arXiv:<id>` to fetch citation counts, influential citation count, and venue information.

Output and Integration

The skill generates a structured reading list in Markdown or JSON format, sorted by relevance score or recency. Each entry includes the paper title, author list, abstract summary (first 200 characters), arXiv ID with hyperlink, BibTeX citation block, citation count, and primary category tags. Supports scheduled monitoring by storing the last-seen paper ID and only returning new entries on subsequent runs. Rate-limits API calls to 1 request per 3 seconds per arXiv’s usage policy. Integrates with Zotero, Notion databases, and Obsidian vaults for automated reference management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill arxiv-paper-discovery-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill arxiv-paper-discovery-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill arxiv-paper-discovery-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill arxiv-paper-discovery-agent -a codex
```

### OpenClaw

```bash
clawhub install arxiv-paper-discovery-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/arxiv-paper-discovery-agent/
