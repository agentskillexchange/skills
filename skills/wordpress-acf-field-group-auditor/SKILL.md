---
name: "WordPress ACF Field Group Auditor"
description: "Fetches all Advanced Custom Fields field groups and their field definitions via the ACF REST API (/wp-json/acf/v3/), maps field keys to their post types, and produces a structured audit report. Detects orphaned fields, duplicate keys, and field type mismatches across groups."
category: "WordPress & CMS"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/wordpress-acf-field-group-auditor/"
tool_ecosystem:
  tool: wordpress
  github_stars: 20976
  github_repo: WordPress/WordPress
  maintained: true
---

# WordPress ACF Field Group Auditor

Fetches all Advanced Custom Fields field groups and their field definitions via the ACF REST API (/wp-json/acf/v3/), maps field keys to their post types, and produces a structured audit report. Detects orphaned fields, duplicate keys, and field type mismatches across groups.

## Overview

Fetches all Advanced Custom Fields field groups and their field definitions via the ACF REST API (/wp-json/acf/v3/), maps field keys to their post types, and produces a structured audit report. Detects orphaned fields, duplicate keys, and field type mismatches across groups.

This skill queries all ACF field groups via the REST API, retrieves field definitions, and analyzes the schema for common issues: fields assigned to deleted post types, duplicate field keys across groups, deprecated field types (relationship fields without return_format set), and groups with zero location rules. Outputs a Markdown audit report suitable for developer handoff.

Use when auditing a site before migration, cleaning up inherited ACF configurations, or generating documentation of custom field schemas. Not for creating or modifying ACF fields — use acf_add_local_field_group() for programmatic registration. Requires ACF Pro 6.0+ and REST API read access enabled in ACF settings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-acf-field-group-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-acf-field-group-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-acf-field-group-auditor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-acf-field-group-auditor -a codex
```

### OpenClaw

```bash
clawhub install wordpress-acf-field-group-auditor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wordpress-acf-field-group-auditor/
