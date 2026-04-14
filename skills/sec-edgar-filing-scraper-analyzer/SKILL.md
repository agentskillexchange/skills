---
title: "SEC EDGAR Filing Scraper & Analyzer"
description: "Downloads and parses SEC EDGAR filings (10-K, 10-Q, 8-K) using the EDGAR full-text search API and python-xbrl. Extracts financial statements, risk factors, and executive compensation into structured datasets."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sec-edgar-filing-scraper-analyzer/"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
  - "Multi-Framework"
---

# SEC EDGAR Filing Scraper & Analyzer

The SEC EDGAR Filing Scraper & Analyzer skill automates the extraction and analysis of SEC regulatory filings for financial research and compliance monitoring. Using the official EDGAR EFTS (full-text search) API and direct filing access endpoints, it retrieves 10-K annual reports, 10-Q quarterly reports, 8-K current reports, and proxy statements for any public company by CIK number or ticker symbol. The python-xbrl parser processes inline XBRL tagged data to extract structured financial statements — income statements, balance sheets, and cash flow statements — with proper handling of GAAP and IFRS taxonomies, extension elements, and dimensional breakdowns. Risk factor extraction uses section detection heuristics and NLP to identify and categorize risk disclosures, tracking changes between filing periods to surface new and removed risks. Executive compensation parsing extracts named executive officer tables, equity award details, and total compensation calculations from DEF 14A proxy statements. The tool generates normalized financial datasets in pandas DataFrames with consistent column naming across companies and filing periods, enabling cross-company comparison and time-series analysis. Automated ratio computation (current ratio, debt-to-equity, ROE, margins) provides instant financial health snapshots. Filing monitoring mode polls EDGAR for new filings matching configurable criteria and triggers analysis pipelines automatically.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sec-edgar-filing-scraper-analyzer/)
