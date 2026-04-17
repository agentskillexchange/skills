---
title: "Google Search Console Insights Agent"
description: "Extracts search performance data via the Google Search Console API v1 /searchAnalytics/query endpoint. Analyzes CTR, impressions, and position trends with dimension filtering by page, query, device, and country."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gsc-insights-agent/"
category:
  - "Content Writing & SEO"
framework:
  - "Custom Agents"
---

# Google Search Console Insights Agent

Google Search Console Insights Agent interfaces with the Search Console API v1 to extract and analyze organic search performance data. It queries the /webmasters/v3/sites/{siteUrl}/searchAnalytics/query endpoint with configurable date ranges, dimensions (query, page, device, country, searchAppearance), and dimension filters.

The agent identifies high-impression/low-CTR keywords (position 4-20) as optimization candidates, flagging pages where title tag or meta description improvements could yield significant traffic gains. It tracks position changes over time to detect ranking drops early and correlate them with algorithm updates or content changes.

Supports advanced analysis including: cannibalization detection (multiple pages ranking for the same query), content decay identification (pages losing impressions over 90-day windows), and featured snippet opportunities (queries where you rank 1-5 with question-type search intent). Outputs weekly performance reports with trend visualizations, actionable recommendations prioritized by estimated traffic impact, and GSC API quota management to stay within the 25,000 queries/day limit.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gsc-insights-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gsc-insights-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gsc-insights-agent/)
