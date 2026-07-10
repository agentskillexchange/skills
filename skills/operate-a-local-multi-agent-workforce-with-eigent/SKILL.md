---
title: "Operate a local multi-agent workforce with Eigent"
description: "Use Eigent when an operator needs a local desktop agent workforce that can coordinate developer, browser, document, multimodal, model-provider, and MCP-backed work in one controlled environment."
verification: "security_reviewed"
source: "https://github.com/eigent-ai/eigent"
author: "eigent-ai"
publisher_type: "open_source"
category:
  - "Templates & Workflows"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "eigent-ai/eigent"
  github_stars: 14273
---

# Operate a local multi-agent workforce with Eigent

Use Eigent when an operator needs a local desktop agent workforce that can coordinate developer, browser, document, multimodal, model-provider, and MCP-backed work in one controlled environment.

## Prerequisites

Eigent desktop/frontend, local backend, Docker/PostgreSQL for local mode, model provider credentials or local models, optional MCP servers

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
For local mode, clone the repository, start `server/` with Docker Compose after copying `.env.example` to `.env`, configure the frontend `.env.development` for the local proxy, run `npm install`, and start the desktop/frontend with `npm run dev`.
```

## Documentation

- https://github.com/eigent-ai/eigent/blob/main/server/README_EN.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-a-local-multi-agent-workforce-with-eigent/)
