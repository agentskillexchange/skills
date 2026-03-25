---
name: "CircleCI Orb Dependency Analyzer"
description: "Analyzes CircleCI orb dependencies using the CircleCI v2 API and Orb Registry API. Maps orb version trees, detects breaking changes, and generates upgrade paths for pinned orb references."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-orb-dependency-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-dependency-analyzer/
