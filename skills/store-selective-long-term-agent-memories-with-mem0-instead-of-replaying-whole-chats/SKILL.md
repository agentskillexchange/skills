---
title: "Store selective long-term agent memories with Mem0 instead of replaying whole chats"
description: "Use Mem0 when an agent should retain durable preferences, facts, and prior decisions as selective memory records instead of stuffing more transcript history back into every prompt."
verification: "security_reviewed"
source: "https://github.com/mem0ai/mem0"
author: "Mem0"
publisher_type: "company"
category:
  - "Library & API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mem0ai/mem0"
  github_stars: 53457
  npm_package: "mem0ai"
  npm_weekly_downloads: 2535676
---

# Store selective long-term agent memories with Mem0 instead of replaying whole chats

Use Mem0 when an agent should retain durable preferences, facts, and prior decisions as selective memory records instead of stuffing more transcript history back into every prompt.

## Prerequisites

A Python or Node agent stack, the Mem0 package or API, and a workflow that can decide which facts should be stored and later retrieved as durable memory.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Mem0 through the supported Python or npm package, configure the LLM and storage components described in the docs, wire the add and search calls into your agent workflow, and store only stable facts or preferences so later runs can retrieve selective memory instead of replaying full chats.
```

## Documentation

- https://docs.mem0.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/store-selective-long-term-agent-memories-with-mem0-instead-of-replaying-whole-chats/)
