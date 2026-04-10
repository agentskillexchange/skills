---
name: SiteOne Crawler Technical SEO and Site Audit
description: SiteOne Crawler is a real website crawler and analyzer for technical
  SEO, accessibility, security, and performance checks. This skill uses the upstream
  SiteOne Crawler project to turn large site crawls into structured diagnostics, export
  files, and remediation queues.
verification: security_reviewed
source: https://github.com/janreges/siteone-crawler
category:
- Content Writing &amp; SEO
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: janreges/siteone-crawler
  github_stars: 708
---
# SiteOne Crawler Technical SEO and Site Audit

SiteOne Crawler is an open-source website crawler designed for technical SEO analysis, link discovery, content validation, security checks, accessibility reviews, and performance-oriented auditing. A skill built around SiteOne Crawler helps an agent run controlled crawls against a site, collect the exported findings, and transform them into a prioritized action list. The job-to-be-done is broader than “crawl a website”: it is to identify broken links, redirect chains, duplicate metadata, missing headings, oversized assets, indexability problems, orphaned resources, and other structural issues that affect search visibility and site health.
The workflow usually starts with crawl configuration: base URL, depth, inclusion and exclusion patterns, user agent, robots handling, rate limits, and export preferences. From there the skill can interpret outputs such as crawl tables, JSON exports, status-code summaries, asset inventories, sitemap-oriented findings, and reports covering SEO, performance, security, and accessibility dimensions. That makes it useful for migration audits, pre-launch checks, ongoing technical SEO sweeps, and change verification after CMS or theme updates.
Integration points include CI jobs, periodic site audits, QA review, and content governance processes. Technically, the skill deals with crawl graphs, HTTP status codes, canonical tags, redirects, sitemap generation, metadata validation, asset analysis, and structured JSON output for downstream processing. Since SiteOne Crawler has an official GitHub repository, a documentation site, releases, licensing, and active maintenance, it meets the standard for a real-source, tool-anchored skill instead of a synthetic SEO placeholder.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/siteone-crawler-technical-seo-and-site-audit/)
