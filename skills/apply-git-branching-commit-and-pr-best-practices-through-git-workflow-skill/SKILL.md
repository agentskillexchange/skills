---
name: "Apply Git branching, commit, and pull request best practices through Git Workflow Skill"
slug: "apply-git-branching-commit-and-pr-best-practices-through-git-workflow-skill"
description: "Give an agent a portable Git workflow playbook for branch strategy, commit hygiene, pull requests, merge choices, and CI-aware collaboration."
github_stars: 13
verification: "security_reviewed"
source: "https://github.com/netresearch/git-workflow-skill"
author: "Netresearch DTT GmbH"
publisher_type: "open_source_project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "netresearch/git-workflow-skill"
  github_stars: 13
---

# Apply Git branching, commit, and pull request best practices through Git Workflow Skill

Give an agent a portable Git workflow playbook for branch strategy, commit hygiene, pull requests, merge choices, and CI-aware collaboration.

## Prerequisites

Git repository, agent that supports Agent Skills, optional GitHub or GitLab CI and pull-request workflow tooling

## Installation

Use the upstream install or setup path that matches your environment:
- npx skills add https://github.com/netresearch/git-workflow-skill --skill git-workflow
- git clone https://github.com/netresearch/git-workflow-skill.git
- composer require netresearch/git-workflow-skill
- npm install --save-dev \

Requirements and caveats from upstream:
- Requires [netresearch/composer-agent-skill-plugin](https://github.com/netresearch/composer-agent-skill-plugin).
- ### npm (Node Projects)
- Requires [@netresearch/agent-skill-coordinator](https://github.com/netresearch/node-agent-skill-coordinator), which discovers the skill in node_modules and registers it in AGENTS.md via a postinstall hook. For pnpm, a...

Basic usage or getting-started notes:
- ### Marketplace (Recommended)
- Add the [Netresearch marketplace](https://github.com/netresearch/claude-code-marketplace) once, then browse and install skills:
- bash

- Source: https://github.com/netresearch/git-workflow-skill
- Extracted from upstream docs: https://raw.githubusercontent.com/netresearch/git-workflow-skill/HEAD/README.md

## Documentation

- https://github.com/netresearch/git-workflow-skill

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apply-git-branching-commit-and-pr-best-practices-through-git-workflow-skill/)
