---
title: "Statically scan agent repos for prompt injection and unsafe MCP configs with Agent Audit"
description: "Audit agent code, prompts, and MCP configuration for prompt-injection surfaces, taint issues, and unsafe tool exposure before shipping."
verification: "listed"
source: "https://github.com/HeadyZhang/agent-audit"
author: "Agent Security Team"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "HeadyZhang/agent-audit"
  github_stars: 149
---

# Statically scan agent repos for prompt injection and unsafe MCP configs with Agent Audit

Audit agent code, prompts, and MCP configuration for prompt-injection surfaces, taint issues, and unsafe tool exposure before shipping.

## Prerequisites

agent-audit, local agent repository or config tree

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the agent-audit package from the upstream project, point it at an agent repository or config tree, and run the static scan before CI approval or release.
```

## Documentation

- https://headyzhang.github.io/agent-audit/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/statically-scan-agent-repos-for-prompt-injection-and-unsafe-mcp-configs-with-agent-audit/)
