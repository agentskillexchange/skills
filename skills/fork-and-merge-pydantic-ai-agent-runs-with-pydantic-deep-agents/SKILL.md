---
name: "Fork and merge Pydantic AI agent runs with Pydantic Deep Agents"
slug: "fork-and-merge-pydantic-ai-agent-runs-with-pydantic-deep-agents"
description: "Run a self-hosted terminal agent or custom Pydantic AI harness that can branch a coding or research run, test isolated alternatives, and merge the winning branch."
github_stars: 912
verification: "security_reviewed"
source: "https://github.com/vstorm-co/pydantic-deepagents"
author: "vstorm-co"
publisher_type: "organization"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "vstorm-co/pydantic-deepagents"
  github_stars: 912
---

# Fork and merge Pydantic AI agent runs with Pydantic Deep Agents

Run a self-hosted terminal agent or custom Pydantic AI harness that can branch a coding or research run, test isolated alternatives, and merge the winning branch.

## Prerequisites

Python 3.10+, pydantic-deep CLI or Python package, approved model provider key, optional sandbox support for isolated execution

## Installation

Use the upstream install or setup path that matches your environment:
- uv run deepresearch # → http://localhost:8080

Requirements and caveats from upstream:
- A self-hosted <b>terminal AI assistant</b> <i>and</i> the <b>Python framework</b> behind it.<br>
- <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=white" alt="Python 3.10+"></a>
- python

Basic usage or getting-started notes:
- <a href="#-live-run-forking--the-feature-no-one-else-has">Forking</a> &middot;
- When an agent hits a fork in the road — "should I refactor this with a decorator or a context manager?" — most tools force one bet. Pydantic Deep Agents lets the run **branch**:
- agent.run("refactor auth") ──┬─┼── branch B: "use a context manager" ── tests: 6/8 ✗ conf 0.42

- Source: https://github.com/vstorm-co/pydantic-deepagents
- Extracted from upstream docs: https://raw.githubusercontent.com/vstorm-co/pydantic-deepagents/HEAD/README.md

## Documentation

- https://vstorm-co.github.io/pydantic-deepagents/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fork-and-merge-pydantic-ai-agent-runs-with-pydantic-deep-agents/)
