---
name: "Technical SEO Audit Crawler"
description: "Crawls websites for technical SEO issues using Screaming Frog CLI, Lighthouse CI API, and PageSpeed Insights v5. Reports on Core Web Vitals, canonical chains, hreflang conflicts, and XML sitemap validation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/technical-seo-audit-crawler/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "OpenClaw"
---

# Technical SEO Audit Crawler

This skill performs comprehensive technical SEO audits by combining multiple analysis tools. It initiates crawls using Screaming Frog SEO Spider command-line interface with custom extraction rules and configuration files for crawl depth, URL scope, and rendering settings. Lighthouse CI runs automated performance audits using the lighthouse-ci/action with budgets configured for Core Web Vitals thresholds (LCP under 2.5s, FID under 100ms, CLS under 0.1). PageSpeed Insights API v5 provides field data from Chrome User Experience Report alongside lab metrics. The agent analyzes crawl data for technical issues including redirect chains (301/302 sequences), canonical tag conflicts between self-referencing and cross-domain canonicals, orphaned pages without internal links, and mixed content warnings. Hreflang implementation is validated for reciprocal tag presence, x-default fallbacks, and ISO 639-1 language code compliance. XML sitemap validation checks for proper lastmod dates, priority values, and URL inclusion against crawl results. The skill generates prioritized issue reports with estimated traffic impact based on Google Search Console impression data.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/technical-seo-audit-crawler/)
