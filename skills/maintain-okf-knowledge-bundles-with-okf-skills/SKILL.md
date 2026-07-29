---
name: "Maintain OKF Knowledge Bundles with Okf Skills"
slug: "maintain-okf-knowledge-bundles-with-okf-skills"
description: "Use Okf Skills to have Claude Code produce, validate, migrate, and visualize Open Knowledge Format bundles with provenance, trust, staleness, and CI checks."
github_stars: 185
verification: "security_reviewed"
source: "https://github.com/scaccogatto/okf-skills"
author: "scaccogatto"
publisher_type: "open_source_project"
category: "Templates & Workflows"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "scaccogatto/okf-skills"
  github_stars: 185
---

# Maintain OKF Knowledge Bundles with Okf Skills

Use Okf Skills to have Claude Code produce, validate, migrate, and visualize Open Knowledge Format bundles with provenance, trust, staleness, and CI checks.

## Prerequisites

Claude Code plugin support or skills.sh-compatible agent skills, uv or python3 with pyyaml, repository-local OKF bundle, optional GitHub Actions

## Installation

Install or set up from the source-backed instructions:

Install as a Claude Code plugin with `/plugin marketplace add scaccogatto/okf-skills` and `/plugin install okf@scaccogatto`, or install the agent skills with `npx skills add scaccogatto/okf-skills`. Use `/okf:okf produce .okf`, `/okf:validate .okf --strict`, and `/okf:visualize .okf` for the core workflow.

- Source: https://github.com/scaccogatto/okf-skills

## Documentation

- https://scaccogatto.github.io/okf-skills/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/maintain-okf-knowledge-bundles-with-okf-skills/)
