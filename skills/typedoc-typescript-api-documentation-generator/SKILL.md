---
name: "TypeDoc TypeScript API Documentation Generator"
description: "TypeDoc is the standard documentation generator for TypeScript projects. It reads TypeScript source code and JSDoc comments to produce structured HTML documentation or JSON models. With 8,000+ GitHub stars and widespread npm adoption, it powers API reference generation for thousands of TypeScript libraries."
category: "Library &amp; API Reference"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/TypeStrong/typedoc"
---
# TypeDoc TypeScript API Documentation Generator

TypeDoc is the standard documentation generator for TypeScript projects. It reads TypeScript source code and JSDoc comments to produce structured HTML documentation or JSON models. With 8,000+ GitHub stars and widespread npm adoption, it powers API reference generation for thousands of TypeScript libraries.

## Overview

TypeDoc is the go-to documentation generator for TypeScript projects, converting source code comments into fully navigable HTML documentation sites or structured JSON models. As an agent skill, TypeDoc enables AI agents to automatically generate, update, and maintain API reference documentation for any TypeScript codebase without manual configuration.

How It Works
TypeDoc analyzes TypeScript source files using the TypeScript compiler API to extract type information, function signatures, class hierarchies, interfaces, enums, and module structures. It combines this structural analysis with JSDoc/TSDoc comment parsing to produce comprehensive documentation that includes descriptions, parameter types, return types, examples, and cross-references between related symbols. The agent invokes TypeDoc via its CLI with the project entry point and it automatically discovers the tsconfig.json for compiler settings.

Output Formats and Customization
TypeDoc supports two primary output modes: HTML documentation sites (via --out) and JSON reflection models (via --json). The HTML output generates a complete, navigable documentation site with a sidebar, search functionality, and syntax-highlighted code examples. The JSON output produces a detailed AST-like model of the project structure that agents can programmatically traverse, query, or transform. TypeDoc supports theming, custom plugins, and configurable entry point strategies including package-mode for monorepos.

Integration Points
An agent skill wrapping TypeDoc can be triggered on code changes to regenerate documentation automatically, validate that all public APIs have documentation comments, or generate documentation diffs during code review. The JSON output mode is particularly useful for agents that need to understand a codebase structure: the agent can query the JSON model to find all exported functions, their parameter types, and return types without parsing source code directly. TypeDoc integrates with CI/CD pipelines for continuous documentation deployment.

Configuration and Extensibility
TypeDoc reads configuration from typedoc.json or command-line flags. Key options include entry points, output directory, theme selection, exclusion patterns, and readme file specification. The plugin system supports custom renderers, additional comment tags, and output transformations. The entryPointStrategy option supports packages mode for documenting multi-package monorepos in a single unified output, and merge mode for combining documentation from separately built projects.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill typedoc-typescript-api-documentation-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill typedoc-typescript-api-documentation-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill typedoc-typescript-api-documentation-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill typedoc-typescript-api-documentation-generator -a codex
```

### OpenClaw

```bash
clawhub install typedoc-typescript-api-documentation-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typedoc-typescript-api-documentation-generator/)
