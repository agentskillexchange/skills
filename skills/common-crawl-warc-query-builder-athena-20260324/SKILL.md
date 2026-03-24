---
name: "Common Crawl WARC Query Builder for Athena"
description: "Builds repeatable AWS Athena queries against Common Crawl indexes and WARC/WET references so researchers can locate domains, paths, and capture dates before downloading terabytes of data. It helps agents pivot from broad web discovery into targeted extraction jobs using S3, SQL, and parquet-friendly exports."
category: "Research & Scraping"
framework: "ChatGPT Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/common-crawl-warc-query-builder-athena-20260324/"
---

# Common Crawl WARC Query Builder for Athena

Builds repeatable AWS Athena queries against Common Crawl indexes and WARC/WET references so researchers can locate domains, paths, and capture dates before downloading terabytes of data. It helps agents pivot from broad web discovery into targeted extraction jobs using S3, SQL, and parquet-friendly exports.

## Overview

This skill is built for researchers who need structured access to **Common Crawl** without manually wading through the whole corpus. It creates Athena-ready SQL for the Common Crawl index tables, filters by domain, path prefixes, status code, MIME type, and crawl date, then turns matching records into a practical worklist of WARC or WET objects to fetch. Instead of downloading huge archives blindly, the skill narrows the search space first and documents exactly which captures are worth pulling. It is useful for web-scale discovery, historical site analysis, content drift studies, SEO datasets, and legal or archival review where reproducibility matters.

The workflow combines AWS Athena, S3 object references, and optional downstream tools such as `warcio`, Apache Spark, DuckDB, or a Python CLI that streams individual WARC records. It can generate parameterized SQL templates, capture date windows, host-level allowlists, and export manifests in CSV or JSONL for later batch jobs. When paired with Airflow, Prefect, dbt, or a containerized Docker workflow, the skill becomes a repeatable extraction stage rather than an ad hoc query. The output usually includes Athena SQL, a manifest of matching crawl files, estimated result counts, and optional shell commands for downloading or parsing the selected records. That makes it a practical bridge between a massive public dataset and a smaller, verifiable research pipeline.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill common-crawl-warc-query-builder-athena-20260324
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill common-crawl-warc-query-builder-athena-20260324 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill common-crawl-warc-query-builder-athena-20260324 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill common-crawl-warc-query-builder-athena-20260324 -a codex
```

### OpenClaw

```bash
clawhub install common-crawl-warc-query-builder-athena-20260324
```

## Source

- Marketplace: https://agentskillexchange.com/skills/common-crawl-warc-query-builder-athena-20260324/
