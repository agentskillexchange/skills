---
name: "Common Crawl Index Query Agent"
description: "Queries the Common Crawl Index API for large-scale web archive research and data extraction. Uses the CDX Server API, WARC record parsing with warcio, and the Common Crawl S3 bucket for bulk data access."
category: "Research & Scraping"
framework: "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/common-crawl-index-query-agent/"
---

# Common Crawl Index Query Agent

Queries the Common Crawl Index API for large-scale web archive research and data extraction. Uses the CDX Server API, WARC record parsing with warcio, and the Common Crawl S3 bucket for bulk data access.

## Overview

The Common Crawl Index Query Agent enables large-scale web research by querying the Common Crawl CDX Server API for historical web page snapshots across petabytes of archived web data. It constructs efficient index queries using URL prefix matching, domain filtering, and MIME type constraints to locate specific WARC records.

The agent retrieves WARC records from the Common Crawl S3 bucket (s3://commoncrawl) using byte-range requests based on offset and length values from CDX API responses. It parses WARC files using the warcio library, extracting HTTP headers and response bodies from warcrecord objects for content analysis.

Advanced features include parallel CDX pagination for high-volume queries across multiple crawl indices, content deduplication using simhash digest values from the CDX API, and temporal analysis by querying across multiple monthly crawl archives (CC-MAIN-YYYY-WW). The agent also integrates with the columnar index format for SQL-like queries via Amazon Athena, and implements robots.txt compliance checking using the urllib.robotparser module against archived robots.txt snapshots.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill common-crawl-index-query-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill common-crawl-index-query-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill common-crawl-index-query-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill common-crawl-index-query-agent -a codex
```

### OpenClaw

```bash
clawhub install common-crawl-index-query-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/common-crawl-index-query-agent/
