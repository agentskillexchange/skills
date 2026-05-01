---
title: "Validate JSON data and config files against schemas with ajv-cli"
description: "Run schema checks from the shell or CI so malformed JSON, JSON5, or YAML inputs fail before they reach downstream tooling."
verification: "listed"
source: "https://github.com/ajv-validator/ajv-cli"
author: "ajv-validator maintainers"
publisher_type: "organization"
category:
  - "Library & API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ajv-validator/ajv-cli"
  github_stars: 308
  npm_package: "ajv-cli"
  npm_weekly_downloads: 335297
---

# Validate JSON data and config files against schemas with ajv-cli

Run schema checks from the shell or CI so malformed JSON, JSON5, or YAML inputs fail before they reach downstream tooling.

## Prerequisites

Node.js, ajv-cli, one or more JSON Schema or JTD files, and target JSON, JSON5, or YAML data files

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install ajv-cli with npm or invoke it with npx, supply the schema and data paths with the documented validate, compile, migrate, or test commands, and use the exit code in scripts or CI gates.
```

## Documentation

- https://github.com/ajv-validator/ajv-cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-json-data-and-config-files-against-schemas-with-ajv-cli/)
