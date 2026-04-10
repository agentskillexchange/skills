---
title: "ElasticPress WordPress Elasticsearch Integration Plugin by 10up"
description: "ElasticPress supercharges WordPress search and queries by integrating Elasticsearch, enabling fast content relevancy analysis, faceted search, WooCommerce product filtering, and autosuggest across large content libraries."
slug: "elasticpress-wordpress-elasticsearch-integration-10up"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/10up/ElasticPress"
listed: true
---

# ElasticPress WordPress Elasticsearch Integration Plugin by 10up

ElasticPress supercharges WordPress search and queries by integrating Elasticsearch, enabling fast content relevancy analysis, faceted search, WooCommerce product filtering, and autosuggest across large content libraries.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install elasticpress-wordpress-elasticsearch-integration-10up
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

ElasticPress is an open-source WordPress plugin by 10up that connects WordPress to Elasticsearch for dramatically faster and more relevant search and content queries. WordPress core search is notoriously slow and returns poor results on sites with large content volumes. ElasticPress solves this by offloading search queries to Elasticsearch and returning results ranked by true content relevancy.
Core Features
The plugin provides multiple feature modules: Instant Results (live search overlay with facets), Autosuggest (real-time search suggestions), WooCommerce integration (product filtering, order search), Related Posts (content recommendations), Custom Search Results (weighting and boosting), Protected Content (search across private/draft posts), and Documents (index and search PDF, Office, and other file contents).
How It Works
ElasticPress syncs WordPress content to an Elasticsearch index. When a search or WP_Query runs, the plugin transparently routes it to Elasticsearch instead of MySQL, then maps the results back. This works with any theme or plugin that uses standard WP_Query. The plugin requires Elasticsearch 5.2+ and WordPress 6.2+.
Developer Integration
ElasticPress exposes extensive hooks and filters. Developers can customize indexing (ep_post_sync_args), modify search queries (ep_formatted_args), and control which post types get indexed. The search algorithm version can be toggled via ep_search_algorithm_version. A React library (elasticpress-react) is available for headless WordPress setups. WP-CLI commands handle bulk indexing and index management. Install from the WordPress.org plugin directory or download from GitHub Releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticpress-wordpress-elasticsearch-integration-10up/)
