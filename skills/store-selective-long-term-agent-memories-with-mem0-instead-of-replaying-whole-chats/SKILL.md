---
name: "Store selective long-term agent memories with Mem0 instead of replaying whole chats"
slug: "store-selective-long-term-agent-memories-with-mem0-instead-of-replaying-whole-chats"
description: "Use Mem0 when an agent should retain durable preferences, facts, and prior decisions as selective memory records instead of stuffing more transcript history back into every prompt."
github_stars: 53457
verification: "listed"
source: "https://github.com/mem0ai/mem0"
author: "Mem0"
publisher_type: "company"
category: "Library & API Reference"
framework: "Multi-Framework"
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

Use the upstream install or setup path that matches your environment:
- npm install -g @mem0/cli # or: pip install mem0-cli
- pip install mem0ai
- pip install mem0ai[nlp]
- npm install mem0ai

Requirements and caveats from upstream:
- | **Setup** | pip install mem0ai | docker compose up | Sign up at [app.mem0.ai](https://app.mem0.ai?utm_source=oss&utm_medium=readme) |
- python -m spacy download en_core_web_sm
- cd server && docker compose up -d # http://localhost:3000

Basic usage or getting-started notes:
- All benchmarks run on the same production-representative model stack. Single-pass retrieval (one call, no agentic loops).
- bash
- ### Self-Hosted Server

- Source: https://github.com/mem0ai/mem0
- Extracted from upstream docs: https://raw.githubusercontent.com/mem0ai/mem0/HEAD/README.md

## Documentation

- https://docs.mem0.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/store-selective-long-term-agent-memories-with-mem0-instead-of-replaying-whole-chats/)
