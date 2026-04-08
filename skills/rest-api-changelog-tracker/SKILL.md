---
title: REST API Changelog Tracker
description: The REST API Changelog Tracker skill monitors REST APIs for breaking
  and non-breaking changes across versions. It uses oasdiff to perform structural
  comparison of OpenAPI specification files, detecting added, removed, and modified
  endpoints, parameters, and response schemas. The skill actively monitors live API
  endpoints for deprecation signals by checking Sunset and Deprecation HTTP headers
  as defined in RFC 8594. It uses node-fetch to periodically probe configured endpoints
  and stores response metadata in a local SQLite database via better-sqlite3. Version
  history is maintained with full schema snapshots, enabling teams to view the complete
  API evolution timeline. The skill generates semantic versioning recommendations
  based on the nature of detected changes, following the semver specification. Integration
  features include automatic GitHub Release creation via the GitHub API when breaking
  changes are detected, Slack notification via webhooks with diff summaries, and Confluence
  page updates using the Atlassian REST API. The skill supports tracking multiple
  APIs simultaneously with configurable polling intervals.
verification: security_reviewed
source: https://agentskillexchange.com/skills/rest-api-changelog-tracker/
category:
- Library &amp; API Reference
framework:
- Custom Agents
---

# REST API Changelog Tracker

The REST API Changelog Tracker skill monitors REST APIs for breaking and non-breaking changes across versions. It uses oasdiff to perform structural comparison of OpenAPI specification files, detecting added, removed, and modified endpoints, parameters, and response schemas. The skill actively monitors live API endpoints for deprecation signals by checking Sunset and Deprecation HTTP headers as defined in RFC 8594. It uses node-fetch to periodically probe configured endpoints and stores response metadata in a local SQLite database via better-sqlite3. Version history is maintained with full schema snapshots, enabling teams to view the complete API evolution timeline. The skill generates semantic versioning recommendations based on the nature of detected changes, following the semver specification. Integration features include automatic GitHub Release creation via the GitHub API when breaking changes are detected, Slack notification via webhooks with diff summaries, and Confluence page updates using the Atlassian REST API. The skill supports tracking multiple APIs simultaneously with configurable polling intervals.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-changelog-tracker/)
