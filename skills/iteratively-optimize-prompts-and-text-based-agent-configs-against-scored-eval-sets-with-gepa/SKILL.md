---
title: "Iteratively optimize prompts and text-based agent configs against scored eval sets with GEPA"
description: "Use reflective search to improve prompts or text-configured agent components against a real eval set instead of manual prompt tweaking."
verification: "listed"
source: "https://github.com/gepa-ai/gepa"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gepa-ai/gepa"
  github_stars: 3550
  ase_npm_package: "gepa"
  npm_weekly_downloads: 4095897
---

# Iteratively optimize prompts and text-based agent configs against scored eval sets with GEPA

Use GEPA when an agent builder needs to iteratively improve a prompt or other text-configured component against a scored eval set, not when they are just chatting with a model or browsing prompt tips. The workflow is bounded: provide a seed candidate, run reflective optimization against train and validation examples, review the improved candidate, and keep or reject it based on measured lift. That scope boundary, reflective text optimization against explicit evaluation data, makes this a skill rather than a generic model or framework listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/iteratively-optimize-prompts-and-text-based-agent-configs-against-scored-eval-sets-with-gepa/)
