---
title: "Mustache Template Renderer"
description: "Renders Mustache logic-less templates with partials resolution and lambda support. Uses the mustache.js library for client and server-side rendering with custom delimiter configuration."
verification: "security_reviewed"
source: "https://github.com/janl/mustache.js"
category:
  - "Templates & Workflows"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "janl/mustache.js"
  github_stars: 16718
  npm_package: "mustache"
  npm_weekly_downloads: 12663471
---

# Mustache Template Renderer

The Mustache Template Renderer skill provides automated rendering of Mustache logic-less templates using the mustache.js library. It supports the full Mustache specification including variables, sections, inverted sections, partials, and comments with proper HTML entity escaping.

Core rendering capabilities include partial template resolution from configurable directories, lambda function support for dynamic content generation, and custom delimiter configuration for embedding Mustache within other template syntaxes. The skill handles template caching via Mustache.parse() for improved performance on repeated renders.

Data binding features include deep object path resolution with dot notation, array iteration with implicit iterators, and context stack traversal for inherited variable access. The skill processes data from JSON, YAML, and TOML sources with automatic type coercion for Mustache truthiness rules.

Output management includes batch rendering of template sets against data arrays, output file naming via template variables, and integration with build pipelines through the mustache CLI command for static site generation and email template compilation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/mustache-template-renderer-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/mustache-template-renderer-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/mustache-template-renderer-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mustache-template-renderer-agent/)
