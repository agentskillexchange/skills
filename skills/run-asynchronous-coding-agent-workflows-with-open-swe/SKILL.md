---
title: "Run asynchronous coding-agent workflows with Open SWE"
description: "Deploy an internal coding agent that accepts tasks from GitHub, Slack, or Linear, runs them in isolated sandboxes, and opens pull requests automatically."
verification: "security_reviewed"
source: "https://github.com/langchain-ai/open-swe"
author: "LangChain"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "langchain-ai/open-swe"
  github_stars: 9823
---

# Run asynchronous coding-agent workflows with Open SWE

Deploy an internal coding agent that accepts tasks from GitHub, Slack, or Linear, runs them in isolated sandboxes, and opens pull requests automatically.

## Prerequisites

Python, uv, GitHub App, LangSmith, sandbox provider, GitHub/Slack/Linear trigger

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone `https://github.com/langchain-ai/open-swe`, run `uv venv`, `source .venv/bin/activate`, and `uv sync --all-extras`, then follow the installation guide to configure the GitHub App, LangSmith OAuth, sandbox snapshot, and webhook triggers.
```

## Documentation

- https://openswe.vercel.app

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-asynchronous-coding-agent-workflows-with-open-swe/)
