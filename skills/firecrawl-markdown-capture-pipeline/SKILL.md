---
title: Firecrawl Markdown Capture Pipeline
description: Firecrawl Markdown Capture Pipeline is aimed at teams that want readable
  web content, not just raw DOM snapshots. It uses Firecrawl APIs such as /v1/scrape
  , /v1/map , and /v1/crawl to discover pages, fetch them with browser-aware rendering,
  and transform the results into Markdown that is much easier to store, diff, summarize,
  and index. That makes it a strong fit for research systems, internal knowledge bases,
  and agent workflows that need high-quality source text. The skill can separate sitemap
  discovery from deep crawling, control which pages get expanded, and preserve page-level
  metadata so downstream tools know where each document originated. Compared with
  ad hoc scraping, that reduces cleanup time and makes the corpus more suitable for
  retrieval, summarization, and change tracking. It is also useful when sites rely
  on JavaScript rendering that simpler HTTP fetchers miss or fragment badly. Use this
  skill when your priority is clean page capture in Markdown, controlled crawl coverage,
  and a pipeline that turns live websites into durable, machine-friendly research
  assets.
verification: security_reviewed
source: https://github.com/firecrawl/firecrawl
category:
- Research &amp; Scraping
framework:
- Codex
tool_ecosystem:
  github_repo: firecrawl/firecrawl
  github_stars: 102630
---

# Firecrawl Markdown Capture Pipeline

Firecrawl Markdown Capture Pipeline is aimed at teams that want readable web content, not just raw DOM snapshots. It uses Firecrawl APIs such as /v1/scrape , /v1/map , and /v1/crawl to discover pages, fetch them with browser-aware rendering, and transform the results into Markdown that is much easier to store, diff, summarize, and index. That makes it a strong fit for research systems, internal knowledge bases, and agent workflows that need high-quality source text. The skill can separate sitemap discovery from deep crawling, control which pages get expanded, and preserve page-level metadata so downstream tools know where each document originated. Compared with ad hoc scraping, that reduces cleanup time and makes the corpus more suitable for retrieval, summarization, and change tracking. It is also useful when sites rely on JavaScript rendering that simpler HTTP fetchers miss or fragment badly. Use this skill when your priority is clean page capture in Markdown, controlled crawl coverage, and a pipeline that turns live websites into durable, machine-friendly research assets.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/firecrawl-markdown-capture-pipeline/)
