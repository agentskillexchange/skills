---
name: "Review and validate project assumptions with Common Ground"
slug: "review-and-validate-project-assumptions-with-common-ground"
description: "Run Common Ground in Claude Code to surface project assumptions, confirm their evidence and confidence with the operator, and save a reviewable Markdown and JSON record before implementation."
verification: "security_reviewed"
source: "https://github.com/Jeffallan/claude-skills/blob/plugin/commands/common-ground/COMMAND.md"
author: "jeffallan"
publisher_type: "community"
category: "Developer Tools"
framework: "Claude Code"
---

# Review and validate project assumptions with Common Ground

Run Common Ground in Claude Code to surface project assumptions, confirm their evidence and confidence with the operator, and save a reviewable Markdown and JSON record before implementation.

## Prerequisites

Claude Code with the fullstack-dev-skills plugin; project files and conversation context; Git when a remote is available; operator input for assumption selection and confidence-tier changes; local access to ~/.claude/common-ground/.

## Installation

Install or set up from the source-backed instructions:

In Claude Code run /plugin marketplace add jeffallan/claude-skills, then /plugin install fullstack-dev-skills@fullstack-dev-skills. Restart when prompted. In the intended project invoke /common-ground. Use /common-ground --list to inspect stored assumptions and /common-ground --check to revalidate. Upstream skills-only installation methods do not include these slash commands.

- Source: https://github.com/Jeffallan/claude-skills/blob/plugin/commands/common-ground/COMMAND.md

## Documentation

- https://github.com/Jeffallan/claude-skills/blob/main/docs/COMMON_GROUND.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-and-validate-project-assumptions-with-common-ground/)
