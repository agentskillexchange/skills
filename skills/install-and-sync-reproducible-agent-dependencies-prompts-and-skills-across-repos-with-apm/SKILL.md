---
title: "Install and sync reproducible agent dependencies, prompts, and skills across repos with APM"
description: "Use one manifest to reproduce agent setup across repositories so skills, prompts, plugins, and config stop drifting from machine to machine."
verification: "listed"
source: "https://github.com/microsoft/apm"
author: "Microsoft"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "microsoft/apm"
  github_stars: 1934
  npm_package: "apm-cli"
  npm_weekly_downloads: 5075
---

# Install and sync reproducible agent dependencies, prompts, and skills across repos with APM

Use one manifest to reproduce agent setup across repositories so skills, prompts, plugins, and config stop drifting from machine to machine.

## Prerequisites

Git access to the target repo, APM CLI, an apm.yml manifest, and whichever agent runtimes or plugin targets the manifest installs into

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install APM from the upstream binary, Homebrew, or pip path, create or adopt an apm.yml manifest, then run the documented install or sync commands inside the target repository to reproduce the agent setup.
```

## Documentation

- https://microsoft.github.io/apm/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-and-sync-reproducible-agent-dependencies-prompts-and-skills-across-repos-with-apm/)
