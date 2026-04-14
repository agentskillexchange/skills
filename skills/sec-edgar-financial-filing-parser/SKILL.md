---
title: "SEC EDGAR Financial Filing Parser"
description: "Retrieves and parses SEC EDGAR filings (10-K, 10-Q, 8-K) using the EDGAR Full-Text Search API and company filing API. Extracts XBRL financial data via the SEC XBRL API for structured balance sheet and income statement analysis."
verification: security_reviewed
source: "https://www.sec.gov/edgar/searchedgar/companysearch"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
---

# SEC EDGAR Financial Filing Parser

The SEC EDGAR Financial Filing Parser automates the extraction and analysis of US public company financial disclosures from the SEC EDGAR database. The company filing API retrieves filing histories filtered by form type including annual reports 10-K, quarterly reports 10-Q, and material event disclosures 8-K. Full-text search across filing content enables discovery of specific risk factors, related party transactions, and management discussion topics across multiple companies simultaneously. XBRL financial data extraction through the SEC XBRL API provides machine-readable access to standardized financial statements including balance sheets, income statements, and cash flow statements with US GAAP taxonomy mapping. The parser handles both inline XBRL and traditional XBRL attachment formats, normalizing data across different reporting taxonomies for cross-company comparison. Filing exhibit extraction retrieves material contracts, legal opinions, and supplementary schedules referenced within main filings. Historical filing comparison identifies year-over-year changes in risk factor disclosures, accounting policy modifications, and segment reporting restructuring. Rate limiting compliance follows SEC EDGAR fair access guidelines with proper User-Agent identification and request throttling.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sec-edgar-financial-filing-parser/)
