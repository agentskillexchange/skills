---
title: "Google Search Console Insights Agent"
description: "Google Search Console Insights Agent interfaces with the Search Console API v1 to extract and analyze organic search performance data. It queries the /webmasters/v3/sites/{siteUrl}/searchAnalytics/query endpoint with configurable date ranges, dimensions (query, page, device, country, searchAppearance), and dimension filters. The agent identifies high-impression/low-CTR keywords (position 4-20) as optimization candidates, flagging pages where title tag or meta description improvements could yield significant traffic gains. It tracks position changes over time to detect ranking drops early and correlate them with algorithm updates or content changes. Supports advanced analysis including: cannibalization detection (multiple pages ranking for the same query), content decay identification (pages losing impressions over 90-day windows), and featured snippet opportunities (queries where you rank 1-5 with question-type search intent). Outputs weekly performance reports with trend visualizations, actionable recommendations prioritized by estimated traffic impact, and GSC API quota management to stay within the 25,000 queries/day limit."
source: "https://agentskillexchange.com/skills/gsc-insights-agent/"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Custom Agents"
---

# Google Search Console Insights Agent

Google Search Console Insights Agent interfaces with the Search Console API v1 to extract and analyze organic search performance data. It queries the /webmasters/v3/sites/{siteUrl}/searchAnalytics/query endpoint with configurable date ranges, dimensions (query, page, device, country, searchAppearance), and dimension filters. The agent identifies high-impression/low-CTR keywords (position 4-20) as optimization candidates, flagging pages where title tag or meta description improvements could yield significant traffic gains. It tracks position changes over time to detect ranking drops early and correlate them with algorithm updates or content changes. Supports advanced analysis including: cannibalization detection (multiple pages ranking for the same query), content decay identification (pages losing impressions over 90-day windows), and featured snippet opportunities (queries where you rank 1-5 with question-type search intent). Outputs weekly performance reports with trend visualizations, actionable recommendations prioritized by estimated traffic impact, and GSC API quota management to stay within the 25,000 queries/day limit.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gsc-insights-agent/)
