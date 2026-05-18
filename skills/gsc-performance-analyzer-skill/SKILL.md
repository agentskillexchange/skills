---
name: "Google Search Console Performance Analyzer"
slug: "gsc-performance-analyzer-skill"
description: "Pulls search analytics from Google Search Console's /searchanalytics/query API to identify declining pages and keyword cannibalization. Calculates CTR optimization opportunities by comparing actual vs expected click-through rates."
verification: "listed"
source: "https://developers.google.com/webmaster-tools/v1/searchanalytics/query"
author: "Google"
category: "Content Writing & SEO"
framework: "Custom Agents"
---

# Google Search Console Performance Analyzer

Pulls search analytics from Google Search Console's /searchanalytics/query API to identify declining pages and keyword cannibalization. Calculates CTR optimization opportunities by comparing actual vs expected click-through rates.

## Prerequisites

Google account, Search Console property access, Google Cloud project, and Search Console API enabled

## Installation

Requirements and caveats from upstream:
- Access a Python sample and JSON POST examples for easy API integration.
- Requires authorization
- See the python sample for calling this method.

Basic usage or getting-started notes:
- JSON POST Example:
- POST https://www.googleapis.com/webmasters/v3/sites/https%3A%2F%2Fwww.example.com%2F/searchAnalytics/query?key={MY_API_KEY}
- http://www.example.com/ (for a URL-prefix property) or

- Source: https://developers.google.com/webmaster-tools/v1/searchanalytics/query

## Documentation

- https://developers.google.com/webmaster-tools/v1/searchanalytics/query

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gsc-performance-analyzer-skill/)
