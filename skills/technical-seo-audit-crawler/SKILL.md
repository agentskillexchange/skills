---
title: "Technical SEO Audit Crawler"
description: "Crawls websites for technical SEO issues using Screaming Frog CLI, Lighthouse CI API, and PageSpeed Insights v5. Reports on Core Web Vitals, canonical chains, hreflang conflicts, and XML sitemap validation."
slug: "technical-seo-audit-crawler"
category:
  - "Content Writing &amp; SEO"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/technical-seo-audit-crawler/"
---

# Technical SEO Audit Crawler

Crawls websites for technical SEO issues using Screaming Frog CLI, Lighthouse CI API, and PageSpeed Insights v5. Reports on Core Web Vitals, canonical chains, hreflang conflicts, and XML sitemap validation.

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
clawhub install technical-seo-audit-crawler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill performs comprehensive technical SEO audits by combining multiple analysis tools. It initiates crawls using Screaming Frog SEO Spider command-line interface with custom extraction rules and configuration files for crawl depth, URL scope, and rendering settings. Lighthouse CI runs automated performance audits using the lighthouse-ci/action with budgets configured for Core Web Vitals thresholds (LCP under 2.5s, FID under 100ms, CLS under 0.1). PageSpeed Insights API v5 provides field data from Chrome User Experience Report alongside lab metrics. The agent analyzes crawl data for technical issues including redirect chains (301/302 sequences), canonical tag conflicts between self-referencing and cross-domain canonicals, orphaned pages without internal links, and mixed content warnings. Hreflang implementation is validated for reciprocal tag presence, x-default fallbacks, and ISO 639-1 language code compliance. XML sitemap validation checks for proper lastmod dates, priority values, and URL inclusion against crawl results. The skill generates prioritized issue reports with estimated traffic impact based on Google Search Console impression data.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/technical-seo-audit-crawler/)
