---
title: "Query Monitor WordPress Developer Tools Panel"
description: "Query Monitor is the developer tools panel for WordPress and WooCommerce. It enables debugging of database queries, PHP errors, hooks and actions, block editor blocks, enqueued scripts and stylesheets, HTTP API calls, and more with filtering by plugin or theme."
slug: "query-monitor-wordpress-developer-tools-panel"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/johnbillion/query-monitor"
tool_ecosystem:
  github_repo: "johnbillion/query-monitor"
  github_stars: 1743
listed: true
---

# Query Monitor WordPress Developer Tools Panel

Query Monitor is the developer tools panel for WordPress and WooCommerce. It enables debugging of database queries, PHP errors, hooks and actions, block editor blocks, enqueued scripts and stylesheets, HTTP API calls, and more with filtering by plugin or theme.

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
clawhub install query-monitor-wordpress-developer-tools-panel
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Query Monitor is a comprehensive developer tools panel for WordPress and WooCommerce, created by John Blackbourn. It provides deep insight into what is happening behind the scenes of a WordPress page load, making it an essential tool for WordPress developers, site builders, and performance engineers.
Core Capabilities
Query Monitor intercepts and displays all database queries executed during a request, showing the SQL, caller, component, and execution time. It highlights slow queries, duplicate queries, and queries with errors, and lets you filter by query type, calling function, or originating plugin/theme. This makes it straightforward to identify which plugin or theme is responsible for poor database performance.
PHP Error Reporting
The tool captures PHP warnings, notices, deprecation errors, and doing-it-wrong calls, presenting them with full call stacks and the responsible component. A visible warning appears in the admin toolbar whenever there are errors to address.
Hook and Action Debugging
All hooks fired during a request are displayed along with their attached callbacks, priorities, and originating components. This is invaluable for understanding execution flow and debugging filter/action interactions across plugins.
Template and Block Debugging
Query Monitor shows the active template file, the full template hierarchy, all requested template parts (loaded or not), and available body classes. It fully supports block themes and Full Site Editing, displaying block information from post content and site editor templates.
HTTP API and REST Debugging
Every server-side HTTP request made via the WordPress HTTP API is logged with its response code, call stack, timeout, response size, and timing. Ajax requests include debugging information in response headers, and REST API calls from authenticated users carry detailed performance headers.
Additional Features
Query Monitor also covers enqueued scripts and styles with dependency analysis, user capability checks, rewrite rule matching, redirect tracing via HTTP headers, multisite blog switching, transient monitoring, and environment information. It supports Guzzle HTTP middleware for external request debugging and works with the script modules feature introduced in WordPress 6.5.
Integration
Query Monitor is available as a free plugin on WordPress.org with over 1,700 GitHub stars. Install via WP-CLI with wp plugin install query-monitor --activate or download from the WordPress plugin directory. It is licensed under GPL-2.0.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-monitor-wordpress-developer-tools-panel/)
