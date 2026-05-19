---
name: "Run repeatable model and agent eval suites and inspect scoring traces with Inspect AI"
slug: "run-repeatable-model-and-agent-eval-suites-and-inspect-scoring-traces-with-inspect-ai"
description: "Run benchmark-style eval suites against models or agents, then inspect scored traces instead of relying on ad hoc chats and gut feel."
github_stars: 1904
verification: "security_reviewed"
source: "https://github.com/UKGovernmentBEIS/inspect_ai"
author: "UK AI Security Institute"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ukgovernmentbeis/inspect_ai"
  github_stars: 1904
---

# Run repeatable model and agent eval suites and inspect scoring traces with Inspect AI

Run benchmark-style eval suites against models or agents, then inspect scored traces instead of relying on ad hoc chats and gut feel.

## Prerequisites

Python environment, inspect-ai package, model provider credentials, evaluation datasets or task definitions, optional sandbox dependencies for agent tasks

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/UKGovernmentBEIS/inspect_ai.git
- pip install -e ".[dev]"
- uv sync --extra dev
- make hooks

Requirements and caveats from upstream:
- If you use VS Code, you should be sure to have installed the recommended extensions (Python, Ruff, and MyPy). Note that you'll be prompted to install these when you open the project in VS Code.
- The web UI lives in a git submodule at src/inspect_ai/_view/ts-mono/. **These steps are only needed if you plan to work on the TypeScript/React frontend** — Python-only contributors can skip this entirely.

Basic usage or getting-started notes:
- Inspect provides many built-in components, including facilities for prompt engineering, tool usage, multi-turn dialog, and model graded evaluations. Extensions to Inspect (e.g. to support new elicitation and scoring t...
- Inspect also includes a collection of over 200 pre-built evaluations ready to run on any model (learn more at <https://inspect.aisi.org.uk/evals/>).
- Run linting, formatting, and tests via

- Source: https://github.com/UKGovernmentBEIS/inspect_ai
- Extracted from upstream docs: https://raw.githubusercontent.com/UKGovernmentBEIS/inspect_ai/HEAD/README.md

## Documentation

- https://inspect.aisi.org.uk/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-repeatable-model-and-agent-eval-suites-and-inspect-scoring-traces-with-inspect-ai/)
