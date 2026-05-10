---
title: "Generate and safely patch AGENTS.md and RUNBOOK.md with AGENTS.md Generator"
slug: "generate-and-safely-patch-agents-md-and-runbook-md-with-agents-md-generator"
description: "Bootstrap and safely update AGENTS.md and RUNBOOK.md without clobbering hand-edited docs, so coding-agent repos keep a clean machine-readable contract."
github_stars: 2
verification: "security_reviewed"
source: "https://github.com/markoblogo/AGENTS.md_generator"
author: "markoblogo"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "markoblogo/AGENTS.md_generator"
  github_stars: 2
---

# Generate and safely patch AGENTS.md and RUNBOOK.md with AGENTS.md Generator

Bootstrap and safely update AGENTS.md and RUNBOOK.md without clobbering hand-edited docs, so coding-agent repos keep a clean machine-readable contract.

## Prerequisites

Python 3.11+, pipx or pip, Git repository

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pipx install git+https://github.com/markoblogo/AGENTS.md_generator.git`, then run `agentsgen init . --defaults --autodetect` in the target repository.
```

## Documentation

- https://github.com/markoblogo/AGENTS.md_generator

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-and-safely-patch-agents-md-and-runbook-md-with-agents-md-generator/)
