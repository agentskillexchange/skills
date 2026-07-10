---
title: "Use Prompt Flow for LLM workflow testing and evaluation"
description: "Build a Prompt Flow graph, run interactive and batch tests, inspect traces and evaluation metrics, and promote only reviewed LLM workflow versions."
verification: "security_reviewed"
source: "https://github.com/microsoft/promptflow"
author: "Microsoft"
publisher_type: "organization"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "microsoft/promptflow"
  github_stars: 11142
---

# Use Prompt Flow for LLM workflow testing and evaluation

Build a Prompt Flow graph, run interactive and batch tests, inspect traces and evaluation metrics, and promote only reviewed LLM workflow versions.

## Prerequisites

Prompt Flow CLI, Python 3.9 through 3.11, promptflow and promptflow-tools packages, configured OpenAI or Azure OpenAI connection, optional VS Code extension.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install promptflow promptflow-tools`, initialize a flow with `pf flow init --flow ./my_chatbot --type chat`, create the provider connection with `pf connection create`, then run `pf flow test --flow ./my_chatbot --interactive` before adding dataset evaluation.
```

## Documentation

- https://microsoft.github.io/promptflow/index.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/use-prompt-flow-for-llm-workflow-testing-and-evaluation/)
