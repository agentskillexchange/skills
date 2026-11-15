---
name: "Link agent skills, commands, and roles across coding assistants with Open Agent Hub"
slug: "link-agent-skills-commands-and-roles-across-coding-assistants-with-open-agent-hub"
description: "Use Open Agent Hub to install, link, and enable reusable skills, agent roles, and slash commands across Claude Code, Codex, Cursor, Gemini, Trae, and related assistants."
github_stars: 934
verification: "security_reviewed"
source: "https://github.com/guanyang/open-agent-hub"
author: "guanyang"
publisher_type: "community"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "guanyang/open-agent-hub"
  github_stars: 934
---

# Link agent skills, commands, and roles across coding assistants with Open Agent Hub

Use Open Agent Hub to install, link, and enable reusable skills, agent roles, and slash commands across Claude Code, Codex, Cursor, Gemini, Trae, and related assistants.

## Prerequisites

Node.js/npm for npm link, Open Agent Hub repository, target coding assistant configuration directories such as .claude, .codex, .cursor, .gemini, or .agents

## Installation

For skills-only installation, use the upstream skills CLI:

- npx skills@latest add guanyang/open-agent-hub

To add one skill from the hub, pass its skill name:

- npx skills@latest add guanyang/open-agent-hub --skill remotion

For the full hub manager, clone the repository, then follow the upstream README to link the open-agent CLI from the repository root:

- git clone https://github.com/guanyang/open-agent-hub.git ~/open-agent-hub

- Source: https://github.com/guanyang/open-agent-hub
- Extracted from upstream docs: https://raw.githubusercontent.com/guanyang/open-agent-hub/HEAD/README.md

## Documentation

- https://github.com/guanyang/open-agent-hub

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/link-agent-skills-commands-and-roles-across-coding-assistants-with-open-agent-hub/)
