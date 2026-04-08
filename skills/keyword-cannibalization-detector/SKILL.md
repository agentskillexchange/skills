---
title: Keyword Cannibalization Detector
description: The Keyword Cannibalization Detector identifies and resolves instances
  where multiple pages compete for the same search queries, diluting SEO performance.
  It connects to the Google Search Console API searchAnalytics.query endpoint to pull
  query-level data with page, position, clicks, and impressions dimensions. The agent
  cross-references this data with Semrush position tracking API to identify keywords
  where multiple URLs rank within the top 100 results. It calculates cannibalization
  severity scores based on position volatility, click distribution, and impression
  share between competing pages. The detector generates actionable recommendations
  including 301 redirect maps, canonical tag suggestions, content merge plans, and
  internal link restructuring using a PageRank-inspired link equity model. It integrates
  with the Ahrefs Batch Analysis API to assess backlink profiles of competing pages
  and determine which URL should be the canonical target. The agent monitors cannibalization
  trends over time using BigQuery exports from Search Console and generates weekly
  reports via the Google Sheets API. Supports WordPress sites through direct WP REST
  API integration for implementing canonical tags and redirect rules via the Redirection
  plugin API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/keyword-cannibalization-detector/
category:
- Content Writing &amp; SEO
framework:
- Claude Code
---

# Keyword Cannibalization Detector

The Keyword Cannibalization Detector identifies and resolves instances where multiple pages compete for the same search queries, diluting SEO performance. It connects to the Google Search Console API searchAnalytics.query endpoint to pull query-level data with page, position, clicks, and impressions dimensions. The agent cross-references this data with Semrush position tracking API to identify keywords where multiple URLs rank within the top 100 results. It calculates cannibalization severity scores based on position volatility, click distribution, and impression share between competing pages. The detector generates actionable recommendations including 301 redirect maps, canonical tag suggestions, content merge plans, and internal link restructuring using a PageRank-inspired link equity model. It integrates with the Ahrefs Batch Analysis API to assess backlink profiles of competing pages and determine which URL should be the canonical target. The agent monitors cannibalization trends over time using BigQuery exports from Search Console and generates weekly reports via the Google Sheets API. Supports WordPress sites through direct WP REST API integration for implementing canonical tags and redirect rules via the Redirection plugin API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keyword-cannibalization-detector/)
