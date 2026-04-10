---
title: "SEC EDGAR Financial Filing Parser"
description: "Retrieves and parses SEC EDGAR filings (10-K, 10-Q, 8-K) using the EDGAR Full-Text Search API and company filing API. Extracts XBRL financial data via the SEC XBRL API for structured balance sheet and income statement analysis."
slug: "sec-edgar-financial-filing-parser"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://www.sec.gov/edgar/searchedgar/companysearch"
listed: true
---

# SEC EDGAR Financial Filing Parser

Retrieves and parses SEC EDGAR filings (10-K, 10-Q, 8-K) using the EDGAR Full-Text Search API and company filing API. Extracts XBRL financial data via the SEC XBRL API for structured balance sheet and income statement analysis.

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
clawhub install sec-edgar-financial-filing-parser
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SEC EDGAR Financial Filing Parser automates the extraction and analysis of US public company financial disclosures from the SEC EDGAR database. The company filing API retrieves filing histories filtered by form type including annual reports 10-K, quarterly reports 10-Q, and material event disclosures 8-K. Full-text search across filing content enables discovery of specific risk factors, related party transactions, and management discussion topics across multiple companies simultaneously. XBRL financial data extraction through the SEC XBRL API provides machine-readable access to standardized financial statements including balance sheets, income statements, and cash flow statements with US GAAP taxonomy mapping. The parser handles both inline XBRL and traditional XBRL attachment formats, normalizing data across different reporting taxonomies for cross-company comparison. Filing exhibit extraction retrieves material contracts, legal opinions, and supplementary schedules referenced within main filings. Historical filing comparison identifies year-over-year changes in risk factor disclosures, accounting policy modifications, and segment reporting restructuring. Rate limiting compliance follows SEC EDGAR fair access guidelines with proper User-Agent identification and request throttling.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sec-edgar-financial-filing-parser/)
