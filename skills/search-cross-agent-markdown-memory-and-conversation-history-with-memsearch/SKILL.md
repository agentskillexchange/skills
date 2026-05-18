---
name: "Search cross-agent Markdown memory and conversation history with memsearch"
slug: "search-cross-agent-markdown-memory-and-conversation-history-with-memsearch"
description: "Give supported coding agents a shared Markdown-first memory layer so they can recall prior decisions, transcripts, and notes across sessions instead of re-deriving context from scratch."
github_stars: 1324
verification: "listed"
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

Use the upstream install or setup path that matches your environment:
- uv tool install memsearch # via uv
- pipx install memsearch # via pipx
- pip install memsearch # plain pip
- uv add memsearch # via uv, adds to pyproject.toml

Requirements and caveats from upstream:
- <a href="https://pypi.org/project/memsearch/"><img src="https://img.shields.io/badge/python-%3E%3D3.10-blue?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
- 👥 **For Agent Users**, install a plugin and get persistent memory with zero effort; **for Agent Developers**, use the full [CLI](https://zilliztech.github.io/memsearch/cli/) and [Python API](https://zilliztech.github....
- Beyond ready-to-use plugins, memsearch provides a complete **CLI and Python API** for building memory into your own agents. Whether you're adding persistent context to a custom agent, building a memory-augmented RAG p...

Basic usage or getting-started notes:
- ### How Plugins Work (Claude Code as example)
- # memsearch command or any of the agent plugins (Claude Code, Codex,
- # OpenClaw, OpenCode), which all shell out to the CLI.

- Source: https://github.com/zilliztech/memsearch
- Extracted from upstream docs: https://raw.githubusercontent.com/zilliztech/memsearch/HEAD/README.md

## Documentation

- https://github.com/zilliztech/memsearch#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-cross-agent-markdown-memory-and-conversation-history-with-memsearch/)
