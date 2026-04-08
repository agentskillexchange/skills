---
title: CircleCI Orb Dependency Analyzer
description: The CircleCI Orb Dependency Analyzer skill leverages the CircleCI v2
  API and Orb Registry API to map and manage orb dependency trees across projects.
  It queries the GET /orb/{namespace}/{orb} endpoint to retrieve orb source and version
  metadata. The skill builds a dependency graph by parsing orb source YAML for nested
  orb imports and command references. Version constraint resolution follows semantic
  versioning rules to identify compatible upgrade paths when breaking changes are
  detected. It uses the CircleCI Pipeline API (GET /project/{project-slug}/pipeline)
  to find which pipelines reference specific orb versions. The skill generates migration
  diffs showing exact YAML changes needed for orb upgrades. It cross-references the
  CircleCI Insights API for build success rates across orb versions to recommend the
  most stable upgrade targets. Automated PR generation includes updated config.yml
  with upgraded orb references and changelog summaries pulled from the Orb Registry.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-analyzer/)
