---
title: "Colly Golang Web Scraper and Crawler Framework"
description: "Colly is a fast open-source scraping and crawling framework for Go. It is built for everything from simple page extraction to asynchronous crawlers that process large collections of pages with request callbacks and structured parsing."
verification: "security_reviewed"
source: "https://github.com/gocolly/colly"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gocolly/colly"
  github_stars: 25229
---

# Colly Golang Web Scraper and Crawler Framework

Colly is an open-source Go framework for building web scrapers, spiders, and site crawlers. Maintained under the gocolly organization, it gives developers a compact but capable API for visiting pages, following links, handling request and response callbacks, and extracting structured data from HTML documents. Its official documentation positions it as suitable for both small one-off scrapers and complex asynchronous crawlers that can process millions of pages, which makes it a strong fit for agents that need deterministic scraping workflows rather than browser-heavy automation.

This skill fits jobs where an agent needs to gather data from public websites, traverse page graphs, normalize extracted data, or implement repeatable collection pipelines in Go. Colly supports request filtering, rate limiting, parallelism, event hooks, storage backends, and HTML parsing integrations, so it can be used for catalog collection, documentation harvesting, competitor monitoring, and scheduled data extraction. Because it is code-first and lightweight, it works especially well when the target site can be handled without a full browser engine.

Integration points include Go applications, CLI tools, cron-driven crawlers, queue-backed workers, and downstream pipelines that transform or store extracted data. The upstream docs include installation, getting-started examples, and API reference guidance, while the project’s GitHub repo shows active maintenance, tagged releases, and a permissive Apache 2.0 license. That gives this candidate a clear job-to-be-done and a real, verifiable upstream source for a Research & Scraping skill.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/colly-golang-web-scraper-crawler-framework/)
