---
name: "Run configurable multi-source deep research passes with Open Deep Research"
slug: "run-configurable-multi-source-deep-research-passes-with-open-deep-research"
description: "Use Open Deep Research when an agent should run a configurable research job that searches, compresses, synthesizes, and writes a cited report across multiple model and search backends."
github_stars: 11125
verification: "security_reviewed"
source: "https://github.com/langchain-ai/open_deep_research"
author: "LangChain"
publisher_type: "organization"
category: "Research & Scraping"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "langchain-ai/open_deep_research"
  github_stars: 11125
---

# Run configurable multi-source deep research passes with Open Deep Research

Use Open Deep Research when an agent should run a configurable research job that searches, compresses, synthesizes, and writes a cited report across multiple model and search backends.

## Prerequisites

Python, uv, model API credentials, one or more supported search tools

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/langchain-ai/open_deep_research.git
- uv venv
- uv sync
- uv pip install -r pyproject.toml

Requirements and caveats from upstream:
- uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --allow-blocking
- Open Deep Research supports a wide range of LLM providers via the [init_chat_model() API](https://python.langchain.com/docs/how_to/chat_models_universal_init/). It uses LLMs for a few different tasks. See the below mo...
- Note: the selected model will need to support [structured outputs](https://python.langchain.com/docs/integrations/chat/) and [tool calling](https://python.langchain.com/docs/how_to/tool_calling/).

Basic usage or getting-started notes:
- cp .env.example .env
- This will open the LangGraph Studio UI in your browser.
- 🚀 API: http://127.0.0.1:2024

- Source: https://github.com/langchain-ai/open_deep_research
- Extracted from upstream docs: https://raw.githubusercontent.com/langchain-ai/open_deep_research/HEAD/README.md

## Documentation

- https://github.com/langchain-ai/open_deep_research#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-configurable-multi-source-deep-research-passes-with-open-deep-research/)
