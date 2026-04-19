---
title: "Parameterize and execute notebooks as repeatable runs"
description: "This skill uses Papermill , the notebook execution tool from the nteract ecosystem, to turn a parameterized Jupyter notebook into a repeatable workflow step. An agent invokes it when a notebook already contains the right logic, but the work now needs to run with different inputs, on a schedule, or inside a larger automation chain without manual editing. The scope boundary keeps this from collapsing into a generic notebook or Python product listing. The agent is not selecting Papermill merely because it is a package. It is using a specific workflow pattern: inject runtime parameters into a tagged notebook, execute the notebook in order, capture outputs and errors, and return the finished notebook or derived artifacts to the next system. If a user just wants to author notebooks interactively, browse data, or manage kernels, this skill does not apply. Use it for recurring analyses, templated reports, batch data checks, experiment reruns, and handoff-friendly research workflows where notebook output needs to be reproducible. Integration points include the Papermill CLI, Python API, schedulers, pipeline runners, and storage for produced notebooks or exports. Agents can pair it with cron, CI, or data extraction steps, then summarize the results, flag failed cells, or archive execution artifacts with the exact parameters used for that run."
source: "https://github.com/nteract/papermill"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "nteract/papermill"
  github_stars: 6429
---

# Parameterize and execute notebooks as repeatable runs

This skill uses Papermill , the notebook execution tool from the nteract ecosystem, to turn a parameterized Jupyter notebook into a repeatable workflow step. An agent invokes it when a notebook already contains the right logic, but the work now needs to run with different inputs, on a schedule, or inside a larger automation chain without manual editing. The scope boundary keeps this from collapsing into a generic notebook or Python product listing. The agent is not selecting Papermill merely because it is a package. It is using a specific workflow pattern: inject runtime parameters into a tagged notebook, execute the notebook in order, capture outputs and errors, and return the finished notebook or derived artifacts to the next system. If a user just wants to author notebooks interactively, browse data, or manage kernels, this skill does not apply. Use it for recurring analyses, templated reports, batch data checks, experiment reruns, and handoff-friendly research workflows where notebook output needs to be reproducible. Integration points include the Papermill CLI, Python API, schedulers, pipeline runners, and storage for produced notebooks or exports. Agents can pair it with cron, CI, or data extraction steps, then summarize the results, flag failed cells, or archive execution artifacts with the exact parameters used for that run.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parameterize-and-execute-notebooks-as-repeatable-runs/)
