---
name: "Crunchbase Company Intelligence Scraper"
description: "Extracts company profiles, funding rounds, and investor data using the Crunchbase Enterprise API v4 with autocomplete, search, and entity lookup endpoints. Builds competitive landscape maps with funding timeline visualizations."
category: "Research & Scraping"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/crunchbase-company-intelligence-scraper/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "hubspot"  # from ase_tool_match
  github_stars: 391  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 905578  # from ase_npm_downloads
  github_repo: "HubSpot/hubspot-api-nodejs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Crunchbase Company Intelligence Scraper

Extracts company profiles, funding rounds, and investor data using the Crunchbase Enterprise API v4 with autocomplete, search, and entity lookup endpoints. Builds competitive landscape maps with funding timeline visualizations.

## Overview

The Crunchbase Company Intelligence Scraper provides structured access to startup and enterprise company data through the Crunchbase Enterprise API v4. The autocomplete endpoint enables fuzzy company name resolution while the search endpoint supports filtered queries across funding amount ranges, industry categories, founding dates, and geographic locations. Entity lookup retrieves comprehensive company profiles including description, employee count estimates, technology stack indicators, and social media presence. Funding round data is extracted with investor attribution, round type classification from pre-seed through IPO, and valuation details where disclosed. The scraper constructs competitive landscape analyses by mapping companies within specific industry verticals, comparing funding trajectories, team sizes, and growth indicators. Investor portfolio analysis identifies active venture capital firms within target sectors and their typical investment stages. Acquisition history tracking maps M&A activity patterns to predict potential consolidation within market segments. Data is normalized into structured formats compatible with CRM import via CSV or direct Salesforce/HubSpot API integration for sales intelligence workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill crunchbase-company-intelligence-scraper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill crunchbase-company-intelligence-scraper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill crunchbase-company-intelligence-scraper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill crunchbase-company-intelligence-scraper -a codex
```

### OpenClaw

```bash
clawhub install crunchbase-company-intelligence-scraper
```

## Source

- Marketplace: https://agentskillexchange.com/skills/crunchbase-company-intelligence-scraper/
