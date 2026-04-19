---
title: "Iteratively optimize prompts and text-based agent configs against scored eval sets with GEPA"
description: "Use GEPA when an agent builder needs to iteratively improve a prompt or other text-configured component against a scored eval set, not when they are just chatting with a model or browsing prompt tips. The workflow is bounded: provide a seed candidate, run reflective optimization against train and validation examples, review the improved candidate, and keep or reject it based on measured lift. That scope boundary, reflective text optimization against explicit evaluation data, makes this a skill rather than a generic model or framework listing."
source: "https://github.com/gepa-ai/gepa"
verification: "listed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gepa-ai/gepa"
  github_stars: 3550
  npm_package: "gepa"
  npm_weekly_downloads: 4095897
---

# Iteratively optimize prompts and text-based agent configs against scored eval sets with GEPA

Use GEPA when an agent builder needs to iteratively improve a prompt or other text-configured component against a scored eval set, not when they are just chatting with a model or browsing prompt tips. The workflow is bounded: provide a seed candidate, run reflective optimization against train and validation examples, review the improved candidate, and keep or reject it based on measured lift. That scope boundary, reflective text optimization against explicit evaluation data, makes this a skill rather than a generic model or framework listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa/)
