---
name: "AutoGen — Microsoft Multi-Agent Conversation Framework"
slug: "autogen-microsoft-multi-agent-framework"
description: "AutoGen is Microsoft's open-source framework for building multi-agent systems where AI agents converse with each other and humans to solve tasks, with support for tool use and human-in-the-loop workflows."
github_stars: 56777
verification: "listed"
source: "https://github.com/microsoft/autogen"
author: "Microsoft Research"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "microsoft/autogen"
  github_stars: 56777
---

# AutoGen — Microsoft Multi-Agent Conversation Framework

AutoGen is Microsoft's open-source framework for building multi-agent systems where AI agents converse with each other and humans to solve tasks, with support for tool use and human-in-the-loop workflows.

## Prerequisites

Python 3.10+, pip, OpenAI API key or compatible LLM

## Installation

Use the upstream install or setup path that matches your environment:
- pip install -U "autogen-agentchat" "autogen-ext[openai]"
- pip install -U "autogenstudio"
- # First run npm install -g @playwright/mcp@latest to install the MCP server.

Requirements and caveats from upstream:
- AutoGen requires **Python 3.10 or later**.
- python
- [Core API](./python/packages/autogen-core/) implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python.

Basic usage or getting-started notes:
- bash
- The current stable version can be found in the [releases](https://github.com/microsoft/autogen/releases). If you are upgrading from AutoGen v0.2, please refer to the [Migration Guide](https://microsoft.github.io/autog...
- The following samples call OpenAI API, so you first need to create an account and export your key as export OPENAI_API_KEY="sk-...".

- Source: https://github.com/microsoft/autogen
- Extracted from upstream docs: https://raw.githubusercontent.com/microsoft/autogen/HEAD/README.md

## Documentation

- https://microsoft.github.io/autogen/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/autogen-microsoft-multi-agent-framework/)
