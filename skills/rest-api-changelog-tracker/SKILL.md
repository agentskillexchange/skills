---
name: "REST API Changelog Tracker"
description: "Tracks breaking changes across REST API versions by diffing OpenAPI specs with oasdiff and monitoring endpoint deprecation headers. Stores version history in SQLite via better-sqlite3."
category: "Library & API Reference"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rest-api-changelog-tracker/"
---
# REST API Changelog Tracker

Tracks breaking changes across REST API versions by diffing OpenAPI specs with oasdiff and monitoring endpoint deprecation headers. Stores version history in SQLite via better-sqlite3.

The REST API Changelog Tracker skill monitors REST APIs for breaking and non-breaking changes across versions. It uses oasdiff to perform structural comparison of OpenAPI specification files, detecting added, removed, and modified endpoints, parameters, and response schemas.



The skill actively monitors live API endpoints for deprecation signals by checking Sunset and Deprecation HTTP headers as defined in RFC 8594. It uses node-fetch to periodically probe configured endpoints and stores response metadata in a local SQLite database via better-sqlite3.



Version history is maintained with full schema snapshots, enabling teams to view the complete API evolution timeline. The skill generates semantic versioning recommendations based on the nature of detected changes, following the semver specification.



Integration features include automatic GitHub Release creation via the GitHub API when breaking changes are detected, Slack notification via webhooks with diff summaries, and Confluence page updates using the Atlassian REST API. The skill supports tracking multiple APIs simultaneously with configurable polling intervals.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rest-api-changelog-tracker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rest-api-changelog-tracker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rest-api-changelog-tracker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rest-api-changelog-tracker -a codex
```

### OpenClaw

```bash
clawhub install rest-api-changelog-tracker
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-changelog-tracker/)
