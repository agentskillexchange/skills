---
name: "Add graph-backed memory and context retrieval to agent workflows"
slug: "add-graph-backed-memory-and-context-retrieval-to-agent-workflows"
description: "Use Cognee to ingest project knowledge into graph and vector memory so agents can retrieve durable context across sessions and workflows."
github_stars: 17584
verification: "security_reviewed"
source: "https://github.com/topoteretes/cognee"
author: "topoteretes"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "topoteretes/cognee"
  github_stars: 17584
---

# Add graph-backed memory and context retrieval to agent workflows

Use Cognee to ingest project knowledge into graph and vector memory so agents can retrieve durable context across sessions and workflows.

## Prerequisites

Python, Cognee, LLM provider credentials, optional graph/vector database backend

## Installation

Prerequisite: Python 3.10 to 3.14.

Install Cognee with uv or pip:

- uv pip install cognee
- pip install cognee

For Claude Code persistent memory, upstream documents installing the Cognee integration plugin:

- claude plugin marketplace add topoteretes/cognee-integrations
- claude plugin install cognee-memory@cognee

- Source: https://github.com/topoteretes/cognee
- Extracted from upstream docs: https://raw.githubusercontent.com/topoteretes/cognee/HEAD/README.md

## Documentation

- https://docs.cognee.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-graph-backed-memory-and-context-retrieval-to-agent-workflows/)
