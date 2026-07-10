---
title: "Evaluate agent and model workflows with EvalScope"
description: "Run repeatable EvalScope benchmark suites for LLM, VLM, RAG, and agent workflows, then inspect traces and reports before changing models or prompts."
verification: "security_reviewed"
source: "https://github.com/modelscope/evalscope"
author: "ModelScope Community"
publisher_type: "organization"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "modelscope/evalscope"
  github_stars: 2953
---

# Evaluate agent and model workflows with EvalScope

Run repeatable EvalScope benchmark suites for LLM, VLM, RAG, and agent workflows, then inspect traces and reports before changing models or prompts.

## Prerequisites

Python 3.10+, pip, evalscope package, model endpoint or local model backend, API credentials when evaluating hosted models, selected benchmark datasets

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip install evalscope, configure the target model or OpenAI-compatible API endpoint, choose a benchmark dataset or agent evaluation mode, run evalscope eval or the relevant benchmark command, and inspect the generated score files, traces, and dashboard reports.
```

## Documentation

- https://evalscope.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/evaluate-agent-and-model-workflows-with-evalscope/)
