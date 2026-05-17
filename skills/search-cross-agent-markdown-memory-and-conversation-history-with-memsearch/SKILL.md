---
name: "Search cross-agent Markdown memory and conversation history with memsearch"
slug: "search-cross-agent-markdown-memory-and-conversation-history-with-memsearch"
description: "Give supported coding agents a shared Markdown-first memory layer so they can recall prior decisions, transcripts, and notes across sessions instead of re-deriving context from scratch."
github_stars: 1324
verification: "security_reviewed"
source: "https://github.com/zilliztech/memsearch"
author: "Zilliz"
publisher_type: "organization"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "zilliztech/memsearch"
  github_stars: 1324
---

# Search cross-agent Markdown memory and conversation history with memsearch

Give supported coding agents a shared Markdown-first memory layer so they can recall prior decisions, transcripts, and notes across sessions instead of re-deriving context from scratch.

## Prerequisites

Supported coding-agent client, local filesystem access, default local Milvus/ONNX setup or another configured embedding provider

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Use the platform-specific plugin flow from the repo. For Claude Code, add the marketplace source and install `memsearch`. For OpenClaw, run `openclaw plugins install clawhub:memsearch` and restart the gateway. Other supported agent clients have separate install instructions in the upstream docs.
```

## Documentation

- https://github.com/zilliztech/memsearch#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-cross-agent-markdown-memory-and-conversation-history-with-memsearch/)
