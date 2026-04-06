---
name: JSDoc JavaScript API Documentation Generator
description: JSDoc is the standard API documentation generator for JavaScript. It
  parses specially-formatted comments in JavaScript source code to produce HTML documentation
  pages. With 15,000+ GitHub stars and millions of npm downloads, it is the most widely
  adopted JavaScript documentation tool and the foundation of the JSDoc comment standard
  used across the entire JS ecosystem.
category: "Library &amp; API Reference"
framework: Custom Agents
verification: security_reviewed
source: "https://github.com/jsdoc/jsdoc"
tool_ecosystem:
  github_repo: "https://github.com/jsdoc/jsdoc"
  github_stars: 15426
  npm_package: jsdoc
  npm_weekly_downloads: 2821540
---
# JSDoc JavaScript API Documentation Generator

JSDoc is the standard API documentation generator for JavaScript. It parses specially-formatted comments in JavaScript source code to produce HTML documentation pages. With 15,000+ GitHub stars and millions of npm downloads, it is the most widely adopted JavaScript documentation tool and the foundation of the JSDoc comment standard used across the entire JS ecosystem.

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

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jsdoc-javascript-api-documentation-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jsdoc-javascript-api-documentation-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jsdoc-javascript-api-documentation-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jsdoc-javascript-api-documentation-generator -a codex
```

### OpenClaw

```bash
clawhub install jsdoc-javascript-api-documentation-generator
```


## Source

- [GitHub](https://github.com/jsdoc/jsdoc)
