---
name: "Generate Go API docs from source annotations with Swag"
slug: "generate-go-api-docs-from-source-annotations-with-swag"
description: "Use Swag when an agent needs to turn Go handler annotations into reviewable Swagger 2.0 documentation before API docs, clients, or release checks depend on it."
github_stars: 12867
verification: "security_reviewed"
source: "https://github.com/swaggo/swag"
author: "swaggo"
publisher_type: "open_source"
category: "Library & API Reference"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "swaggo/swag"
  github_stars: 12867
---

# Generate Go API docs from source annotations with Swag

Use Swag when an agent needs to turn Go handler annotations into reviewable Swagger 2.0 documentation before API docs, clients, or release checks depend on it.

## Prerequisites

Go 1.19 or newer; Swag CLI or Docker image; Go API source tree with handler annotations

## Installation

Use the upstream install or setup path that matches your environment:
- go install github.com/swaggo/swag/cmd/swag@latest
- docker run --rm -v $(pwd):/code ghcr.io/swaggo/swag:latest
- Make sure to import the generated docs/docs.go so that your specific configuration gets init'ed. If your General API annotations do not live in main.go, you can let swag know with -g flag.
- Make it OR condition

Requirements and caveats from upstream:
- Alternatively you can run the docker image:
- --dir value, -d value Directories you want to parse,comma separated and general-info file must be in the first one (default: "./")
- | x-name | The extension key, must be start by x- and take only json value | // @x-example-key {"key": "value"} |

Basic usage or getting-started notes:
- [Getting started](#getting-started)
- [Example value of struct](#example-value-of-struct)
- Add comments to your API source code, See [Declarative Comments Format](#declarative-comments-format).

- Source: https://github.com/swaggo/swag
- Extracted from upstream docs: https://raw.githubusercontent.com/swaggo/swag/HEAD/README.md

## Documentation

- https://github.com/swaggo/swag

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-go-api-docs-from-source-annotations-with-swag/)
