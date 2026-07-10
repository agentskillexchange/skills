---
title: "Ship AG2 multi-agent workflows behind APIs with FastAgency"
description: "Turn an AG2 multi-agent prototype into a reusable console, web, REST API, or broker-backed service with FastAgency."
verification: "security_reviewed"
source: "https://github.com/ag2ai/fastagency"
author: "AG2"
publisher_type: "Organization"
category:
  - "Templates & Workflows"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "ag2ai/fastagency"
  github_stars: 540
---

# Ship AG2 multi-agent workflows behind APIs with FastAgency

Turn an AG2 multi-agent prototype into a reusable console, web, REST API, or broker-backed service with FastAgency.

## Prerequisites

Python 3.10+; FastAgency; AG2/AutoGen workflow; optional Cookiecutter, FastAPI, Mesop, NATS/FastStream, and pytest depending on deployment target

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install FastAgency with `pip install fastagency` or scaffold a project with `pip install cookiecutter` and `cookiecutter https://github.com/ag2ai/cookiecutter-fastagency.git`; define the AG2 workflow, select the UI or adapter, set required LLM API keys, and run the generated tests before deployment.
```

## Documentation

- https://fastagency.ai/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ship-ag2-multi-agent-workflows-behind-apis-with-fastagency/)
