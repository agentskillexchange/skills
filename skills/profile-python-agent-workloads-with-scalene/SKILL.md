---
title: "Profile Python agent workloads with Scalene"
description: "Use Scalene when a Python agent, tool server, or retrieval pipeline needs line-level CPU, GPU, and memory profiling before targeted optimization."
verification: "security_reviewed"
source: "https://github.com/plasma-umass/scalene"
author: "plasma-umass"
publisher_type: "open_source"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "plasma-umass/scalene"
  github_stars: 13455
---

# Profile Python agent workloads with Scalene

Use Scalene when a Python agent, tool server, or retrieval pipeline needs line-level CPU, GPU, and memory profiling before targeted optimization.

## Prerequisites

Python project or script that reproduces the workload; Scalene CLI; local or staging permission to run profiling

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with python3 -m pip install -U scalene or conda install -c conda-forge scalene. Run scalene run your_prog.py, or python3 -m scalene run your_prog.py, then inspect with scalene view, scalene view --cli, or exported output such as scalene run -o results.json your_prog.py.
```

## Documentation

- https://github.com/plasma-umass/scalene

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/profile-python-agent-workloads-with-scalene/)
