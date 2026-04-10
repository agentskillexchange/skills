---
title: "WordPress ACF Field Group Auditor"
description: "Fetches all Advanced Custom Fields field groups and their field definitions via the ACF REST API (/wp-json/acf/v3/), maps field keys to their post types, and produces a structured audit report. Detects orphaned fields, duplicate keys, and field type mismatches across groups."
slug: "wordpress-acf-field-group-auditor"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/wordpress-acf-field-group-auditor/"
listed: true
---

# WordPress ACF Field Group Auditor

Fetches all Advanced Custom Fields field groups and their field definitions via the ACF REST API (/wp-json/acf/v3/), maps field keys to their post types, and produces a structured audit report. Detects orphaned fields, duplicate keys, and field type mismatches across groups.

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
clawhub install wordpress-acf-field-group-auditor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill queries all ACF field groups via the REST API, retrieves field definitions, and analyzes the schema for common issues: fields assigned to deleted post types, duplicate field keys across groups, deprecated field types (relationship fields without return_format set), and groups with zero location rules. Outputs a Markdown audit report suitable for developer handoff.
Use when auditing a site before migration, cleaning up inherited ACF configurations, or generating documentation of custom field schemas. Not for creating or modifying ACF fields — use acf_add_local_field_group() for programmatic registration. Requires ACF Pro 6.0+ and REST API read access enabled in ACF settings.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-acf-field-group-auditor/)
