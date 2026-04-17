---
title: "CircleCI Orb Dependency Analyzer"
description: "The CircleCI Orb Dependency Analyzer skill leverages the CircleCI v2 API and Orb Registry API to map and manage orb dependency trees across projects. It queries the GET /orb/{namespace}/{orb} endpoint to retrieve orb source and version metadata. The skill builds a dependency graph by parsing orb source YAML for nested orb imports and command references. Version constraint resolution follows semantic versioning rules to identify compatible upgrade paths when breaking changes are detected. It uses the CircleCI Pipeline API (GET /project/{project-slug}/pipeline) to find which pipelines reference specific orb versions. The skill generates migration diffs showing exact YAML changes needed for orb upgrades. It cross-references the CircleCI Insights API for build success rates across orb versions to recommend the most stable upgrade targets. Automated PR generation includes updated config.yml with upgraded orb references and changelog summaries pulled from the Orb Registry."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Dependency Analyzer

The CircleCI Orb Dependency Analyzer skill leverages the CircleCI v2 API and Orb Registry API to map and manage orb dependency trees across projects. It queries the GET /orb/{namespace}/{orb} endpoint to retrieve orb source and version metadata. The skill builds a dependency graph by parsing orb source YAML for nested orb imports and command references. Version constraint resolution follows semantic versioning rules to identify compatible upgrade paths when breaking changes are detected. It uses the CircleCI Pipeline API (GET /project/{project-slug}/pipeline) to find which pipelines reference specific orb versions. The skill generates migration diffs showing exact YAML changes needed for orb upgrades. It cross-references the CircleCI Insights API for build success rates across orb versions to recommend the most stable upgrade targets. Automated PR generation includes updated config.yml with upgraded orb references and changelog summaries pulled from the Orb Registry.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-orb-dependency-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/circleci-orb-dependency-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-analyzer/)
