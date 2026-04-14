---
title: "Enforce JavaScript and TypeScript dependency rules before architectural drift spreads with dependency-cruiser"
description: "Scan a JS or TS codebase for forbidden imports, circular dependencies, orphaned modules, and other dependency-rule violations before they turn into structural drift."
verification: listed
source: "https://github.com/sverweij/dependency-cruiser"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sverweij/dependency-cruiser"
  github_stars: 6557
  npm_package: "dependency-cruiser"
  npm_weekly_downloads: 5181412
---

# Enforce JavaScript and TypeScript dependency rules before architectural drift spreads with dependency-cruiser

Use dependency-cruiser when an agent needs to check whether a JavaScript or TypeScript codebase still respects architecture boundaries, import rules, and package dependency expectations. It is the right invocation when you want a dependency-policy gate, violation report, or dependency graph for CI and review, rather than using a generic package tool normally. The scope boundary is narrow and skill-shaped: it validates and reports dependency structure against explicit rules, not general linting, package management, or broad code analysis.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-javascript-and-typescript-dependency-rules-before-architectural-drift-spreads-with-dependency-cruiser/)
