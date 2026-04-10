---
name: CircleCI Orb Dependency Analyzer
description: Analyzes CircleCI orb dependencies using the CircleCI v2 API and Orb
  Registry API. Maps orb version trees, detects breaking changes, and generates upgrade
  paths for pinned orb references.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-dependency-analyzer/
category:
- CI/CD Integrations
framework:
- Gemini
---
# CircleCI Orb Dependency Analyzer

The CircleCI Orb Dependency Analyzer skill leverages the CircleCI v2 API and Orb Registry API to map and manage orb dependency trees across projects. It queries the GET /orb/{namespace}/{orb} endpoint to retrieve orb source and version metadata. The skill builds a dependency graph by parsing orb source YAML for nested orb imports and command references. Version constraint resolution follows semantic versioning rules to identify compatible upgrade paths when breaking changes are detected. It uses the CircleCI Pipeline API (GET /project/{project-slug}/pipeline) to find which pipelines reference specific orb versions. The skill generates migration diffs showing exact YAML changes needed for orb upgrades. It cross-references the CircleCI Insights API for build success rates across orb versions to recommend the most stable upgrade targets. Automated PR generation includes updated config.yml with upgraded orb references and changelog summaries pulled from the Orb Registry.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-analyzer/)
