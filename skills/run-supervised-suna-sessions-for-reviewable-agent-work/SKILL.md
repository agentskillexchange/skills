---
title: "Run supervised Suna sessions for reviewable agent work"
description: "Start a bounded Suna or Kortix agent session, let it use browser, files, tools, and connectors, then review the session output before delivery."
verification: "security_reviewed"
source: "https://github.com/kortix-ai/suna"
author: "Kortix AI"
publisher_type: "organization"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "kortix-ai/suna"
  github_stars: 19814
---

# Run supervised Suna sessions for reviewable agent work

Start a bounded Suna or Kortix agent session, let it use browser, files, tools, and connectors, then review the session output before delivery.

## Prerequisites

Suna or Kortix runtime, Kortix CLI or hosted Kortix project, browser/files workspace, configured connectors or MCP tools as needed.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Use the upstream Kortix installer from https://kortix.com/install after reviewing it, then run kortix init to scaffold a project and kortix ship to bring it live. For a bounded run, start a session with kortix sessions new --prompt "<task>", inspect change requests with kortix cr ls, and use kortix chat for session interaction.
```

## Documentation

- https://kortix.com/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-supervised-suna-sessions-for-reviewable-agent-work/)
