---
name: "Validate JSON data and config files against schemas with ajv-cli"
slug: "validate-json-data-and-config-files-against-schemas-with-ajv-cli"
description: "Run schema checks from the shell or CI so malformed JSON, JSON5, or YAML inputs fail before they reach downstream tooling."
github_stars: 308
verification: "security_reviewed"
source: "https://github.com/ajv-validator/ajv-cli"
author: "ajv-validator maintainers"
publisher_type: "organization"
category: "Library & API Reference"
framework: "Multi-Framework"
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

Use the upstream install or setup path that matches your environment:
- npm install -g ajv-cli

Requirements and caveats from upstream:
- Multiple schemas can be passed both by using this parameter multiple times and with [glob patterns](https://github.com/isaacs/node-glob#glob-primer). Glob pattern should be quoted and extensions cannot be omitted.
- These modules can be written in TypeScript if you have ts-node installed.
- Multiple schemas can be passed both by using this parameter multiple times and with [glob patterns](https://github.com/isaacs/node-glob#glob-primer).

Basic usage or getting-started notes:
- sh
- ## JSON schema language and version
- Parameter --spec can be used with all commands (other than help) to choose JSON schema language:

- Source: https://github.com/ajv-validator/ajv-cli
- Extracted from upstream docs: https://raw.githubusercontent.com/ajv-validator/ajv-cli/HEAD/README.md

## Documentation

- https://github.com/ajv-validator/ajv-cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-json-data-and-config-files-against-schemas-with-ajv-cli/)
