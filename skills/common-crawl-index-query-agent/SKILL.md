---
name: "Common Crawl Index Query Agent"
description: "Queries the Common Crawl Index API for large-scale web archive research and data extraction. Uses the CDX Server API, WARC record parsing with warcio, and the Common Crawl S3 bucket for bulk data access."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/common-crawl-index-query-agent/"
category:
  - "Research &amp; Scraping"
framework:
  - "OpenClaw"
---

# Common Crawl Index Query Agent

The Common Crawl Index Query Agent enables large-scale web research by querying the Common Crawl CDX Server API for historical web page snapshots across petabytes of archived web data. It constructs efficient index queries using URL prefix matching, domain filtering, and MIME type constraints to locate specific WARC records.
The agent retrieves WARC records from the Common Crawl S3 bucket (s3://commoncrawl) using byte-range requests based on offset and length values from CDX API responses. It parses WARC files using the warcio library, extracting HTTP headers and response bodies from warcrecord objects for content analysis.
Advanced features include parallel CDX pagination for high-volume queries across multiple crawl indices, content deduplication using simhash digest values from the CDX API, and temporal analysis by querying across multiple monthly crawl archives (CC-MAIN-YYYY-WW). The agent also integrates with the columnar index format for SQL-like queries via Amazon Athena, and implements robots.txt compliance checking using the urllib.robotparser module against archived robots.txt snapshots.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/common-crawl-index-query-agent/)
