---
title: "Google Search Console Insights Agent"
description: "Extracts search performance data via the Google Search Console API v1 /searchAnalytics/query endpoint. Analyzes CTR, impressions, and position trends with dimension filtering by page, query, device, and country."
slug: "gsc-insights-agent"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gsc-insights-agent/"
listed: true
---

# Google Search Console Insights Agent

Extracts search performance data via the Google Search Console API v1 /searchAnalytics/query endpoint. Analyzes CTR, impressions, and position trends with dimension filtering by page, query, device, and country.

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
clawhub install gsc-insights-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Google Search Console Insights Agent interfaces with the Search Console API v1 to extract and analyze organic search performance data. It queries the /webmasters/v3/sites/{siteUrl}/searchAnalytics/query endpoint with configurable date ranges, dimensions (query, page, device, country, searchAppearance), and dimension filters.
The agent identifies high-impression/low-CTR keywords (position 4-20) as optimization candidates, flagging pages where title tag or meta description improvements could yield significant traffic gains. It tracks position changes over time to detect ranking drops early and correlate them with algorithm updates or content changes.
Supports advanced analysis including: cannibalization detection (multiple pages ranking for the same query), content decay identification (pages losing impressions over 90-day windows), and featured snippet opportunities (queries where you rank 1-5 with question-type search intent). Outputs weekly performance reports with trend visualizations, actionable recommendations prioritized by estimated traffic impact, and GSC API quota management to stay within the 25,000 queries/day limit.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gsc-insights-agent/)
