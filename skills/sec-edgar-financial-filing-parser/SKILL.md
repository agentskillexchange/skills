---
title: SEC EDGAR Financial Filing Parser
description: The SEC EDGAR Financial Filing Parser automates the extraction and analysis
  of US public company financial disclosures from the SEC EDGAR database. The company
  filing API retrieves filing histories filtered by form type including annual reports
  10-K, quarterly reports 10-Q, and material event disclosures 8-K. Full-text search
  across filing content enables discovery of specific risk factors, related party
  transactions, and management discussion topics across multiple companies simultaneously.
  XBRL financial data extraction through the SEC XBRL API provides machine-readable
  access to standardized financial statements including balance sheets, income statements,
  and cash flow statements with US GAAP taxonomy mapping. The parser handles both
  inline XBRL and traditional XBRL attachment formats, normalizing data across different
  reporting taxonomies for cross-company comparison. Filing exhibit extraction retrieves
  material contracts, legal opinions, and supplementary schedules referenced within
  main filings. Historical filing comparison identifies year-over-year changes in
  risk factor disclosures, accounting policy modifications, and segment reporting
  restructuring. Rate limiting compliance follows SEC EDGAR fair access guidelines
  with proper User-Agent identification and request throttling.
verification: security_reviewed
source: https://www.sec.gov/edgar/searchedgar/companysearch
category:
- Research &amp; Scraping
framework:
- Claude Code
---

# SEC EDGAR Financial Filing Parser

The SEC EDGAR Financial Filing Parser automates the extraction and analysis of US public company financial disclosures from the SEC EDGAR database. The company filing API retrieves filing histories filtered by form type including annual reports 10-K, quarterly reports 10-Q, and material event disclosures 8-K. Full-text search across filing content enables discovery of specific risk factors, related party transactions, and management discussion topics across multiple companies simultaneously. XBRL financial data extraction through the SEC XBRL API provides machine-readable access to standardized financial statements including balance sheets, income statements, and cash flow statements with US GAAP taxonomy mapping. The parser handles both inline XBRL and traditional XBRL attachment formats, normalizing data across different reporting taxonomies for cross-company comparison. Filing exhibit extraction retrieves material contracts, legal opinions, and supplementary schedules referenced within main filings. Historical filing comparison identifies year-over-year changes in risk factor disclosures, accounting policy modifications, and segment reporting restructuring. Rate limiting compliance follows SEC EDGAR fair access guidelines with proper User-Agent identification and request throttling.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sec-edgar-financial-filing-parser/)
