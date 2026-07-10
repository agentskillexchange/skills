---
title: "Gate agent inputs and outputs with Superagent safety checks"
description: "Use Superagent to add prompt-injection blocking, PII redaction, repository scanning, and compliance evidence around AI agent runs."
verification: "listed"
source: "https://github.com/superagent-ai/superagent"
author: "Superagent AI"
publisher_type: "open_source_project"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "superagent-ai/superagent"
  github_stars: 6615
  npm_package: "safety-agent"
  npm_weekly_downloads: 43707
---

# Gate agent inputs and outputs with Superagent safety checks

Use Superagent to add prompt-injection blocking, PII redaction, repository scanning, and compliance evidence around AI agent runs.

## Prerequisites

Superagent SDK, CLI, or MCP server; SUPERAGENT_API_KEY for hosted checks or supported local guard model

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the TypeScript package with npm install safety-agent or the Python package with uv add safety-agent, set SUPERAGENT_API_KEY when using hosted checks, then invoke guard, redact, scan, CLI, or MCP flows from the agent workflow.
```

## Documentation

- https://docs.superagent.sh

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-agent-inputs-and-outputs-with-superagent-safety-checks/)
