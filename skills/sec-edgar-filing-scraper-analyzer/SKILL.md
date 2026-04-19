---
title: "SEC EDGAR Filing Scraper &#038; Analyzer"
description: "The SEC EDGAR Filing Scraper &#038; Analyzer skill automates the extraction and analysis of SEC regulatory filings for financial research and compliance monitoring. Using the official EDGAR EFTS (full-text search) API and direct filing access endpoints, it retrieves 10-K annual reports, 10-Q quarterly reports, 8-K current reports, and proxy statements for any public company by CIK number or ticker symbol. The python-xbrl parser processes inline XBRL tagged data to extract structured financial statements — income statements, balance sheets, and cash flow statements — with proper handling of GAAP and IFRS taxonomies, extension elements, and dimensional breakdowns. Risk factor extraction uses section detection heuristics and NLP to identify and categorize risk disclosures, tracking changes between filing periods to surface new and removed risks. Executive compensation parsing extracts named executive officer tables, equity award details, and total compensation calculations from DEF 14A proxy statements. The tool generates normalized financial datasets in pandas DataFrames with consistent column naming across companies and filing periods, enabling cross-company comparison and time-series analysis. Automated ratio computation (current ratio, debt-to-equity, ROE, margins) provides instant financial health snapshots. Filing monitoring mode polls EDGAR for new filings matching configurable criteria and triggers analysis pipelines automatically."
source: "https://agentskillexchange.com/skills/sec-edgar-filing-scraper-analyzer/"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
  - "Multi-Framework"
---

# SEC EDGAR Filing Scraper &#038; Analyzer

The SEC EDGAR Filing Scraper &#038; Analyzer skill automates the extraction and analysis of SEC regulatory filings for financial research and compliance monitoring. Using the official EDGAR EFTS (full-text search) API and direct filing access endpoints, it retrieves 10-K annual reports, 10-Q quarterly reports, 8-K current reports, and proxy statements for any public company by CIK number or ticker symbol. The python-xbrl parser processes inline XBRL tagged data to extract structured financial statements — income statements, balance sheets, and cash flow statements — with proper handling of GAAP and IFRS taxonomies, extension elements, and dimensional breakdowns. Risk factor extraction uses section detection heuristics and NLP to identify and categorize risk disclosures, tracking changes between filing periods to surface new and removed risks. Executive compensation parsing extracts named executive officer tables, equity award details, and total compensation calculations from DEF 14A proxy statements. The tool generates normalized financial datasets in pandas DataFrames with consistent column naming across companies and filing periods, enabling cross-company comparison and time-series analysis. Automated ratio computation (current ratio, debt-to-equity, ROE, margins) provides instant financial health snapshots. Filing monitoring mode polls EDGAR for new filings matching configurable criteria and triggers analysis pipelines automatically.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sec-edgar-filing-scraper-analyzer/)
