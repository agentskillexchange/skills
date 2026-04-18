---
title: "REST API Changelog Tracker"
description: "Tracks breaking changes across REST API versions by diffing OpenAPI specs with oasdiff and monitoring endpoint deprecation headers. Stores version history in SQLite via better-sqlite3."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rest-api-changelog-tracker/"
category:
  - "Library & API Reference"
framework:
  - "Custom Agents"
---

# REST API Changelog Tracker

The REST API Changelog Tracker skill monitors REST APIs for breaking and non-breaking changes across versions. It uses oasdiff to perform structural comparison of OpenAPI specification files, detecting added, removed, and modified endpoints, parameters, and response schemas.

The skill actively monitors live API endpoints for deprecation signals by checking Sunset and Deprecation HTTP headers as defined in RFC 8594. It uses node-fetch to periodically probe configured endpoints and stores response metadata in a local SQLite database via better-sqlite3.

Version history is maintained with full schema snapshots, enabling teams to view the complete API evolution timeline. The skill generates semantic versioning recommendations based on the nature of detected changes, following the semver specification.

Integration features include automatic GitHub Release creation via the GitHub API when breaking changes are detected, Slack notification via webhooks with diff summaries, and Confluence page updates using the Atlassian REST API. The skill supports tracking multiple APIs simultaneously with configurable polling intervals.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/rest-api-changelog-tracker
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/rest-api-changelog-tracker` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-changelog-tracker/)
