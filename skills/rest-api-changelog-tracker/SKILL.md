---
name: REST API Changelog Tracker
description: Tracks breaking changes across REST API versions by diffing OpenAPI specs
  with oasdiff and monitoring endpoint deprecation headers. Stores version history
  in SQLite via better-sqlite3.
verification: security_reviewed
source: https://agentskillexchange.com/skills/rest-api-changelog-tracker/
category:
- Library &amp; API Reference
framework:
- Custom Agents
---
# REST API Changelog Tracker

The REST API Changelog Tracker skill monitors REST APIs for breaking and non-breaking changes across versions. It uses oasdiff to perform structural comparison of OpenAPI specification files, detecting added, removed, and modified endpoints, parameters, and response schemas.
The skill actively monitors live API endpoints for deprecation signals by checking Sunset and Deprecation HTTP headers as defined in RFC 8594. It uses node-fetch to periodically probe configured endpoints and stores response metadata in a local SQLite database via better-sqlite3.
Version history is maintained with full schema snapshots, enabling teams to view the complete API evolution timeline. The skill generates semantic versioning recommendations based on the nature of detected changes, following the semver specification.
Integration features include automatic GitHub Release creation via the GitHub API when breaking changes are detected, Slack notification via webhooks with diff summaries, and Confluence page updates using the Atlassian REST API. The skill supports tracking multiple APIs simultaneously with configurable polling intervals.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-changelog-tracker/)
