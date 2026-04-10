---
title: "SEC EDGAR Filing Scraper & Analyzer"
description: "Downloads and parses SEC EDGAR filings (10-K, 10-Q, 8-K) using the EDGAR full-text search API and python-xbrl. Extracts financial statements, risk factors, and executive compensation into structured datasets."
slug: "sec-edgar-filing-scraper-analyzer"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sec-edgar-filing-scraper-analyzer/"
listed: true
---

# SEC EDGAR Filing Scraper & Analyzer

Downloads and parses SEC EDGAR filings (10-K, 10-Q, 8-K) using the EDGAR full-text search API and python-xbrl. Extracts financial statements, risk factors, and executive compensation into structured datasets.

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
clawhub install sec-edgar-filing-scraper-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SEC EDGAR Filing Scraper & Analyzer skill automates the extraction and analysis of SEC regulatory filings for financial research and compliance monitoring. Using the official EDGAR EFTS (full-text search) API and direct filing access endpoints, it retrieves 10-K annual reports, 10-Q quarterly reports, 8-K current reports, and proxy statements for any public company by CIK number or ticker symbol. The python-xbrl parser processes inline XBRL tagged data to extract structured financial statements — income statements, balance sheets, and cash flow statements — with proper handling of GAAP and IFRS taxonomies, extension elements, and dimensional breakdowns. Risk factor extraction uses section detection heuristics and NLP to identify and categorize risk disclosures, tracking changes between filing periods to surface new and removed risks. Executive compensation parsing extracts named executive officer tables, equity award details, and total compensation calculations from DEF 14A proxy statements. The tool generates normalized financial datasets in pandas DataFrames with consistent column naming across companies and filing periods, enabling cross-company comparison and time-series analysis. Automated ratio computation (current ratio, debt-to-equity, ROE, margins) provides instant financial health snapshots. Filing monitoring mode polls EDGAR for new filings matching configurable criteria and triggers analysis pipelines automatically.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sec-edgar-filing-scraper-analyzer/)
