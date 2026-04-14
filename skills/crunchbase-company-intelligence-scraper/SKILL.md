---
title: "Crunchbase Company Intelligence Scraper"
description: "Extracts company profiles, funding rounds, and investor data using the Crunchbase Enterprise API v4 with autocomplete, search, and entity lookup endpoints. Builds competitive landscape maps with funding timeline visualizations."
verification: security_reviewed
source: "https://data.crunchbase.com/docs"
category:
  - "Research &amp; Scraping"
framework:
  - "Custom Agents"
---

# Crunchbase Company Intelligence Scraper

The Crunchbase Company Intelligence Scraper provides structured access to startup and enterprise company data through the Crunchbase Enterprise API v4. The autocomplete endpoint enables fuzzy company name resolution while the search endpoint supports filtered queries across funding amount ranges, industry categories, founding dates, and geographic locations. Entity lookup retrieves comprehensive company profiles including description, employee count estimates, technology stack indicators, and social media presence. Funding round data is extracted with investor attribution, round type classification from pre-seed through IPO, and valuation details where disclosed. The scraper constructs competitive landscape analyses by mapping companies within specific industry verticals, comparing funding trajectories, team sizes, and growth indicators. Investor portfolio analysis identifies active venture capital firms within target sectors and their typical investment stages. Acquisition history tracking maps M&A activity patterns to predict potential consolidation within market segments. Data is normalized into structured formats compatible with CRM import via CSV or direct Salesforce/HubSpot API integration for sales intelligence workflows.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crunchbase-company-intelligence-scraper/)
