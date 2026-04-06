---
name: Firecrawl Web Data API for AI Search Scraping and Crawl Workflows
description: Firecrawl is an open source web data platform for search, scraping, crawling,
  and browser-like page interaction. It gives agents LLM-ready markdown, structured
  JSON, screenshots, and agent-oriented endpoints for turning live websites into usable
  data.
category: "Research &amp; Scraping"
framework: Multi-Framework
verification: listed
source: "https://github.com/firecrawl/firecrawl"
---
# Firecrawl Web Data API for AI Search Scraping and Crawl Workflows

Firecrawl is an open source web data platform for search, scraping, crawling, and browser-like page interaction. It gives agents LLM-ready markdown, structured JSON, screenshots, and agent-oriented endpoints for turning live websites into usable data.

Firecrawl is an open source web data API built for AI applications that need dependable access to live websites. The project offers a unified surface for search, scrape, crawl, map, and browser interaction workflows, which makes it useful for agent systems that need more than a one-off HTML fetch. Rather than forcing developers to stitch together headless browsers, proxy layers, site maps, and post-processing code, Firecrawl packages those concerns into a service and SDKs designed for AI use cases.

The upstream project documents endpoints for search, scrape, interact, crawl, and agent. Its output formats include markdown, structured JSON, screenshots, and extracted page content that is easier to feed into LLM pipelines. Firecrawl also publishes an npm package, @mendable/firecrawl-js, and maintains public docs at docs.firecrawl.dev. The quickstart examples show integrations in Node.js, Python, cURL, CLI, and MCP-style setups.

On ASE, Firecrawl fits teams building research agents, lead enrichment flows, competitive monitoring, site intelligence, and large-scale content extraction. It is especially relevant when an agent must discover pages, follow links, interact with JavaScript-heavy content, and return normalized outputs instead of brittle raw markup. The GitHub repository, docs, public license, npm package, and strong community adoption all make it a good metadata-verified listing candidate.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill firecrawl-web-data-api-ai-search-scraping-crawl-workflows
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill firecrawl-web-data-api-ai-search-scraping-crawl-workflows -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill firecrawl-web-data-api-ai-search-scraping-crawl-workflows -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill firecrawl-web-data-api-ai-search-scraping-crawl-workflows -a codex
```

### OpenClaw

```bash
clawhub install firecrawl-web-data-api-ai-search-scraping-crawl-workflows
```


## Source

- [GitHub](https://github.com/firecrawl/firecrawl)
