---
title: "Add managed long-term memory to LangGraph agents with LangMem"
description: "Give LangGraph agents memory management and search tools so they can store, retrieve, and update durable facts across sessions."
verification: "security_reviewed"
source: "https://github.com/langchain-ai/langmem"
author: "LangChain"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "langchain-ai/langmem"
  github_stars: 1502
---

# Add managed long-term memory to LangGraph agents with LangMem

Give LangGraph agents memory management and search tools so they can store, retrieve, and update durable facts across sessions.

## Prerequisites

Python, langmem, LangGraph or LangChain agent runtime, persistent store such as Postgres for production, LLM provider API key

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install -U langmem`, configure the target LLM provider key, create or connect a LangGraph store, then add `create_manage_memory_tool` and `create_search_memory_tool` to the agent.
```

## Documentation

- https://langchain-ai.github.io/langmem/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-managed-long-term-memory-to-langgraph-agents-with-langmem/)
