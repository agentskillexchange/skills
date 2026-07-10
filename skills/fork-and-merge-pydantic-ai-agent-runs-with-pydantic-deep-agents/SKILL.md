---
title: "Fork and merge Pydantic AI agent runs with Pydantic Deep Agents"
description: "Run a self-hosted terminal agent or custom Pydantic AI harness that can branch a coding or research run, test isolated alternatives, and merge the winning branch."
verification: "security_reviewed"
source: "https://github.com/vstorm-co/pydantic-deepagents"
author: "vstorm-co"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "vstorm-co/pydantic-deepagents"
  github_stars: 912
---

# Fork and merge Pydantic AI agent runs with Pydantic Deep Agents

Run a self-hosted terminal agent or custom Pydantic AI harness that can branch a coding or research run, test isolated alternatives, and merge the winning branch.

## Prerequisites

Python 3.10+, pydantic-deep CLI or Python package, approved model provider key, optional sandbox support for isolated execution

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install from PyPI with `pip install pydantic-deep`, then run the terminal assistant or create a custom harness with `create_deep_agent(...)`. Configure an approved model provider key, enable live run forking for branch-and-merge workflows, and compare branch results with a project check command such as `pytest -q` before merging.
```

## Documentation

- https://vstorm-co.github.io/pydantic-deepagents/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fork-and-merge-pydantic-ai-agent-runs-with-pydantic-deep-agents/)
