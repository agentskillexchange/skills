---
title: "SEC EDGAR Financial Filing Parser"
description: "The SEC EDGAR Financial Filing Parser automates the extraction and analysis of US public company financial disclosures from the SEC EDGAR database. The company filing API retrieves filing histories filtered by form type including annual reports 10-K, quarterly reports 10-Q, and material event disclosures 8-K. Full-text search across filing content enables discovery of specific risk factors, related party transactions, and management discussion topics across multiple companies simultaneously. XBRL financial data extraction through the SEC XBRL API provides machine-readable access to standardized financial statements including balance sheets, income statements, and cash flow statements with US GAAP taxonomy mapping. The parser handles both inline XBRL and traditional XBRL attachment formats, normalizing data across different reporting taxonomies for cross-company comparison. Filing exhibit extraction retrieves material contracts, legal opinions, and supplementary schedules referenced within main filings. Historical filing comparison identifies year-over-year changes in risk factor disclosures, accounting policy modifications, and segment reporting restructuring. Rate limiting compliance follows SEC EDGAR fair access guidelines with proper User-Agent identification and request throttling."
source: "https://www.sec.gov/edgar/searchedgar/companysearch"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
---

# SEC EDGAR Financial Filing Parser

The SEC EDGAR Financial Filing Parser automates the extraction and analysis of US public company financial disclosures from the SEC EDGAR database. The company filing API retrieves filing histories filtered by form type including annual reports 10-K, quarterly reports 10-Q, and material event disclosures 8-K. Full-text search across filing content enables discovery of specific risk factors, related party transactions, and management discussion topics across multiple companies simultaneously. XBRL financial data extraction through the SEC XBRL API provides machine-readable access to standardized financial statements including balance sheets, income statements, and cash flow statements with US GAAP taxonomy mapping. The parser handles both inline XBRL and traditional XBRL attachment formats, normalizing data across different reporting taxonomies for cross-company comparison. Filing exhibit extraction retrieves material contracts, legal opinions, and supplementary schedules referenced within main filings. Historical filing comparison identifies year-over-year changes in risk factor disclosures, accounting policy modifications, and segment reporting restructuring. Rate limiting compliance follows SEC EDGAR fair access guidelines with proper User-Agent identification and request throttling.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sec-edgar-financial-filing-parser/)
