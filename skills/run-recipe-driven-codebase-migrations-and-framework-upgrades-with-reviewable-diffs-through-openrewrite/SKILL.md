---
title: "Run recipe-driven codebase migrations and framework upgrades with reviewable diffs through OpenRewrite"
description: "Apply reusable refactoring recipes to large codebases so framework upgrades and codemods happen as auditable, reviewable changes."
verification: listed
source: "https://github.com/openrewrite/rewrite"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "openrewrite/rewrite"
  github_stars: 3395
---

# Run recipe-driven codebase migrations and framework upgrades with reviewable diffs through OpenRewrite

Use OpenRewrite when an agent needs to execute a known migration or refactoring recipe across a large codebase, such as framework upgrades, API replacements, or consistency fixes. Invoke this instead of using the underlying ecosystem normally when the task is bulk automated rewrites with reviewable diffs, not ordinary coding or library use. The scope boundary is clear: OpenRewrite is being used here as a recipe-driven migration workflow, not as a generic build plugin, SDK, or platform listing.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-recipe-driven-codebase-migrations-and-framework-upgrades-with-reviewable-diffs-through-openrewrite/)
