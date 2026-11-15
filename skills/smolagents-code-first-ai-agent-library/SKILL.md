---
name: "smolagents Code-First AI Agent Library"
slug: "smolagents-code-first-ai-agent-library"
description: "smolagents is HuggingFace's barebones Python library for building AI agents that think in code rather than JSON. Agents write and execute Python code as their action space, enabling more flexible reasoning and tool use with support for sandboxed execution via E2B, Docker, or WebAssembly."
github_stars: 26355
verification: "security_reviewed"
source: "https://github.com/huggingface/smolagents"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "huggingface/smolagents"
  github_stars: 26355
---

# smolagents Code-First AI Agent Library

smolagents is HuggingFace's barebones Python library for building AI agents that think in code rather than JSON. Agents write and execute Python code as their action space, enabling more flexible reasoning and tool use with support for sandboxed execution via E2B, Docker, or WebAssembly.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install "smolagents[toolkit]"

Requirements and caveats from upstream:
- Our [CodeAgent](https://huggingface.co/docs/smolagents/reference/agents#smolagents.CodeAgent) works mostly like classical ReAct agents - the exception being that the LLM engine writes its actions as Python code snippets.
- Actions are now Python code snippets. Hence, tool calls will be performed as Python function calls. For instance, here is how the agent can perform web search over several websites in one single action:
- [Docker](https://www.docker.com/) — self-hosted container isolation

Basic usage or getting-started notes:
- smolagents is a library that enables you to run powerful agents in a few lines of code. It offers:
- 🧑‍💻 **First-class support for Code Agents**. Our [CodeAgent](https://huggingface.co/docs/smolagents/reference/agents#smolagents.CodeAgent) writes its actions in code (as opposed to "agents being used to write code")....
- Then define your agent, give it the tools it needs and run it!

- Source: https://github.com/huggingface/smolagents
- Extracted from upstream docs: https://raw.githubusercontent.com/huggingface/smolagents/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/smolagents-code-first-ai-agent-library/)
