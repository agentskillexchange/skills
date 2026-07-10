---
title: "Run agentic anomaly investigations with PyOD"
description: "Use PyOD’s agent skill or MCP server to turn natural-language anomaly detection requests into repeatable detector selection, fitting, scoring, and investigation workflows."
verification: "security_reviewed"
source: "https://github.com/yzhao062/pyod"
author: "PyOD maintainers"
publisher_type: "individual"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "yzhao062/pyod"
  github_stars: 9854
---

# Run agentic anomaly investigations with PyOD

Use PyOD’s agent skill or MCP server to turn natural-language anomaly detection requests into repeatable detector selection, fitting, scoring, and investigation workflows.

## Prerequisites

Python, pip, PyOD, optional MCP-compatible client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install pyod`. For agent skill use, run `pyod install skill` or `pyod install skill --project`. For MCP clients, install `pip install pyod[mcp]` and start the server with `pyod mcp serve`.
```

## Documentation

- http://pyod.readthedocs.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agentic-anomaly-investigations-with-pyod/)
