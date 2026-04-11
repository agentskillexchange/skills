---
title: "Diagnose WordPress repo structure and route follow-up work safely"
description: "This skill inspects a WordPress codebase, identifies what kind of project it is, and returns the signals an agent needs before touching files or running tools. Use it when you need a deterministic first pass instead of guessing whether a repo is a plugin, block theme, site, core checkout, or mixed workspace."
verification: "security_reviewed"
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-project-triage"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
---

# Diagnose WordPress repo structure and route follow-up work safely

This skill inspects a WordPress codebase, identifies what kind of project it is, and returns the signals an agent needs before touching files or running tools. Use it when you need a deterministic first pass instead of guessing whether a repo is a plugin, block theme, site, core checkout, or mixed workspace.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-wordpress-repo-structure-and-route-follow-up-work-safely/)
