---
title: "SEC EDGAR Filing Scraper & Analyzer"
description: "The SEC EDGAR Filing Scraper & Analyzer skill automates the extraction and analysis of SEC regulatory filings for financial research and compliance monitoring. Using the official EDGAR EFTS (full-text search) API and direct filing access endpoints, it retrieves 10-K annual reports, 10-Q quarterly reports, 8-K current reports, and proxy statements for any public company by CIK number or ticker symbol. The python-xbrl parser processes inline XBRL tagged data to extract structured financial statements — income statements, balance sheets, and cash flow statements — with proper handling of GAAP and IFRS taxonomies, extension elements, and dimensional breakdowns. Risk factor extraction uses section detection heuristics and NLP to identify and categorize risk disclosures, tracking changes between filing periods to surface new and removed risks. Executive compensation parsing extracts named executive officer tables, equity award details, and total compensation calculations from DEF 14A proxy statements. The tool generates normalized financial datasets in pandas DataFrames with consistent column naming across companies and filing periods, enabling cross-company comparison and time-series analysis. Automated ratio computation (current ratio, debt-to-equity, ROE, margins) provides instant financial health snapshots. Filing monitoring mode polls EDGAR for new filings matching configurable criteria and triggers analysis pipelines automatically."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sec-edgar-filing-scraper-analyzer/"
framework:
  - "Claude Code"
  - "Multi-Framework"
---

# SEC EDGAR Filing Scraper & Analyzer

The SEC EDGAR Filing Scraper & Analyzer skill automates the extraction and analysis of SEC regulatory filings for financial research and compliance monitoring. Using the official EDGAR EFTS (full-text search) API and direct filing access endpoints, it retrieves 10-K annual reports, 10-Q quarterly reports, 8-K current reports, and proxy statements for any public company by CIK number or ticker symbol. The python-xbrl parser processes inline XBRL tagged data to extract structured financial statements — income statements, balance sheets, and cash flow statements — with proper handling of GAAP and IFRS taxonomies, extension elements, and dimensional breakdowns. Risk factor extraction uses section detection heuristics and NLP to identify and categorize risk disclosures, tracking changes between filing periods to surface new and removed risks. Executive compensation parsing extracts named executive officer tables, equity award details, and total compensation calculations from DEF 14A proxy statements. The tool generates normalized financial datasets in pandas DataFrames with consistent column naming across companies and filing periods, enabling cross-company comparison and time-series analysis. Automated ratio computation (current ratio, debt-to-equity, ROE, margins) provides instant financial health snapshots. Filing monitoring mode polls EDGAR for new filings matching configurable criteria and triggers analysis pipelines automatically.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sec-edgar-filing-scraper-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sec-edgar-filing-scraper-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sec-edgar-filing-scraper-analyzer/)
