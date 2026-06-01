---
name: "Use Potpie for spec-driven codebase workflows"
slug: "use-potpie-for-spec-driven-codebase-workflows"
description: "Index a repository with Potpie, turn it into a code knowledge graph, and drive focused implementation or review tasks from specs."
github_stars: 5411
verification: "security_reviewed"
source: "https://github.com/potpie-ai/potpie"
author: "Potpie AI"
publisher_type: "open_source"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "potpie-ai/potpie"
  github_stars: 5411
---

# Use Potpie for spec-driven codebase workflows

Index a repository with Potpie, turn it into a code knowledge graph, and drive focused implementation or review tasks from specs.

## Prerequisites

Docker; Git; Python 3.11+; uv; configured LLM provider

## Installation

Use the upstream install or setup path that matches your environment:
- git clone --recurse-submodules https://github.com/potpie-ai/potpie.git
- uv sync
- pnpm build && pnpm start

Requirements and caveats from upstream:
- [Docker](https://docker.com) installed and running
- [Python 3.11+](https://python.org) with [uv](https://docs.astral.sh/uv/)
- This will start Docker services, apply migrations, start the FastAPI app, and start the Celery worker.

Basic usage or getting-started notes:
- [Git](https://git-scm.com) installed
- **Clone the repository**
- bash

- Source: https://github.com/potpie-ai/potpie
- Extracted from upstream docs: https://raw.githubusercontent.com/potpie-ai/potpie/HEAD/README.md

## Documentation

- https://docs.potpie.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/use-potpie-for-spec-driven-codebase-workflows/)
