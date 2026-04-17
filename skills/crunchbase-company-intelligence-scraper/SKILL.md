---
title: "Crunchbase Company Intelligence Scraper"
description: "The Crunchbase Company Intelligence Scraper provides structured access to startup and enterprise company data through the Crunchbase Enterprise API v4. The autocomplete endpoint enables fuzzy company name resolution while the search endpoint supports filtered queries across funding amount ranges, industry categories, founding dates, and geographic locations. Entity lookup retrieves comprehensive company profiles including description, employee count estimates, technology stack indicators, and social media presence. Funding round data is extracted with investor attribution, round type classification from pre-seed through IPO, and valuation details where disclosed. The scraper constructs competitive landscape analyses by mapping companies within specific industry verticals, comparing funding trajectories, team sizes, and growth indicators. Investor portfolio analysis identifies active venture capital firms within target sectors and their typical investment stages. Acquisition history tracking maps M&A activity patterns to predict potential consolidation within market segments. Data is normalized into structured formats compatible with CRM import via CSV or direct Salesforce/HubSpot API integration for sales intelligence workflows."
verification: security_reviewed
source: "https://data.crunchbase.com/docs"
framework:
  - "Custom Agents"
---

# Crunchbase Company Intelligence Scraper

The Crunchbase Company Intelligence Scraper provides structured access to startup and enterprise company data through the Crunchbase Enterprise API v4. The autocomplete endpoint enables fuzzy company name resolution while the search endpoint supports filtered queries across funding amount ranges, industry categories, founding dates, and geographic locations. Entity lookup retrieves comprehensive company profiles including description, employee count estimates, technology stack indicators, and social media presence. Funding round data is extracted with investor attribution, round type classification from pre-seed through IPO, and valuation details where disclosed. The scraper constructs competitive landscape analyses by mapping companies within specific industry verticals, comparing funding trajectories, team sizes, and growth indicators. Investor portfolio analysis identifies active venture capital firms within target sectors and their typical investment stages. Acquisition history tracking maps M&A activity patterns to predict potential consolidation within market segments. Data is normalized into structured formats compatible with CRM import via CSV or direct Salesforce/HubSpot API integration for sales intelligence workflows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/crunchbase-company-intelligence-scraper
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/crunchbase-company-intelligence-scraper` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crunchbase-company-intelligence-scraper/)
