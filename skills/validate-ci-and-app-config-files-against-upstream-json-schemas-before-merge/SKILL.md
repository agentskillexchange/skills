---
name: "Validate CI and app config files against upstream JSON schemas before merge"
slug: "validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge"
description: "Use check-jsonschema when an agent needs to catch broken GitHub Actions, Renovate, Azure Pipelines, and other schema-backed config files before they hit CI. The agent picks the right schema hook, validates the changed files, and reports the exact key or structure that drifted from the contract."
github_stars: 312
verification: "security_reviewed"
source: "https://github.com/python-jsonschema/check-jsonschema"
author: "Stephen Rosen"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "python-jsonschema/check-jsonschema"
  github_stars: 312
---

# Validate CI and app config files against upstream JSON schemas before merge

Use check-jsonschema when an agent needs to catch broken GitHub Actions, Renovate, Azure Pipelines, and other schema-backed config files before they hit CI. The agent picks the right schema hook, validates the changed files, and reports the exact key or structure that drifted from the contract.

## Prerequisites

Python 3.10+, pipx or pre-commit

## Installation

Use the upstream install or setup path that matches your environment:
- pipx install check-jsonschema
- brew install check-jsonschema

Requirements and caveats from upstream:
- [![build](https://github.com/python-jsonschema/check-jsonschema/actions/workflows/build.yaml/badge.svg)](https://github.com/python-jsonschema/check-jsonschema/actions/workflows/build.yaml)
- [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/python-jsonschema/check-jsonschema/main.svg)](https://results.pre-commit.ci/latest/github/python-jsonschema/check-jsonschema/main)
- A JSON Schema CLI and [pre-commit](https://pre-commit.com/) hook built on [jsonschema](https://github.com/python-jsonschema/jsonschema/).

Basic usage or getting-started notes:
- check-jsonschema can be installed and run as a CLI tool, or via pre-commit.
- ### Example pre-commit config
- The following configuration uses check-jsonschema to validate Github Workflow

- Source: https://github.com/python-jsonschema/check-jsonschema
- Extracted from upstream docs: https://raw.githubusercontent.com/python-jsonschema/check-jsonschema/HEAD/README.md

## Documentation

- https://check-jsonschema.readthedocs.io/en/stable/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge/)
