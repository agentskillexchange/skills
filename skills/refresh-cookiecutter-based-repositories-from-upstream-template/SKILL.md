---
title: "Refresh Cookiecutter-based repositories from their upstream template without losing local answers"
description: "Use Cruft when an agent needs to pull new changes from a Cookiecutter template into an existing generated repository without redoing the project from scratch. The agent tracks the template origin, previews the diff, applies the update, and preserves the repository&#8217;s saved answers and local customizations as carefully as possible."
verification: security_reviewed
source: "https://github.com/cruft/cruft"
category:
  - "Templates &amp; Workflows"
---

# Refresh Cookiecutter-based repositories from their upstream template without losing local answers

Use Cruft when an agent needs to pull new changes from a Cookiecutter template into an existing generated repository without redoing the project from scratch. The agent tracks the template origin, previews the diff, applies the update, and preserves the repository&#8217;s saved answers and local customizations as carefully as possible.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/refresh-cookiecutter-based-repositories-from-upstream-template/)
