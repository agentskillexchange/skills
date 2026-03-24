---
name: "WordPress REST Batch Publisher with Application Passwords"
description: "Publishes posts, pages, or custom post types through the WordPress REST API using Application Password authentication, field mapping, and retry-safe batching. It is designed for migrations, content syndication, AI-assisted drafting, and controlled bulk imports that need auditability."
category: "WordPress & CMS"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wordpress-rest-batch-publisher-application-passwords-20260324/"
---

# WordPress REST Batch Publisher with Application Passwords

Publishes posts, pages, or custom post types through the WordPress REST API using Application Password authentication, field mapping, and retry-safe batching. It is designed for migrations, content syndication, AI-assisted drafting, and controlled bulk imports that need auditability.

## Overview

This skill automates reliable bulk publishing into WordPress through the **REST API** with **Application Passwords** instead of fragile browser automation. It takes structured content records, maps them onto post fields and taxonomies, handles featured media relationships, and creates or updates resources in repeatable batches. That is valuable for editorial imports, headless CMS sync jobs, static-to-WordPress migrations, and AI-assisted pipelines where content is generated elsewhere but needs to land in a standard WordPress instance. The skill documents required endpoints, payload structure, auth headers, pagination, and error handling so the process remains transparent and supportable.

Operationally, it can validate slugs, detect duplicates, resolve category or tag IDs, throttle request bursts, and retry transient 429 or 5xx failures. It works well with Node, Python, `curl`, Postman, GitHub Actions, Makefiles, Docker jobs, or queue workers that process content from a webhook or database export. Outputs typically include a publish log, per-record success or failure summaries, created post IDs, and reconciliation data that maps source IDs to WordPress IDs. Integration points extend to image sideloading, revision capture, translation workflows, and downstream search indexing. The result is not just a batch uploader, but a durable publishing pipeline that can be audited, resumed, and embedded inside larger content operations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-rest-batch-publisher-application-passwords-20260324
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-rest-batch-publisher-application-passwords-20260324 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-rest-batch-publisher-application-passwords-20260324 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-rest-batch-publisher-application-passwords-20260324 -a codex
```

### OpenClaw

```bash
clawhub install wordpress-rest-batch-publisher-application-passwords-20260324
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wordpress-rest-batch-publisher-application-passwords-20260324/
