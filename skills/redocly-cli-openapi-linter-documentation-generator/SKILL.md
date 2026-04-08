---
title: Redocly CLI OpenAPI Linter and Documentation Generator
description: 'Redocly CLI is a comprehensive command-line tool for working with API
  descriptions throughout the API lifecycle. Built by Redocly, the company behind
  the popular Redoc documentation renderer (24k+ GitHub stars), the CLI handles linting,
  validation, bundling, and documentation generation for OpenAPI and AsyncAPI specifications.
  Supported Formats The tool supports a wide range of API description formats: OpenAPI
  3.2, 3.1, and 3.0, legacy Swagger 2.0, AsyncAPI 3.0 and 2.6, and Arazzo 1.0 workflow
  descriptions. This broad format support makes it useful across organizations with
  varying API standards. Linting and Validation The lint command checks API descriptions
  against configurable rulesets. Unlike tools that use JSONPath for rule targeting,
  Redocly CLI uses simple expressions that understand API specification structure,
  making rules easier to write and maintain. Built-in rulesets cover common API governance
  concerns, and teams can create custom rules for organization-specific standards.
  The linter is optimized for speed even on large documents. Bundling Most teams split
  API descriptions across multiple files using $ref references, but some tools don’t
  support multi-file specs. The bundle command recombines split documents into a single
  clean file that looks human-written, solving compatibility issues with downstream
  tooling. Documentation Generation The build-docs command uses Redoc to generate
  beautiful, interactive API reference documentation as a single HTML file. The output
  is customizable with themes, logos, and navigation options. A preview command enables
  local development with live reloading. Agent Integration For AI agents, Redocly
  CLI enables automated API governance workflows: lint specs on every commit, catch
  breaking changes in PRs, bundle multi-file specs for deployment, and generate documentation
  as part of CI/CD pipelines. Agents can use the structured lint output to suggest
  fixes for API design issues. Install via npm with npm install @redocly/cli -g or
  run without installation using npx @redocly/cli@latest . Docker images are also
  available. The project is MIT-licensed and hosted at github.com/Redocly/redocly-cli.'
verification: security_reviewed
source: https://github.com/Redocly/redocly-cli
category:
- Developer Tools
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: redocly/redocly-cli
  github_stars: 1422
---

# Redocly CLI OpenAPI Linter and Documentation Generator

Redocly CLI is a comprehensive command-line tool for working with API descriptions throughout the API lifecycle. Built by Redocly, the company behind the popular Redoc documentation renderer (24k+ GitHub stars), the CLI handles linting, validation, bundling, and documentation generation for OpenAPI and AsyncAPI specifications. Supported Formats The tool supports a wide range of API description formats: OpenAPI 3.2, 3.1, and 3.0, legacy Swagger 2.0, AsyncAPI 3.0 and 2.6, and Arazzo 1.0 workflow descriptions. This broad format support makes it useful across organizations with varying API standards. Linting and Validation The lint command checks API descriptions against configurable rulesets. Unlike tools that use JSONPath for rule targeting, Redocly CLI uses simple expressions that understand API specification structure, making rules easier to write and maintain. Built-in rulesets cover common API governance concerns, and teams can create custom rules for organization-specific standards. The linter is optimized for speed even on large documents. Bundling Most teams split API descriptions across multiple files using $ref references, but some tools don’t support multi-file specs. The bundle command recombines split documents into a single clean file that looks human-written, solving compatibility issues with downstream tooling. Documentation Generation The build-docs command uses Redoc to generate beautiful, interactive API reference documentation as a single HTML file. The output is customizable with themes, logos, and navigation options. A preview command enables local development with live reloading. Agent Integration For AI agents, Redocly CLI enables automated API governance workflows: lint specs on every commit, catch breaking changes in PRs, bundle multi-file specs for deployment, and generate documentation as part of CI/CD pipelines. Agents can use the structured lint output to suggest fixes for API design issues. Install via npm with npm install @redocly/cli -g or run without installation using npx @redocly/cli@latest . Docker images are also available. The project is MIT-licensed and hosted at github.com/Redocly/redocly-cli.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/redocly-cli-openapi-linter-documentation-generator/)
