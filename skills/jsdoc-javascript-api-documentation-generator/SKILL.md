---
name: JSDoc JavaScript API Documentation Generator
description: JSDoc is the standard API documentation generator for JavaScript. It
  parses specially-formatted comments in JavaScript source code to produce HTML documentation
  pages. With 15,000+ GitHub stars and millions of npm downloads, it is the most widely
  adopted JavaScript documentation tool and the foundation of the JSDoc comment standard
  used across the entire JS ecosystem.
verification: security_reviewed
source: https://github.com/jsdoc/jsdoc
category:
- Library &amp; API Reference
framework:
- Custom Agents
tool_ecosystem:
  github_repo: jsdoc/jsdoc
  github_stars: 15426
  ase_npm_package: jsdoc
  npm_weekly_downloads: 2663272
---
# JSDoc JavaScript API Documentation Generator

JSDoc is the canonical API documentation generator for JavaScript projects. It reads structured comment annotations (the JSDoc comment format using /** ... */ blocks with @param, @returns, @typedef, and other tags) from JavaScript source files and generates navigable HTML documentation sites. The JSDoc comment format has become a de facto standard, supported by IDEs like VS Code for inline type hints and by TypeScript for type checking JavaScript files via JSDoc annotations.
How It Works
An agent skill wrapping JSDoc enables automated documentation generation from JavaScript codebases. The agent invokes the jsdoc CLI with source file paths or directories, and JSDoc parses all annotated comments to extract function signatures, parameter types and descriptions, return values, class hierarchies, module definitions, events, and custom type definitions. The tool produces a complete static HTML site with navigation, search, and cross-referenced links between documented symbols.
Comment Tags and Configuration
JSDoc supports a rich set of documentation tags including @param for function parameters with types, @returns for return values, @typedef for custom type definitions, @class and @constructor for classes, @module for module declarations, @fires and @listens for events, @example for code examples, @deprecated for deprecation notices, and @see for cross-references. Configuration is managed via a jsdoc.json (or conf.json) file that specifies source directories, recursion depth, template/theme selection, plugins, and output directory.
Template and Plugin Ecosystem
JSDoc features a plugin system that enables custom tag definitions, AST transformations, and output modifications. The template system allows complete customization of the generated documentation appearance. Popular community templates include clean-jsdoc-theme, docdash, and better-docs. Plugins can add support for additional comment tags, integrate with Markdown rendering, or inject custom metadata into the output.
Agent Integration
For AI agents, JSDoc serves two purposes: generating human-readable documentation sites, and extracting structured API information that the agent can use to understand a codebase. The agent can invoke JSDoc in JSON output mode to get a machine-readable representation of all documented symbols, or generate HTML docs and deploy them to documentation hosting services. JSDoc integrates naturally into CI/CD pipelines for continuous documentation updates. It installs via npm (npm install --save-dev jsdoc) and runs on any Node.js environment.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jsdoc-javascript-api-documentation-generator/)
