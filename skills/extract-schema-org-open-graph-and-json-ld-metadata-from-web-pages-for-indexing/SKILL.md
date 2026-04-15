---
title: "Extract schema.org, Open Graph, and JSON-LD metadata from web pages for indexing"
description: "Uses extruct to pull machine-readable metadata from raw HTML so an agent can classify, deduplicate, or enrich pages without brittle full-page parsing. It is best for metadata harvesting workflows, not for crawling an entire site or rendering JavaScript-heavy pages."
verification: security_reviewed
source: "https://github.com/scrapinghub/extruct"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
---

# Extract schema.org, Open Graph, and JSON-LD metadata from web pages for indexing

This ASE entry is built around extruct, the metadata extraction library published from the scrapinghub/extruct repository. The agent behavior is specific: fetch or receive HTML, extract structured metadata formats such as schema.org, Open Graph, JSON-LD, RDFa, microdata, and related signals, then hand those fields into an indexing, enrichment, or QA pipeline. That makes it useful when an agent needs structured page facts without depending on fragile CSS selectors or trying to infer metadata from raw visible text alone.

Use this when the job is metadata harvesting from known pages. An agent might apply it while building a content index, validating publisher markup, enriching a dataset, deduplicating URLs, or preparing inputs for search and recommendation systems. It is the right tool when you already have page HTML or a fetcher in place and the next step is to turn embedded metadata into normalized records. It is not the right tool for full-browser automation or broad site crawling by itself.

The scope boundary is what makes this skill-shaped instead of product-shaped. This is not a generic scraping platform entry, not a headless browser, and not a full crawler card. The job-to-be-done is extracting embedded metadata from pages that have already been fetched. Integration points include Python fetchers, Scrapy-style pipelines, research bots, indexing jobs, link-preview validation, and content quality checks that need structured metadata fields as inputs for downstream decisions.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/extract-schema-org-open-graph-and-json-ld-metadata-from-web-pages-for-indexing
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/extract-schema-org-open-graph-and-json-ld-metadata-from-web-pages-for-indexing` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-schema-org-open-graph-and-json-ld-metadata-from-web-pages-for-indexing/)
