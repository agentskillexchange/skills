---
title: "Crawlee Web Crawling and Scraping Library by Apify"
description: "Crawlee is Apify’s open source crawling and scraping framework for Node.js. It unifies HTTP scraping and browser automation, adds queues, storage, retries, proxies, and lets developers switch between Playwright, Puppeteer, Cheerio, and JSDOM without rebuilding the whole pipeline."
verification: "security_reviewed"
source: "https://github.com/apify/crawlee"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "apify/crawlee"
  github_stars: 22714
---

# Crawlee Web Crawling and Scraping Library by Apify

Crawlee is an open source web crawling and scraping library from Apify for JavaScript and TypeScript teams that need something more robust than ad hoc scripts. It gives developers a single framework for collecting pages, files, and structured data across both lightweight HTTP requests and full browser automation. In practice, that means one project can start with fast HTTP extraction and then move specific routes to Playwright or Puppeteer when JavaScript rendering, screenshots, or session handling are required.

The library’s core job-to-be-done is reliable extraction at scale. Crawlee includes persistent request queues, retries, routing, storage, proxy rotation, session management, hooks, and autoscaling so a crawler can keep moving without every site-specific edge case turning into custom infrastructure. The project documentation also highlights support for Cheerio and JSDOM, which makes it useful when an agent or internal tool needs to mix low-cost HTML parsing with targeted browser work.

For AI and automation workflows, Crawlee fits naturally into pipelines that collect product catalogs, documentation, site maps, or research corpora before passing the output into downstream analysis. It integrates with Playwright and Puppeteer for browser-based steps, writes datasets and files to disk, and can be run locally or deployed in containerized environments. Teams already using Node.js can install the main package and add Playwright when they need a browser-backed crawler.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-web-crawling-and-scraping-library-by-apify/)
