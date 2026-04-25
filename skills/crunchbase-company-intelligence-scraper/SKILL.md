---
title: "Crunchbase Company Intelligence Scraper"
description: "Extracts company profiles, funding rounds, and investor data using the Crunchbase Enterprise API v4 with autocomplete, search, and entity lookup endpoints. Builds competitive landscape maps with funding timeline visualizations."
verification: "security_reviewed"
source: "https://data.crunchbase.com/docs"
category:
  - "Research & Scraping"
framework:
  - "Custom Agents"
---

# Crunchbase Company Intelligence Scraper

The Crunchbase Company Intelligence Scraper provides structured access to startup and enterprise company data through the Crunchbase Enterprise API v4. The autocomplete endpoint enables fuzzy company name resolution while the search endpoint supports filtered queries across funding amount ranges, industry categories, founding dates, and geographic locations. Entity lookup retrieves comprehensive company profiles including description, employee count estimates, technology stack indicators, and social media presence. Funding round data is extracted with investor attribution, round type classification from pre-seed through IPO, and valuation details where disclosed. The scraper constructs competitive landscape analyses by mapping companies within specific industry verticals, comparing funding trajectories, team sizes, and growth indicators. Investor portfolio analysis identifies active venture capital firms within target sectors and their typical investment stages. Acquisition history tracking maps M&A activity patterns to predict potential consolidation within market segments. Data is normalized into structured formats compatible with CRM import via CSV or direct Salesforce/HubSpot API integration for sales intelligence workflows.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/crunchbase-company-intelligence-scraper/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/crunchbase-company-intelligence-scraper
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/crunchbase-company-intelligence-scraper`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crunchbase-company-intelligence-scraper/)
