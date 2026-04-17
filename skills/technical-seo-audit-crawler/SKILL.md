---
title: "Technical SEO Audit Crawler"
description: "This skill performs comprehensive technical SEO audits by combining multiple analysis tools. It initiates crawls using Screaming Frog SEO Spider command-line interface with custom extraction rules and configuration files for crawl depth, URL scope, and rendering settings. Lighthouse CI runs automated performance audits using the lighthouse-ci/action with budgets configured for Core Web Vitals thresholds (LCP under 2.5s, FID under 100ms, CLS under 0.1). PageSpeed Insights API v5 provides field data from Chrome User Experience Report alongside lab metrics. The agent analyzes crawl data for technical issues including redirect chains (301/302 sequences), canonical tag conflicts between self-referencing and cross-domain canonicals, orphaned pages without internal links, and mixed content warnings. Hreflang implementation is validated for reciprocal tag presence, x-default fallbacks, and ISO 639-1 language code compliance. XML sitemap validation checks for proper lastmod dates, priority values, and URL inclusion against crawl results. The skill generates prioritized issue reports with estimated traffic impact based on Google Search Console impression data."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/technical-seo-audit-crawler/"
framework:
  - "OpenClaw"
---

# Technical SEO Audit Crawler

This skill performs comprehensive technical SEO audits by combining multiple analysis tools. It initiates crawls using Screaming Frog SEO Spider command-line interface with custom extraction rules and configuration files for crawl depth, URL scope, and rendering settings. Lighthouse CI runs automated performance audits using the lighthouse-ci/action with budgets configured for Core Web Vitals thresholds (LCP under 2.5s, FID under 100ms, CLS under 0.1). PageSpeed Insights API v5 provides field data from Chrome User Experience Report alongside lab metrics. The agent analyzes crawl data for technical issues including redirect chains (301/302 sequences), canonical tag conflicts between self-referencing and cross-domain canonicals, orphaned pages without internal links, and mixed content warnings. Hreflang implementation is validated for reciprocal tag presence, x-default fallbacks, and ISO 639-1 language code compliance. XML sitemap validation checks for proper lastmod dates, priority values, and URL inclusion against crawl results. The skill generates prioritized issue reports with estimated traffic impact based on Google Search Console impression data.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/technical-seo-audit-crawler
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/technical-seo-audit-crawler` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/technical-seo-audit-crawler/)
