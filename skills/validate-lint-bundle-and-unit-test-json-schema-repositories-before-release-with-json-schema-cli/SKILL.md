---
title: "Validate lint bundle and unit-test JSON Schema repositories before release with JSON Schema CLI"
description: "Catch broken schemas, bad references, anti-patterns, and inconsistent formatting before a schema repo or contract bundle ships downstream."
verification: "listed"
source: "https://github.com/sourcemeta/jsonschema"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sourcemeta/jsonschema"
  github_stars: 270
  npm_package: "@sourcemeta/jsonschema"
  npm_weekly_downloads: 27164
---

# Validate lint bundle and unit-test JSON Schema repositories before release with JSON Schema CLI

Use the JSON Schema CLI when the job is maintaining a repository of JSON Schemas rather than just using JSON Schema as a format. The operator workflow is concrete: validate schemas, lint for anti-patterns, run schema tests against example instances, and bundle references for distribution or CI gating. That scope boundary—schema repository quality control before release—keeps this distinct from a generic SDK or product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/validate-lint-bundle-and-unit-test-json-schema-repositories-before-release-with-json-schema-cli/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/validate-lint-bundle-and-unit-test-json-schema-repositories-before-release-with-json-schema-cli
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/validate-lint-bundle-and-unit-test-json-schema-repositories-before-release-with-json-schema-cli`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-lint-bundle-and-unit-test-json-schema-repositories-before-release-with-json-schema-cli/)
