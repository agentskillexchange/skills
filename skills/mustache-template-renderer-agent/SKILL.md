---
name: "Mustache Template Renderer"
description: "Renders Mustache logic-less templates with partials resolution and lambda support. Uses the mustache.js library for client and server-side rendering with custom delimiter configuration."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/mustache-template-renderer-agent/"
category:
  - "Templates &amp; Workflows"
framework:
  - "OpenClaw"
---

# Mustache Template Renderer

The Mustache Template Renderer skill provides automated rendering of Mustache logic-less templates using the mustache.js library. It supports the full Mustache specification including variables, sections, inverted sections, partials, and comments with proper HTML entity escaping.
Core rendering capabilities include partial template resolution from configurable directories, lambda function support for dynamic content generation, and custom delimiter configuration for embedding Mustache within other template syntaxes. The skill handles template caching via Mustache.parse() for improved performance on repeated renders.
Data binding features include deep object path resolution with dot notation, array iteration with implicit iterators, and context stack traversal for inherited variable access. The skill processes data from JSON, YAML, and TOML sources with automatic type coercion for Mustache truthiness rules.
Output management includes batch rendering of template sets against data arrays, output file naming via template variables, and integration with build pipelines through the mustache CLI command for static site generation and email template compilation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mustache-template-renderer-agent/)
