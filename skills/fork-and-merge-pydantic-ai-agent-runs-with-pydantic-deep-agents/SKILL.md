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

Install the package in the Python environment that will run the local agent harness:

```bash
pip install pydantic-deep
```

Use the upstream documentation for current CLI and framework setup details:

- https://vstorm-co.github.io/pydantic-deepagents/

A minimal ASE-safe workflow is:

1. Install the package and CLI in an isolated Python environment.
2. Configure only the approved model provider credentials needed by your harness.
3. Run a branch or fork workflow from a self-hosted terminal agent or custom Pydantic AI agent.
4. Compare branch outputs with tests, traces, or review notes.
5. Merge or select the winning branch only after a human reviews the evidence.

Treat this as a self-hosted custom-agent workflow for branching and evaluating Pydantic AI runs. It is not a generic Claude Code replacement, and it should not be wired to broad shell or repository permissions until the branch/test/merge loop is constrained and reviewed.

## Documentation

- https://vstorm-co.github.io/pydantic-deepagents/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fork-and-merge-pydantic-ai-agent-runs-with-pydantic-deep-agents/)
