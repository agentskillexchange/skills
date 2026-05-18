---
name: "Diagnose WordPress repo structure and route follow-up work safely"
slug: "diagnose-wordpress-repo-structure-and-route-follow-up-work-safely"
description: "This skill inspects a WordPress codebase, identifies what kind of project it is, and returns the signals an agent needs before touching files or running tools. Use it when you need a deterministic first pass instead of guessing whether a repo is a plugin, block theme, site, core checkout, or mixed workspace."
verification: "listed"
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-project-triage"
author: "WordPress Contributors"
publisher_type: "Open Source Project"
category: "WordPress & CMS"
framework: "Multi-Framework"
---

# Diagnose WordPress repo structure and route follow-up work safely

This skill inspects a WordPress codebase, identifies what kind of project it is, and returns the signals an agent needs before touching files or running tools. Use it when you need a deterministic first pass instead of guessing whether a repo is a plugin, block theme, site, core checkout, or mixed workspace.

## Prerequisites

Node.js; filesystem access; optional WP-CLI for downstream workflows

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/WordPress/agent-skills.git

Requirements and caveats from upstream:
- node shared/scripts/skillpack-build.mjs --clean
- node shared/scripts/skillpack-install.mjs --global
- node shared/scripts/skillpack-install.mjs --global --skills=wp-playground,wp-block-development

Basic usage or getting-started notes:
- bash
- # Clone agent-skills
- cd agent-skills

- Source: https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-project-triage
- Extracted from upstream docs: https://raw.githubusercontent.com/WordPress/agent-skills/HEAD/README.md

## Documentation

- https://github.com/WordPress/agent-skills

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-wordpress-repo-structure-and-route-follow-up-work-safely/)
