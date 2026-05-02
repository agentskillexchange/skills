---
title: "SEC EDGAR Filing Scraper & Analyzer"
description: "Downloads and parses SEC EDGAR filings (10-K, 10-Q, 8-K) using the EDGAR full-text search API and python-xbrl. Extracts financial statements, risk factors, and executive compensation into structured datasets."
verification: "security_reviewed"
source: "https://www.sec.gov/search-filings/edgar-application-programming-interfaces"
category:
  - "Research & Scraping"
framework:
  - "Claude Code"
  - "Multi-Framework"
---

# SEC EDGAR Filing Scraper & Analyzer

The SEC EDGAR Filing Scraper & Analyzer skill automates the extraction and analysis of SEC regulatory filings for financial research and compliance monitoring. Using the official EDGAR EFTS (full-text search) API and direct filing access endpoints, it retrieves 10-K annual reports, 10-Q quarterly reports, 8-K current reports, and proxy statements for any public company by CIK number or ticker symbol. The python-xbrl parser processes inline XBRL tagged data to extract structured financial statements — income statements, balance sheets, and cash flow statements — with proper handling of GAAP and IFRS taxonomies, extension elements, and dimensional breakdowns. Risk factor extraction uses section detection heuristics and NLP to identify and categorize risk disclosures, tracking changes between filing periods to surface new and removed risks. Executive compensation parsing extracts named executive officer tables, equity award details, and total compensation calculations from DEF 14A proxy statements. The tool generates normalized financial datasets in pandas DataFrames with consistent column naming across companies and filing periods, enabling cross-company comparison and time-series analysis. Automated ratio computation (current ratio, debt-to-equity, ROE, margins) provides instant financial health snapshots. Filing monitoring mode polls EDGAR for new filings matching configurable criteria and triggers analysis pipelines automatically.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sec-edgar-filing-scraper-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sec-edgar-filing-scraper-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sec-edgar-filing-scraper-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sec-edgar-filing-scraper-analyzer/)
