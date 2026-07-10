---
title: "Study customer-service triage and handoff patterns with the OpenAI CS agents demo"
description: "Use OpenAI’s customer-service agents demo as a reference workflow for triage, specialist handoffs, guardrails, and support-case orchestration before building a production support agent."
verification: "security_reviewed"
source: "https://github.com/openai/openai-cs-agents-demo"
author: "OpenAI"
publisher_type: "official_project"
category:
  - "Templates & Workflows"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "openai/openai-cs-agents-demo"
  github_stars: 6314
---

# Study customer-service triage and handoff patterns with the OpenAI CS agents demo

Use OpenAI’s customer-service agents demo as a reference workflow for triage, specialist handoffs, guardrails, and support-case orchestration before building a production support agent.

## Prerequisites

OpenAI API key; Python backend; Node.js/Next.js UI; OpenAI Agents SDK; ChatKit

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Set OPENAI_API_KEY. Backend: cd python-backend; python -m venv .venv; source .venv/bin/activate; pip install -r requirements.txt; python -m uvicorn main:app --reload --port 8000. UI: cd ui; npm install; npm run dev.
```

## Documentation

- https://github.com/openai/openai-cs-agents-demo

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/study-customer-service-triage-and-handoff-patterns-with-the-openai-cs-agents-demo/)
