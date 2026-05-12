---
title: "Turn GitHub issues into reviewed code changes with SWE-agent"
slug: "turn-github-issues-into-reviewed-code-changes-with-swe-agent"
description: "Run SWE-agent against a repository issue so a language model can inspect files, execute commands and tests, and produce a patch for human review."
verification: "security_reviewed"
source: "https://github.com/SWE-agent/SWE-agent"
author: "SWE-agent"
publisher_type: "academic_open_source"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "SWE-agent/SWE-agent"
  github_stars: 19162
---

# Turn GitHub issues into reviewed code changes with SWE-agent

Run SWE-agent against a repository issue so a language model can inspect files, execute commands and tests, and produce a patch for human review.

## Prerequisites

SWE-agent; Python environment; Git repository or GitHub issue; model API credentials; test/runtime dependencies for the target project

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the SWE-agent documentation to install the CLI, configure a model, point it at a repository issue or task, run the agent, then review and test the generated patch before merging.
```

## Documentation

- https://swe-agent.com/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-github-issues-into-reviewed-code-changes-with-swe-agent/)
