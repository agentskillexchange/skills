---
name: "Query Monitor WordPress Developer Tools Panel"
description: "Query Monitor is the developer tools panel for WordPress and WooCommerce. It enables debugging of database queries, PHP errors, hooks and actions, block editor blocks, enqueued scripts and stylesheets, HTTP API calls, and more with filtering by plugin or theme."
category: "WordPress & CMS"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/johnbillion/query-monitor"
tool_ecosystem:
  tool: query-monitor
  github_repo: johnbillion/query-monitor
  github_stars: 1743
  license: GPL-2.0
  maintained: true
---
# Query Monitor WordPress Developer Tools Panel

Query Monitor is the developer tools panel for WordPress and WooCommerce. It enables debugging of database queries, PHP errors, hooks and actions, block editor blocks, enqueued scripts and stylesheets, HTTP API calls, and more with filtering by plugin or theme.

## Overview

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

Query Monitor is available as a free plugin on WordPress.org with over 1,700 GitHub stars. Install via WP-CLI with `wp plugin install query-monitor --activate` or download from the WordPress plugin directory. It is licensed under GPL-2.0.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill query-monitor-wordpress-developer-tools-panel
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill query-monitor-wordpress-developer-tools-panel -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill query-monitor-wordpress-developer-tools-panel -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill query-monitor-wordpress-developer-tools-panel -a codex
```

### OpenClaw

```bash
clawhub install query-monitor-wordpress-developer-tools-panel
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-monitor-wordpress-developer-tools-panel/)
