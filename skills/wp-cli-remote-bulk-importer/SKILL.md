---
name: "WP-CLI Remote Bulk Importer"
description: "Orchestrates large-scale content imports into WordPress using WP-CLI’s import and post commands over SSH. Handles CSV, JSON, and WXR files with batched inserts, taxonomy mapping, and featured image sideloading via wp media import."
category: "WordPress & CMS"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wp-cli-remote-bulk-importer/"
---

# WP-CLI Remote Bulk Importer

Orchestrates large-scale content imports into WordPress using WP-CLI’s import and post commands over SSH. Handles CSV, JSON, and WXR files with batched inserts, taxonomy mapping, and featured image sideloading via wp media import.

## Overview

Overview

The WP-CLI Remote Bulk Importer skill automates large-scale content migration into WordPress sites accessible over SSH. It leverages `wp post create`, `wp import`, and `wp media import` commands to insert thousands of posts, pages, or custom post type entries from CSV, JSON, or WordPress eXtended RSS (WXR) export files without touching the WordPress admin UI or hitting PHP memory limits.

How It Works

The agent first connects to the remote server via SSH using key-based authentication or a configured password. It validates the WP-CLI installation with `wp --info`, then parses the source file to build a batch queue. For CSV imports, each row maps to a `wp post create` invocation with `--post_type`, `--post_status`, `--post_title`, `--post_content`, and `--meta_input` flags. Taxonomy terms are resolved or created via `wp term create` before assignment with `wp post term set`. Featured images are sideloaded using `wp media import <url> --post_id=<id> --featured_image`.

Output and Integration

The skill produces a detailed import log with created post IDs, failed rows with error messages, and a summary count. It supports dry-run mode via `--dry-run` flags where available, and batches operations in groups of 50 to avoid SSH timeout issues. Integrates with ACF field imports by writing meta via `wp post meta update` and supports multisite with `--url=<site>` targeting. All operations are idempotent — re-running skips already-imported slugs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wp-cli-remote-bulk-importer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wp-cli-remote-bulk-importer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wp-cli-remote-bulk-importer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wp-cli-remote-bulk-importer -a codex
```

### OpenClaw

```bash
clawhub install wp-cli-remote-bulk-importer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wp-cli-remote-bulk-importer/
