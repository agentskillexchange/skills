---
name: "Model and verify bounded LP and MILP problems with NVIDIA cuOpt"
slug: "model-and-verify-bounded-lp-and-milp-problems-with-nvidia-cuopt"
description: "Use NVIDIA’s portable optimization skill to formulate a bounded LP or MILP, run cuOpt, and check solver status and assignments against the intended constraints."
verification: "security_reviewed"
source: "https://github.com/NVIDIA/skills/tree/main/skills/cuopt-numerical-optimization-api"
author: "NVIDIA cuOpt Team"
publisher_type: "organization"
category: "Developer Tools"
framework: "Multi-Framework"
---

# Model and verify bounded LP and MILP problems with NVIDIA cuOpt

Use NVIDIA’s portable optimization skill to formulate a bounded LP or MILP, run cuOpt, and check solver status and assignments against the intended constraints.

## Prerequisites

Agent Skills-compatible coding agent; Node.js/npm skills CLI; NVIDIA GPU with supported driver and CUDA; matching cuOpt Python package or CLI

## Installation

Install or set up from the source-backed instructions:

Install the Agent Skills package with npx skills@latest add nvidia/skills --skill cuopt-numerical-optimization-api --agent claude-code --yes; use --agent codex or another supported target when appropriate. Confirm the installed skill and load it in the target agent. Provision cuOpt separately using the upstream cuopt-install instructions for the actual GPU, driver and CUDA version; do not mix CUDA package variants. Verify the Python import or cuopt_cli --help before solving.

- Source: https://github.com/NVIDIA/skills/tree/main/skills/cuopt-numerical-optimization-api

## Documentation

- https://github.com/NVIDIA/skills/blob/main/skills/cuopt-numerical-optimization-api/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/model-and-verify-bounded-lp-and-milp-problems-with-nvidia-cuopt/)
