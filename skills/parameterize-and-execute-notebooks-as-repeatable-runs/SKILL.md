---
title: "Parameterize and execute notebooks as repeatable runs"
description: "Use Papermill when an agent needs to treat a Jupyter notebook like a reusable job instead of a one-off interactive document. The skill injects parameters, runs the notebook end to end, and preserves the executed output as an artifact for review or handoff."
verification: "security_reviewed"
source: "https://github.com/nteract/papermill"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "nteract/papermill"
  github_stars: 6429
---

# Parameterize and execute notebooks as repeatable runs

This skill uses Papermill, the notebook execution tool from the nteract ecosystem, to turn a parameterized Jupyter notebook into a repeatable workflow step. An agent invokes it when a notebook already contains the right logic, but the work now needs to run with different inputs, on a schedule, or inside a larger automation chain without manual editing. The scope boundary keeps this from collapsing into a generic notebook or Python product listing. The agent is not selecting Papermill merely because it is a package. It is using a specific workflow pattern: inject runtime parameters into a tagged notebook, execute the notebook in order, capture outputs and errors, and return the finished notebook or derived artifacts to the next system. If a user just wants to author notebooks interactively, browse data, or manage kernels, this skill does not apply. Use it for recurring analyses, templated reports, batch data checks, experiment reruns, and handoff-friendly research workflows where notebook output needs to be reproducible. Integration points include the Papermill CLI, Python API, schedulers, pipeline runners, and storage for produced notebooks or exports. Agents can pair it with cron, CI, or data extraction steps, then summarize the results, flag failed cells, or archive execution artifacts with the exact parameters used for that run.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/parameterize-and-execute-notebooks-as-repeatable-runs/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/parameterize-and-execute-notebooks-as-repeatable-runs
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/parameterize-and-execute-notebooks-as-repeatable-runs`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parameterize-and-execute-notebooks-as-repeatable-runs/)
