---
title: Google Search Console Performance Analyzer
description: 'This skill connects to the Google Search Console API to analyze search
  performance data and identify actionable SEO opportunities. It authenticates via
  OAuth 2.0 service account credentials and queries the /webmasters/v3/sites/{siteUrl}/searchAnalytics/query
  endpoint with configurable date ranges, dimensions (query, page, country, device),
  and row limits. The skill performs three core analyses: (1) Declining pages detection—compares
  current period metrics (clicks, impressions, CTR, position) against previous period
  to identify pages with >20% traffic decline, categorizing causes as position drops,
  CTR decreases, or impression losses. (2) Keyword cannibalization detection—groups
  queries by page URL to identify cases where multiple pages compete for the same
  keyword, flagged when 2+ pages rank in positions 1-20 for identical queries with
  similar impressions. (3) CTR optimization—compares actual CTR per position against
  industry benchmark curves (position 1: ~28%, position 2: ~15%, position 3: ~11%)
  to find pages with below-average CTR that could benefit from title/description rewrites.
  The skill generates priority-ranked recommendations: quick wins (high impressions,
  low position, fixable with on-page optimization), content consolidation targets
  (cannibalized keywords to merge), and title tag rewrites (below-benchmark CTR pages).
  Output includes CSV exports for each analysis, trend charts data in JSON format,
  and a markdown executive summary with estimated traffic impact of recommended changes.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/gsc-performance-analyzer-skill/
category:
- Content Writing &amp; SEO
framework:
- Custom Agents
---

# Google Search Console Performance Analyzer

This skill connects to the Google Search Console API to analyze search performance data and identify actionable SEO opportunities. It authenticates via OAuth 2.0 service account credentials and queries the /webmasters/v3/sites/{siteUrl}/searchAnalytics/query endpoint with configurable date ranges, dimensions (query, page, country, device), and row limits. The skill performs three core analyses: (1) Declining pages detection—compares current period metrics (clicks, impressions, CTR, position) against previous period to identify pages with >20% traffic decline, categorizing causes as position drops, CTR decreases, or impression losses. (2) Keyword cannibalization detection—groups queries by page URL to identify cases where multiple pages compete for the same keyword, flagged when 2+ pages rank in positions 1-20 for identical queries with similar impressions. (3) CTR optimization—compares actual CTR per position against industry benchmark curves (position 1: ~28%, position 2: ~15%, position 3: ~11%) to find pages with below-average CTR that could benefit from title/description rewrites. The skill generates priority-ranked recommendations: quick wins (high impressions, low position, fixable with on-page optimization), content consolidation targets (cannibalized keywords to merge), and title tag rewrites (below-benchmark CTR pages). Output includes CSV exports for each analysis, trend charts data in JSON format, and a markdown executive summary with estimated traffic impact of recommended changes.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gsc-performance-analyzer-skill/)
