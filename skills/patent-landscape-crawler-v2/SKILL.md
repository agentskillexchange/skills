---
name: "Patent Landscape Crawler"
description: "Crawls the Google Patents API and USPTO Open Data portal to map patent landscapes for technology domains. Extracts CPC classification codes, assignee networks, and filing trends using the PatentsView API with structured query parameters."
category: "Research & Scraping"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/patent-landscape-crawler-v2/"
---

# Patent Landscape Crawler

Crawls the Google Patents API and USPTO Open Data portal to map patent landscapes for technology domains. Extracts CPC classification codes, assignee networks, and filing trends using the PatentsView API with structured query parameters.

## Overview

Overview

The Patent Landscape Crawler skill automates competitive intelligence gathering from patent databases by querying the Google Patents Public Datasets on BigQuery, the USPTO PatentsView API at `https://api.patentsview.org/patents/query`, and the European Patent Office’s Open Patent Services (OPS) API. It maps the patent landscape for any technology domain by extracting filing trends, top assignees, inventor networks, and Cooperative Patent Classification (CPC) code distributions.

How It Works

The agent accepts a technology topic or seed patent number and expands the search using CPC subclass codes. For PatentsView queries, it constructs JSON query objects with filters on `patent_date`, `assignee_organization`, `cpc_subgroup_id`, and `patent_abstract` keyword matching. Results are paginated using the `page` and `per_page` parameters (max 10,000 results per query). For deeper analysis, the skill queries BigQuery’s `patents-public-data.patents.publications` table using standard SQL with filters on `publication_date`, `country_code`, and full-text search on `abstract_localized`.

Output and Visualization

Generates a patent landscape report in Markdown with sections for filing volume by year, top 20 assignees ranked by patent count, CPC code heatmap showing technology cluster density, key inventor profiles with co-invention networks, and citation analysis identifying foundational patents. Exports structured data as CSV or JSON for import into Tableau, Google Sheets, or Pandas DataFrames. The agent handles API authentication via OAuth2 for OPS and API keys for PatentsView. Includes rate limiting at 30 requests per minute for PatentsView and 2.5 QPS for OPS. Supports incremental crawling by storing the last-processed publication number.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill patent-landscape-crawler-v2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill patent-landscape-crawler-v2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill patent-landscape-crawler-v2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill patent-landscape-crawler-v2 -a codex
```

### OpenClaw

```bash
clawhub install patent-landscape-crawler-v2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/patent-landscape-crawler-v2/
