---
title: "Benchmark deep research agents across factual, quality, and process dimensions with MiroEval"
slug: "benchmark-deep-research-agents-across-factual-quality-and-process-dimensions-with-miroeval"
description: "Score deep research agents on benchmark tasks using factual verification, report-quality scoring, and process evaluation before model or workflow changes ship."
github_stars: 34
verification: "security_reviewed"
source: "https://github.com/MiroMindAI/MiroEval"
author: "MiroMindAI"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "MiroMindAI/MiroEval"
  github_stars: 34
---

# Benchmark deep research agents across factual, quality, and process dimensions with MiroEval

Score deep research agents on benchmark tasks using factual verification, report-quality scoring, and process evaluation before model or workflow changes ship.

## Prerequisites

Python, uv, model result JSON, required API keys for judge and retrieval services

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run `uv sync`, copy `.env.template` to `.env` and add the required API keys, prepare a model-results JSON file, then execute `bash run_eval.sh --input data/method_results/my_model.json --model_name my_model`.
```

## Documentation

- https://github.com/MiroMindAI/MiroEval

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/benchmark-deep-research-agents-across-factual-quality-and-process-dimensions-with-miroeval/)
