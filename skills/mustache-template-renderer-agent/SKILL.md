---
name: "Mustache Template Renderer"
description: "Renders Mustache logic-less templates with partials resolution and lambda support. Uses the mustache.js library for client and server-side rendering with custom delimiter configuration."
category: "Templates &amp; Workflows"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/mustache-template-renderer-agent/"
---
# Mustache Template Renderer

Renders Mustache logic-less templates with partials resolution and lambda support. Uses the mustache.js library for client and server-side rendering with custom delimiter configuration.

## Overview

The Mustache Template Renderer skill provides automated rendering of Mustache logic-less templates using the mustache.js library. It supports the full Mustache specification including variables, sections, inverted sections, partials, and comments with proper HTML entity escaping.

Core rendering capabilities include partial template resolution from configurable directories, lambda function support for dynamic content generation, and custom delimiter configuration for embedding Mustache within other template syntaxes. The skill handles template caching via Mustache.parse() for improved performance on repeated renders.

Data binding features include deep object path resolution with dot notation, array iteration with implicit iterators, and context stack traversal for inherited variable access. The skill processes data from JSON, YAML, and TOML sources with automatic type coercion for Mustache truthiness rules.

Output management includes batch rendering of template sets against data arrays, output file naming via template variables, and integration with build pipelines through the mustache CLI command for static site generation and email template compilation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mustache-template-renderer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mustache-template-renderer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mustache-template-renderer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mustache-template-renderer-agent -a codex
```

### OpenClaw

```bash
clawhub install mustache-template-renderer-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mustache-template-renderer-agent/)
