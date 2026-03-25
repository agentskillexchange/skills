---
name: "REST API Changelog Tracker"
description: "Tracks breaking changes across REST API versions by diffing OpenAPI specs with oasdiff and monitoring endpoint deprecation headers. Stores version history in SQLite via better-sqlite3."
category: "Library & API Reference"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/rest-api-changelog-tracker/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2900  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# REST API Changelog Tracker

Tracks breaking changes across REST API versions by diffing OpenAPI specs with oasdiff and monitoring endpoint deprecation headers. Stores version history in SQLite via better-sqlite3.

## Overview

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

- Marketplace: https://agentskillexchange.com/skills/rest-api-changelog-tracker/
