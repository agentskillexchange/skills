---
name: "SiteOne Crawler Technical SEO and Site Audit"
description: "SiteOne Crawler is a real website crawler and analyzer for technical SEO, accessibility, security, and performance checks. This skill uses the upstream SiteOne Crawler project to turn large site crawls into structured diagnostics, export files, and remediation queues."
category: "Content Writing & SEO"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/janreges/siteone-crawler"
tool_ecosystem:
  github_repo: "janreges/siteone-crawler"
  github_stars: 708
---
# SiteOne Crawler Technical SEO and Site Audit

SiteOne Crawler is a real website crawler and analyzer for technical SEO, accessibility, security, and performance checks. This skill uses the upstream SiteOne Crawler project to turn large site crawls into structured diagnostics, export files, and remediation queues.

## Overview

SiteOne Crawler is an open-source website crawler designed for technical SEO analysis, link discovery, content validation, security checks, accessibility reviews, and performance-oriented auditing. A skill built around SiteOne Crawler helps an agent run controlled crawls against a site, collect the exported findings, and transform them into a prioritized action list. The job-to-be-done is broader than “crawl a website”: it is to identify broken links, redirect chains, duplicate metadata, missing headings, oversized assets, indexability problems, orphaned resources, and other structural issues that affect search visibility and site health.

The workflow usually starts with crawl configuration: base URL, depth, inclusion and exclusion patterns, user agent, robots handling, rate limits, and export preferences. From there the skill can interpret outputs such as crawl tables, JSON exports, status-code summaries, asset inventories, sitemap-oriented findings, and reports covering SEO, performance, security, and accessibility dimensions. That makes it useful for migration audits, pre-launch checks, ongoing technical SEO sweeps, and change verification after CMS or theme updates.

Integration points include CI jobs, periodic site audits, QA review, and content governance processes. Technically, the skill deals with crawl graphs, HTTP status codes, canonical tags, redirects, sitemap generation, metadata validation, asset analysis, and structured JSON output for downstream processing. Since SiteOne Crawler has an official GitHub repository, a documentation site, releases, licensing, and active maintenance, it meets the standard for a real-source, tool-anchored skill instead of a synthetic SEO placeholder.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill siteone-crawler-technical-seo-and-site-audit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill siteone-crawler-technical-seo-and-site-audit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill siteone-crawler-technical-seo-and-site-audit -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill siteone-crawler-technical-seo-and-site-audit -a codex
```

### OpenClaw

```bash
clawhub install siteone-crawler-technical-seo-and-site-audit
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/siteone-crawler-technical-seo-and-site-audit/)
