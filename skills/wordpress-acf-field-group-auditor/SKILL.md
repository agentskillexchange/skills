---
title: "WordPress ACF Field Group Auditor"
description: "Fetches all Advanced Custom Fields field groups and their field definitions via the ACF REST API (/wp-json/acf/v3/), maps field keys to their post types, and produces a structured audit report. Detects orphaned fields, duplicate keys, and field type mismatches across groups."
verification: security_reviewed
source: "https://github.com/WordPress/WordPress"
category:
  - "WordPress & CMS"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "wordpress/wordpress"
  github_stars: 21027
---

# WordPress ACF Field Group Auditor

Fetches all Advanced Custom Fields field groups and their field definitions via the ACF REST API (/wp-json/acf/v3/), maps field keys to their post types, and produces a structured audit report. Detects orphaned fields, duplicate keys, and field type mismatches across groups.

This skill queries all ACF field groups via the REST API, retrieves field definitions, and analyzes the schema for common issues: fields assigned to deleted post types, duplicate field keys across groups, deprecated field types (relationship fields without return_format set), and groups with zero location rules. Outputs a Markdown audit report suitable for developer handoff.

Use when auditing a site before migration, cleaning up inherited ACF configurations, or generating documentation of custom field schemas. Not for creating or modifying ACF fields — use acf_add_local_field_group() for programmatic registration. Requires ACF Pro 6.0+ and REST API read access enabled in ACF settings.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wordpress-acf-field-group-auditor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/wordpress-acf-field-group-auditor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-acf-field-group-auditor/)
