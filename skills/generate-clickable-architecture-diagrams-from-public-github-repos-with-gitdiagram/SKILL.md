---
name: "Generate clickable architecture diagrams from public GitHub repos with GitDiagram"
slug: "generate-clickable-architecture-diagrams-from-public-github-repos-with-gitdiagram"
description: "Turn a public GitHub repository into an interactive architecture diagram before onboarding, code review, or agent handoff."
github_stars: 15447
verification: "security_reviewed"
source: "https://github.com/ahmedkhaleel2004/gitdiagram"
author: "Ahmed Khaleel"
publisher_type: "open_source_project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ahmedkhaleel2004/gitdiagram"
  github_stars: 15447
---

# Generate clickable architecture diagrams from public GitHub repos with GitDiagram

Turn a public GitHub repository into an interactive architecture diagram before onboarding, code review, or agent handoff.

## Prerequisites

Public GitHub repository URL, web access, optional self-hosted OpenAI or OpenRouter configuration

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/ahmedkhaleel2004/gitdiagram.git
- docker-compose up --build -d
- docker-compose logs -f api

Requirements and caveats from upstream:
- That graph is validated against the actual file tree, retried with feedback if it contains bad paths or invalid connections, then compiled into Mermaid and validated again before it is shown. Any node tied to a real p...
- This keeps the backend's Python environment managed by uv and installs the backend Mermaid validator's Bun dependencies from backend/bun.lock.

Basic usage or getting-started notes:
- One implementation detail worth knowing: the Next backend validates Mermaid in-process in [src/server/generate/mermaid-validator.ts](/Users/ahmedkhaleel/repos/gitdiagram/src/server/generate/mermaid-validator.ts), whil...
- bun run install:backend
- cp .env.example .env

- Source: https://github.com/ahmedkhaleel2004/gitdiagram
- Extracted from upstream docs: https://raw.githubusercontent.com/ahmedkhaleel2004/gitdiagram/HEAD/README.md

## Documentation

- https://gitdiagram.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-clickable-architecture-diagrams-from-public-github-repos-with-gitdiagram/)
