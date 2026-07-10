---
title: "Run production multi-agent workflows with Hive"
description: "Use Hive as a model-agnostic harness for long-running multi-agent workflows that need state, recovery, observability, human oversight, and business-system tools."
verification: "security_reviewed"
source: "https://github.com/aden-hive/hive"
author: "Aden Hive"
publisher_type: "organization"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "aden-hive/hive"
  github_stars: 10461
---

# Run production multi-agent workflows with Hive

Use Hive as a model-agnostic harness for long-running multi-agent workflows that need state, recovery, observability, human oversight, and business-system tools.

## Prerequisites

Hive/OpenHive, Python 3.11+, uv workspace setup, LLM provider credentials, optional MCP business-system tools, optional ripgrep

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone `https://github.com/aden-hive/hive.git`, enter the repository, then run `./quickstart.sh` on macOS/Linux or `./quickstart.ps1` on Windows. Do not use `pip install -e .` from the repository root; the upstream README states that Hive uses a uv workspace layout.
```

## Documentation

- https://docs.adenhq.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-production-multi-agent-workflows-with-hive/)
