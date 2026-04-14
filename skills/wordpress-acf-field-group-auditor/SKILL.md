---
title: "WordPress ACF Field Group Auditor"
description: "Fetches all Advanced Custom Fields field groups and their field definitions via the ACF REST API (/wp-json/acf/v3/), maps field keys to their post types, and produces a structured audit report. Detects orphaned fields, duplicate keys, and field type mismatches across groups."
verification: security_reviewed
source: "https://github.com/WordPress/WordPress"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
---

# WordPress ACF Field Group Auditor

Fetches all Advanced Custom Fields field groups and their field definitions via the ACF REST API (/wp-json/acf/v3/), maps field keys to their post types, and produces a structured audit report. Detects orphaned fields, duplicate keys, and field type mismatches across groups.

This skill queries all ACF field groups via the REST API, retrieves field definitions, and analyzes the schema for common issues: fields assigned to deleted post types, duplicate field keys across groups, deprecated field types (relationship fields without return_format set), and groups with zero location rules. Outputs a Markdown audit report suitable for developer handoff.

Use when auditing a site before migration, cleaning up inherited ACF configurations, or generating documentation of custom field schemas. Not for creating or modifying ACF fields — use acf_add_local_field_group() for programmatic registration. Requires ACF Pro 6.0+ and REST API read access enabled in ACF settings.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-acf-field-group-auditor/)
