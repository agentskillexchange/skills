---
title: "CircleCI Orb Dependency Analyzer"
description: "Analyzes CircleCI orb dependencies using the CircleCI v2 API and Orb Registry API. Maps orb version trees, detects breaking changes, and generates upgrade paths for pinned orb references."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Dependency Analyzer

The CircleCI Orb Dependency Analyzer skill leverages the CircleCI v2 API and Orb Registry API to map and manage orb dependency trees across projects. It queries the GET /orb/{namespace}/{orb} endpoint to retrieve orb source and version metadata. The skill builds a dependency graph by parsing orb source YAML for nested orb imports and command references. Version constraint resolution follows semantic versioning rules to identify compatible upgrade paths when breaking changes are detected. It uses the CircleCI Pipeline API (GET /project/{project-slug}/pipeline) to find which pipelines reference specific orb versions. The skill generates migration diffs showing exact YAML changes needed for orb upgrades. It cross-references the CircleCI Insights API for build success rates across orb versions to recommend the most stable upgrade targets. Automated PR generation includes updated config.yml with upgraded orb references and changelog summaries pulled from the Orb Registry.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-analyzer/)
