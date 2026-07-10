---
title: "Generate Go API docs from source annotations with Swag"
description: "Use Swag when an agent needs to turn Go handler annotations into reviewable Swagger 2.0 documentation before API docs, clients, or release checks depend on it."
verification: "security_reviewed"
source: "https://github.com/swaggo/swag"
author: "swaggo"
publisher_type: "open_source"
category:
  - "Library & API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "swaggo/swag"
  github_stars: 12867
---

# Generate Go API docs from source annotations with Swag

Use Swag when an agent needs to turn Go handler annotations into reviewable Swagger 2.0 documentation before API docs, clients, or release checks depend on it.

## Prerequisites

Go 1.19 or newer; Swag CLI or Docker image; Go API source tree with handler annotations

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with go install github.com/swaggo/swag/cmd/swag@latest, then run swag init from the project root containing main.go. Use swag init -g path/to/file.go when the general API annotations live outside main.go, and import the generated docs package as described in the upstream README.
```

## Documentation

- https://github.com/swaggo/swag

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-go-api-docs-from-source-annotations-with-swag/)
