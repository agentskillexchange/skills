---
name: "CircleCI Orb Dependency Analyzer"
description: "Analyzes CircleCI orb dependencies using the CircleCI v2 API and Orb Registry API. Maps orb version trees, detects breaking changes, and generates upgrade paths for pinned orb references."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
tool_ecosystem:
  tool: circleci
  github_repo: circleci/circleci-docs
  github_stars: 841
  maintained: true
---
# CircleCI Orb Dependency Analyzer

Analyzes CircleCI orb dependencies using the CircleCI v2 API and Orb Registry API. Maps orb version trees, detects breaking changes, and generates upgrade paths for pinned orb references.

## Overview

The CircleCI Orb Dependency Analyzer skill leverages the CircleCI v2 API and Orb Registry API to map and manage orb dependency trees across projects. It queries the GET /orb/{namespace}/{orb} endpoint to retrieve orb source and version metadata. The skill builds a dependency graph by parsing orb source YAML for nested orb imports and command references. Version constraint resolution follows semantic versioning rules to identify compatible upgrade paths when breaking changes are detected. It uses the CircleCI Pipeline API (GET /project/{project-slug}/pipeline) to find which pipelines reference specific orb versions. The skill generates migration diffs showing exact YAML changes needed for orb upgrades. It cross-references the CircleCI Insights API for build success rates across orb versions to recommend the most stable upgrade targets. Automated PR generation includes updated config.yml with upgraded orb references and changelog summaries pulled from the Orb Registry.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-analyzer -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-dependency-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-analyzer/)
